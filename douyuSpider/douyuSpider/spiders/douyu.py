# -*- coding: utf-8 -*-
import scrapy
import json
from douyuSpider.items import DouyuspiderItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']

    baseURL = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        # 将拿到的json文件转换成python
        data_list = json.loads(response.text)['data']
        if len(data_list) == 0:
            return
        for data in data_list:
            item = DouyuspiderItem()
            item["nickName"] = data["nickname"]
            item["imageLink"] = data["vertical_src"]

            yield item

        self.offset += 20
        yield scrapy.Request(self.baseURL + str(self.offset),callback=self.parse)