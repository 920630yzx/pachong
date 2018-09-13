# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:10:53 2018

@author: 肖
"""
# scrapy crawl test-2  
# 仍然是爬取一页数据，但这里更改了保存的方式，该方式更亲民，更简单。
import scrapy

class Scrapy1Spider(scrapy.Spider):  # 继承scrapy.Spider
    name = 'test'  # 定义爬虫名称
    allowed_domains = ['kexuejisuan.com']
    start_urls = ['http://www.kexuejisuan.com']  # 初始url；默认情况下，scrapy会以get的方式发送start_urls中的 url

    def parse(self, response):  # 定义处理响应函数，函数名必须为parse
        print(response.text)
        #pass
    
    
class WbtcSpider(scrapy.Spider):  # 新建一个爬虫类，同样继承自scrapy.Spider
    name = 'test-2'  # 定义爬虫名称
    # allowed_domain = ()  # 域名可以不用
    start_urls = ['http://bj.58.com/chuzu/?PGTID=0d200001-0000-1667-c912-e8843d0c8065&ClickID=1']   # 设置 url：
    table = []
    row = {}
    def parse(self, response):  # 定义处理响应函数，函数名必须为parse
        # print(response.xpath("//ul[@class='listUl']/li[@logr]/div[@class='des']/h2/a[1]/text()").extract())  # 此方法会得到一个较大的列表
   
        # li_list = response.xpath("//ul[@class='listUl']/li[@logr]/div[@class='des']/h2/a[1]/text()").extract()   # 循环打印这个列表,得到很多小字符串
        # for li in li_list:
             #print(i)
        li_list = response.xpath("//ul[@class='listUl']/li[@logr]")  # 另一种写法,拼接式写法
        for li in li_list:
            print(li.xpath("./div[@class='des']/h2/a[1]/text()").extract()[0].strip())  # 爬取住房概述;会返回一个列表,[0]表示取列表第一个元素,strip()表示去掉去除左右两边的空字符！
            
            print(li.xpath("./div[@class='des']/p[@class='room']/text()").extract()[0].strip())  # 爬取住房面积;strip()表示去掉去除左右两边的空字符！       
            room_info = li.xpath("./div[@class='des']/p[@class='room']/text()").extract()[0].strip().split(' ')  # 爬取住房面积;不同之处在于修改了打印格式,上面的当然也可
            room_type = room_info[0]
            room_size = room_info[-1].strip()
            print(room_type)
            print(room_size)
            
            print(li.xpath("./div[@class='des']/p[@class='add']/a[1]/text()").extract()[0].strip())  # 爬取地址;strip()表示去掉去除左右两边的空字符！
            
            print(li.xpath("./div[@class='listliright']/div[@class][2]/b/text()").extract()[0].strip())  # 爬取费用;strip()表示去掉去除左右两边的空字符！         
            
            self.row['des'] = li.xpath("./div[@class='des']/h2/a[1]/text()").extract()[0].strip()  # 保存
            self.row['room_type'] = room_type
            self.row['room_size'] = room_size
            self.row['addr'] = li.xpath("./div[@class='des']/p[@class='add']/a[1]/text()").extract()[0].strip()
            self.row['money'] = li.xpath("./div[@class='listliright']/div[@class][2]/b/text()").extract()[0].strip()
            # 将每一行加入表中:
            self.table.append(self.row)
            # 一定要清空行,不然打印table全部为最后一项:(新建一个地址,这里设计到c语言底层)
            self.row = {}
        # print(self.table)    
        # 将数据保存成 json文件 :   
        with open('G:/abc.txt', "w", encoding='gbk',errors='ignore') as f: # 默认模式为‘r’，只读模式
             f.write(str(self.table))
            
            
            
            
            