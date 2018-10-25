# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 主播昵称
    nickName = scrapy.Field()
    # 图片链接
    imageLink = scrapy.Field()
