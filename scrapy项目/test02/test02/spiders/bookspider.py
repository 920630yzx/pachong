[# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time


class BookspiderSpider(CrawlSpider):
    name = 'bookspider'
  # allowed_domains = ['baidu.com']   # 同样可以不写
    start_urls = ['http://www.quanwenyuedu.io/']   # 小说网站总页面
    
    book_link = LinkExtractor(allow=r'quanwenyuedu.io$', deny='big5')  # allow=r'quanwenyuedu.io$'表示url中以这个结尾的选中；deny='big5',表示url中只要有'big5'就拒绝；
    text_link = LinkExtractor(allow=r'/(\d+).html$')   # 正则表达式 

  # 生成Rule对象，callback的函数为字符串；当follow=True，爬虫会自动向下挖取url，再向url发送请求！ 
    rules = (       
        Rule(book_link, callback='get_book', follow=True),  # 如果满足book_link，则调用callback中的函数 
        Rule(text_link, callback='get_text', follow=True),
    )
   
    def get_book(self, response):
        print('get_book ===== ', response.url)
        time.sleep(1)
    
    def get_text(self, response):
        print('get_text =====', response.url)



        time.sleep(1)
       
        


