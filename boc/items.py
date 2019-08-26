import scrapy


class AtmItem(scrapy.Item):
    ss = scrapy.Field()
    cs = scrapy.Field()
    address_type = scrapy.Field()
    device_type = scrapy.Field()
    address = scrapy.Field()
    status = scrapy.Field()
    page_url = scrapy.Field()

