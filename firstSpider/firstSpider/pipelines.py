# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class FirstspiderPipeline(object):
    # 可选实现，做参数初始化等
    def __init__(self):
        self.f = codecs.open("item_popeline.json","w",encoding="utf-8")

    # item (Item 对象) – 被爬取的item
    # spider (Spider 对象) – 爬取该item的spider
    # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
    # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.f.write(content)
        return item

    # spider (Spider 对象) – 被关闭的spider
    # 可选实现，当spider被关闭时，这个方法被调用
    def close_spider(self,spider):
        self.f.close()
