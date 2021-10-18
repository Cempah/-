# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from pymongo import MongoClient

class LabirintparserPipeline:
    def process_item(self, item, spider):
        item['basic_price'] = self.process_price(item['basic_price'])
        item['discounted_price'] = self.process_price(item['discounted_price'])
        item['book_rating'] = self.process_rating(item['book_rating'])

        return item

    def process_price(self, price):
        if price:
            return int(price)
        else:
            return "Сумма отсутствует"

    def process_rating(self, rating):
        if rating:
            try:
                return float(rating)
            except Exception:
                return "Рейтинг отсутствует"


class MongoPipeline(object):
    def __init__(self):
        MONGO_URI = 'mongodb://127.0.0.1:27017/'
        MONGO_DATABASE = 'book_db'

        client = MongoClient(MONGO_URI)
        self.mongo_base = client[MONGO_DATABASE]

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item