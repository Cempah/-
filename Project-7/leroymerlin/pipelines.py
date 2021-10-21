# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class LeroymerlinPipeline:
    def process_item(self, item, spider):
        print()
        return item


class LeroymerlinPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['all_photos']:
            for img in item['all_photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as exc:
                    print(exc)

    def item_completed(self, results, item, info):
        item['all_photos'] = [itm[1] for itm in results if itm[0]]
        return item

    # def file_path(self, request, response=None, info=None, *, item=None):
    #     return