# -*- coding: utf-8 -*-
import scrapy
from tencentSpider.items import TencentspiderItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    base_url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):

        for node in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 构建item对象，用来保存数据
            item = TencentspiderItem()

            item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0]

            item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0]
            # 防止由于该项为空时导致引起获取连接范围越界
            if len(node.xpath("./td[2]/text()")):
                item['positionType'] = node.xpath("./td[2]/text()").extract()[0]
            else:
                item['positionType'] = ""

            item['peopleNumber'] = node.xpath("./td[3]/text()").extract()[0]

            item['workLocation'] = node.xpath("./td[4]/text()").extract()[0]

            item['publishTime'] = node.xpath("./td[5]/text()").extract()[0]

            yield item

        # 第一种写法，拼接url，适用场景：页面没有可以点击的请求连接（如：下一页），必须通过拼接url才能获取响应
        # if self.offset < 2990:
        #     self.offset += 10
        #     url = self.base_url + str(self.offset)
        #     yield scrapy.Request(url,callback=self.parse)

        #第二种写法：直接从response获取需要爬取的连接，并发送请求处理，直到连接全部提取完
        #表示当“下一页”按钮处于active激活状态时，继续执行下一页，来依次获取信息
        if len(response.xpath("//a[@class='noactive' and @id='next']")) == 0:
            url = response.xpath("//a[@id='next']/@href").extract()[0]
            yield scrapy.Request("https://hr.tencent.com/" + url,callback=self.parse)
