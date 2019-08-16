import scrapy


class StockQuoteItem(scrapy.Item):
    stock_code = scrapy.Field()
    stock_short = scrapy.Field()
    stock_type = scrapy.Field()
    last_price = scrapy.Field()
    change_per = scrapy.Field()
    change = scrapy.Field()
    turnover = scrapy.Field()
    volume = scrapy.Field()
    prev_price = scrapy.Field()
    open_price = scrapy.Field()
    high_price = scrapy.Field()
    low_price = scrapy.Field()
    range_price = scrapy.Field()
    ext1 = scrapy.Field()
    ext2 = scrapy.Field()
    query_date = scrapy.Field()
    query_time = scrapy.Field()