# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class Douban01Pipeline(object):
    def process_item(self, item, spider):
        #print('pipelines.py 爬取数据之后 保存')  # 新加入！
        return item
