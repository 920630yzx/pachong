# -*- coding: utf-8 -*-
import scrapy
from app01.items import App01Item  # 新加入！

class TsSpider(scrapy.Spider):
    name = 'ts'
    allowed_domains = ['']  # 域名
    start_urls = ['https://ke.qq.com/']

    def parse(self, response):
        print('ts.py运行...开始爬取数据')  # 新加入！
        item = App01Item()   # 新加入！
        item['title'] = 'aaa'   # 新加入！
        yield item  # 新加入！
        #print(response.body)  # 运行爬虫程序后打印全部内容
        title = response.xpath("//title/text()").extract()  # 将text()换成text也可以
        print(title)   # 运行爬虫程序后打印title内容
        title = response.xpath('//div[@class="container-1200"]/div[starts-with(@class,"mod-sub")]/h2/text()').extract()
        print(title)   # 运行爬虫程序后打印title内容
        title = response.xpath('//div[@class="js-custom-course mod-sub custom-course-wrap"]/div[@class="container-1200"]/h2/text()').extract()
        print(title) 
        #open('./temp.html','w').write(response.body.decode('utf-8')) #保存
        # pass
