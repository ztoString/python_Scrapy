# -*- coding: utf-8 -*-
import scrapy
from firstSpider.items import FirstspiderItem

class ItcastSpider(scrapy.Spider):
    # 爬虫名，启动爬虫时需要的参数（必需）
    name = 'itcast'
    # 爬取域范围，允许爬虫在这个域名下进行爬取（可选）
    allowed_domains = ['itcast.cn']  # 域名可以不写，防止出现范围错误
    # 起始url列表，爬虫执行后第一批请求，将从这个列表里获取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 在windows下面，新文件的默认编码是gbk，这样的话，python解释器会用gbk编码去解析我们的网络数据流txt
        # 然而txt此时已经是decode过的unicode编码，这样的话就会导致解析不了，出现上述问题。
        # 解决的办法就是，改变目标文件的编码：
        # with open("teacher.html", "w",encoding='utf-8') as f:
        #     f.write(response.text)

        # 存放老师信息的集合
        # items = []
        for each in response.xpath("//div[@class='li_txt']"):
            # 将我们得到的数据封装到一个 `FirstspiderItem` 对象
            item = FirstspiderItem()
            # extract()方法返回的都是unicode字符串
            # extract()方法返回的都是unicode字符串
            name = each.xpath("./h3/text()").extract()
            title = each.xpath("./h4/text()").extract()
            info = each.xpath("./p/text()").extract()

            # xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            # items.append(item)

            # 返回提取到的每个item文件，将数据交给pipeline，同时还会回来继续执行
            yield item

        # 直接返回最后数据
        # return items

