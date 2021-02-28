# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TorentNeighborhoodItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    postal_code=scrapy.Field()
    borough=scrapy.Field()
    neighborhood=scrapy.Field()
