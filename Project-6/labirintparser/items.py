# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LabirintparserItem(scrapy.Item):
    link_book = scrapy.Field()
    book_name = scrapy.Field()
    authors = scrapy.Field()
    basic_price = scrapy.Field()
    discounted_price = scrapy.Field()
    book_rating = scrapy.Field()
    _id = scrapy.Field()

