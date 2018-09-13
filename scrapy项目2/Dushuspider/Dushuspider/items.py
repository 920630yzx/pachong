# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DushuspiderItem(scrapy.Item):
   
    title = scrapy.Field()   # title
    
    author = scrapy.Field()  # 作者
    
    info = scrapy.Field()    # 简介
     
    cover = scrapy.Field()   # 封面
    
    price = scrapy.Field()   # 定价
    
    author_info = scrapy.Field()  # 作者介绍
