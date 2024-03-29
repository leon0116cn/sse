import json
import scrapy
from scrapy.http import Request
from sse.items import StockQuoteItem


class AshareQuotesSpider(scrapy.Spider):
    name = 'asharequotes'
    allowed_domains = ['http://yunhq.sse.com.cn']
    stock_keys = ['stock_code', 'stock_name', 'open_price', 'high_price', 'low_price', 'last_price', 'prev_price',
                  'chg_rate', 'volume', 'amount', 'trade_phase', 'chg_price', 'amp_rate', 'cpxxsubtype', 'cpxxprodusta']

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
        data = json.loads(response.text)
        for quotes in data.get('list'):
            quote_item = StockQuoteItem()
            quote_item.update(dict(zip(self.stock_keys, quotes)))
            quote_item['trade_date'] = data.get('date')
            quote_item['trade_time'] = data.get('time')
            quote_item['stock_total'] = data.get('total')
            yield quote_item


class KshareQuotesSpider(scrapy.Spider):
    name = 'ksharequotes'
    allowed_domains = ['http://yunhq.sse.com.cn']
    stock_keys = ['stock_code', 'stock_name', 'open_price', 'high_price', 'low_price', 'last_price', 'prev_price',
                  'chg_rate', 'volume', 'amount', 'trade_phase', 'chg_price', 'amp_rate', 'cpxxsubtype', 'cpxxprodusta']

    def start_requests(self):
        offset = 50
        max_count = 1000
        urls_template = 'http://yunhq.sse.com.cn:32041/v1/sh1/list/exchange/kshare?select=code%2Cname%2Copen%2C' \
                        'high%2Clow%2Clast%2Cprev_close%2Cchg_rate%2Cvolume%2Camount%2Ctradephase%2Cchange%2C' \
                        'amp_rate%2Ccpxxsubtype%2Ccpxxprodusta&order=&begin={0}&end={1}&_=1565835901771'
        start_urls = [urls_template.format(index, index + offset) for index in range(0, max_count, offset)]
        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        for quotes in data.get('list'):
            quote_item = StockQuoteItem()
            quote_item.update(dict(zip(self.stock_keys, quotes)))
            quote_item['trade_date'] = data.get('date')
            quote_item['trade_time'] = data.get('time')
            quote_item['stock_total'] = data.get('total')
            yield quote_item
