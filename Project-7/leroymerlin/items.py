# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst


def clear_price(value):
    try:
        value = int(value.replace(' ', ''))
    except:
        return value
    return value

def actual_link(value):
    try:
        value = value.replace('w_82,h_82', 'w_2000,h_2000')
    except:
        return value
    return value

class LeroymerlinItem(scrapy.Item):
    link = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(clear_price), output_processor=TakeFirst())
    all_photos = scrapy.Field(input_processor=MapCompose(actual_link), output_processor=TakeFirst())
    _id = scrapy.Field()


