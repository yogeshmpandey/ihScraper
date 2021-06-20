# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem
from datetime import datetime

class CheckItemPipeline:
    def process_item(self, article, spider):
        if not article['price'] or not article['title']:
            raise DropItem('Missing something!')
        return article


