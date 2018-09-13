# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''
class Test01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass'''  # 原有内容

# 下面是定义每一列列名，类似与excel
class WbtcItem(scrapy.Item):  # WbtcItem是一个名字而已
    des = scrapy.Field()
    room_type = scrapy.Field()
    room_size = scrapy.Field()
    addr = scrapy.Field()
    money = scrapy.Field()
    
    
''' 储存至数据库
create table WbtcItem
(   
    des Varchar(N),
    room_type Varchar(N),
    room_size Varchar(N),
    addr_1 Varchar(N),
    addr_2 Varchar(N),
    addr_3 Varchar(N),
    money Varchar(N),
);
'''    

















