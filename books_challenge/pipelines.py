# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings

# Condition to Drop the Spider after scraping n number of items 
class BooksChallengePipeline:
    itemCount = 0
    settings = get_project_settings()

    def process_item(self, item, spider):
        if self.settings['CLOSESPIDER_ITEMCOUNT'] != 0 and self.itemCount >= self.settings['CLOSESPIDER_ITEMCOUNT']:
            raise DropItem(
                "ClOSESPIDER_ITEMCOUNT limit reached - " + str(self.settings['CLOSESPIDER_ITEMCOUNT']))
        else:
            self.itemCount += 1
            pass
        return item
