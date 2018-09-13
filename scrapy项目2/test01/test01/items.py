# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Test01Item(scrapy.Item):
    # 这个类本质是一个字典对象，主要作用：用于对接需求，需求分析阶段需要我们爬取那些数据，一般情况下我们会在这个模型进行定义
    # 然后以这个模型为基础进行爬取   
    title = scrapy.Field()  # 音乐的标题   
    img_url = scrapy.Field()  # 图片的url
    author = scrapy.Field()   # 作者
    time = scrapy.Field()     # 时间
    pass
