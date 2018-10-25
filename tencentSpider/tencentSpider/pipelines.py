# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class TencentspiderPipeline(object):

    def __init__(self):
        self.f = codecs.open("item_pipeline.json","w",encoding="utf-8")

    def process_item(self, item, spider):
        # 先将item对象转换成字典，再转换为字符串格式，最后添加\n换行符
        content = json.dumps(dict(item),ensure_ascii=False) + ",\n"
        self.f.write(content)
        return item

    def close_spider(self,spider):
        self.f.close()
