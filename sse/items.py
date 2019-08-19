import scrapy


class StockQuoteItem(scrapy.Item):
    stock_code = scrapy.Field()
    stock_name = scrapy.Field()
    open_price = scrapy.Field()
    high_price = scrapy.Field()
    low_price = scrapy.Field()
    last_price = scrapy.Field()
    prev_price = scrapy.Field()
    chg_rate = scrapy.Field()
    volume = scrapy.Field()
    amount = scrapy.Field()
    trade_phase = scrapy.Field()
    change = scrapy.Field()
    amp_rate = scrapy.Field()
    cpxxsubtype = scrapy.Field()
    cpxxprodusta = scrapy.Field()
    stock_total = scrapy.Field()
    trade_date = scrapy.Field()
    trade_time = scrapy.Field()
