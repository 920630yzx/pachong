# -*- coding: utf-8 -*-
# http://u148.cn/ ----有意思吧爬取----71课
import scrapy
from test01.items import Test01Item

class U148Spider(scrapy.Spider):
    name = 'u148'  # 爬虫名称,非常重要
    allowed_domains = ['u148.cn']  # 允许访问的域名,当引擎在队列中提取url时,查看这些url是否在这个队列中;如果在则允许访问,如果不在则不允许放入调度器的url队列
    start_urls = ['http://u148.cn/']  # 起始url

    def parse(self, response):
        # print(response)  # 输出网页全部内容
        # print(response.text)  # 输出网页源码(字符串格式)(最重要)
        # print(response.content) # 输出网页源码(二进制格式)
        # print(response.body)    # 输出二进制类型源码
        # print(response.headers)   # 输出响应头
        # print(response.url)  # 输出url
        # f = open("u.html",'w',encoding='utf-8')  # 保存源码,这种保存方式可行
        # f.write(response.text)
        music_list = response.xpath("//article[starts-with(@class,'postgrid')]")
        items =[]
        for music in music_list:       
            item = Test01Item()  # 创建一个item模型,把页面内容放入模型中，extract()[0]可以换为extract_first()
            item['title'] = music.xpath(".//h2/a/text()").extract()[0]  # 得到的应该是一个列表
            item['author'] = music.xpath(".//div/span/a/text()").extract()[0]
            item["img_url"] = music.xpath(".//img/@src").extract()[0]
            item["time"] = music.xpath(".//div/span[2]/text()").extract()[0]
            # print(item['title'])
            # print(item)  # 直接打印
            
            items.append(item)  
        return items  # 这是迭代性的输出方式,每迭代一次则输出一次；此时才能运行 scrapy crawl u148 -o u148.json直接保存之；反之不写这句管道pipelines、items都不能用了
        
            # 注意:下面这种保存方式是不可行的
            # with open("test1.json","w",encoding="uft-8") as f:
            #    f.write(item)
    
            

