# python_Scrapy入门

## 关键步骤：
1. scrapy startproject XXXX
2. scrapy genspider xxx "http://www.xxx.com"
3. 编写items.py，明确需要提取的数据  
4. 编写spiders/xxx.py，编写爬虫文件，处理请求和响应，以及提取数据（yield item）
5. 编写pipeline.py，编写管道文件，处理spider返回的item数据
6. 编写setting.py，启动管道组件ITEM_PIPELINES = {}，以及其他相关设置
7. 执行爬虫

### firstSpider---- 第一个scrapy小项目

### tencentSpider ---- 腾讯招聘网自动翻页采集

### douyuSpider ---- 斗鱼App抓包爬虫获取主播照片并用昵称进行重命名


