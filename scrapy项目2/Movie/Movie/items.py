# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 内容简介
    info = scrapy.Field()
    # 海报链接
    img_url = scrapy.Field()
    # 剧情介绍
    story = scrapy.Field()
    # 下载链接
    download_url = scrapy.Field()
