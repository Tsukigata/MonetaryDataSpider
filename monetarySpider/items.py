# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MonetarydataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stock_code = scrapy.Field()
    date = scrapy.Field()
    index = scrapy.Field()
    deal_time = scrapy.Field()
    deal_price = scrapy.Field()
    price_change = scrapy.Field()
    deal_amount = scrapy.Field()
    deal_amount_price = scrapy.Field()
    deal_attribute = scrapy.Field()
    
class MonetaryRealItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stock_code = scrapy.Field()
    date = scrapy.Field()
    ticktime = scrapy.Field()
    changepercent = scrapy.Field()
    volume = scrapy.Field()
    amount = scrapy.Field()
    price = scrapy.Field()
    pricechange = scrapy.Field()
    