import scrapy, logging, json
from scrapy.http import Request
from sse.items import StockQuotesItem


class StockquotesSpider(scrapy.Spider):
    name = 'stockquotes'
    allowed_domains = ['http://yunhq.sse.com.cn']

    def start_requests(self):
        offset = 50
        max_count = 1500
        urls_template = 'http://yunhq.sse.com.cn:32041/v1/sh1/list/exchange/ashare?select=code%2Cname%2Copen%2C' \
                        'high%2Clow%2Clast%2Cprev_close%2Cchg_rate%2Cvolume%2Camount%2Ctradephase%2Cchange%2C' \
                        'amp_rate%2Ccpxxsubtype%2Ccpxxprodusta&order=&begin={0}&end={1}&_=1565835901771'
        start_urls = [urls_template.format(index, index + offset) for index in range(0, max_count, offset)]
        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log('url = {0}'.format(response.url), logging.INFO)
        yield json.loads(response.text)

