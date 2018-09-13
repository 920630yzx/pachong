# -*- coding: utf-8 -*-
import scrapy
import re
import requests
from scrapy.http import Request

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jd.com']
    start_urls = ['http://book.jd.com/']

    def parse(self, response):
        print('正常运行')  # 打印网页全部 print(response.body)
        # 1.获取京东读书目录下的频道列表:
        pat = '"URL":"(\\\\/\\\\/channel.jd.com\\\\/\d{4}.{1}\d{4}.html)"'
        ls = re.compile(pat,re.S).findall(response.body.decode('utf-8','ignore'))  # 匹配'http://book.jd.com/'全部的频道
        # print(ls)
        # print(ls[0])
        # 更改url格式: 如:http://channel.jd.com/1713-3258.html
        ls1 = []
        for i in ls:
            ls1.append('http:'+i.replace('\\',''))  # 统一url格式,如果不统一则网址不能打开,并且可能会出错
        print(ls1)  
        print(len(ls1))
        # 2.获取京东读书-小说频道下的频道列表:
        response = requests.get(ls1[0])  # 链接,进入ls1[0]这个网址
        print(response)   # 返回200则表示正常链接
        pat = 'href="..(list.jd.com/list.html.cat=[0-9,]*)"'    # 匹配另一种格式,进入频道进行匹配;小心问号,这里换成了.来进行匹配
        ls = re.compile(pat,re.S).findall(response.text)  # 有时需要仍需要加上response.text.decode('utf-8','ignore'),有时又不能加,看情况调整格式
        # print(ls)
        # print(len(ls))
        # 更改url格式 如：http://list.jd.com/list.html?cat=1713,3258,3304
        ls2 = []
        for i in ls:
            ls2.append('http://'+i) 
        print(ls2)
        print(len(ls2))
        # 3.获取京东读书-小说-某频道下的内容:(总页数,书名,价格,作者,出版社)
        response = requests.get(ls2[0])  # 链接,进入ls2[0]这个网址
        print(response)  # 返回200则表示正常链接
        pat = '<em>共<b>(.*?)</b>页&nbsp'  
        pagecount = re.compile(pat,re.S).findall(response.text)
        print('总页数是:'+ str(pagecount[0]))  # 获取总页数
        # 4.获取京东读书-小说-某频道下的内容的第二页:(总页数,书名,价格,作者,出版社)
        ls3 = []
        ls3 = ls2[0]+'&page=2'
        print(ls3)
        
        ''' yield Request(ls3,callback=self.parsel)

    def parsel(self,response):
        ls = requests.xpath("//li[@class='gl-item'][3]/div[@class='gl-i-wrap j-sku-item']/div[@class='p-name']").extract()
        print(ls)
        print(len(ls))'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        