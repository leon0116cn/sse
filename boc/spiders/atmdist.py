import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from boc.items import AtmItem


class AtmdistSpider(CrawlSpider):
    name = 'atmdist'
    allowed_domains = ['bankofchina.com']
    start_urls = ['http://www.bankofchina.com/sourcedb/atmdist/']
    atm_fields = ['ss', 'cs', 'address_type', 'device_type', 'address', 'status']
    pattern = re.compile(r'createPageHTML\((\d+), (\d+), "(.+)", "(.+)"\)')

    rules = (
        Rule(LinkExtractor(restrict_css='#apDiv1'), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.debug('**************** Current page url is : {0}'.format(response.request.url))
        for tr in response.css('#documentContainer tr'):
            atm_item = AtmItem()
            tds = tr.xpath('./td/text()').getall()
            if len(tds) > 0:
                atm_item = dict(zip(self.atm_fields, tds))
                atm_item['page_url'] = response.request.url
                yield atm_item

        next_url = self.get_next_page(response)
        self.logger.debug('**************** Next page url is : {0}'.format(next_url))
        if next_url is not None:
            yield response.follow(url=response.urljoin(next_url), callback=self.parse_item)

    def get_next_page(self, response):
        page_script = response.css('.turn_page').xpath('ol/script').get()
        m = self.pattern.search(page_script)
        if m is not None:
            total_page = int(m.group(1))
            current_page = int(m.group(2))
            file_name = m.group(3)
            file_extension = m.group(4)
            if current_page + 1 < total_page:
                next_page = current_page + 1
                next_page_url = file_name + '_' + str(next_page) + '.' + file_extension
                return next_page_url
