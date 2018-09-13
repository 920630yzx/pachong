# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 在setting中需要先打开，并且可以设置它们的优先级，数字越小优先级越高
class Test01Pipeline(object):
    def process_item(self, item, spider):
        return item
    
'''
class WbtcPipeline(object):
    def process_item(self, item, spider):
        pass
        #if item['addr_1'] :  # item['addr_1']为空则返回item
            #return item

class WbtcPipeline_2(object):
    def __init__(self):
        # 新建一个 set 类型集合
        # 这是一种 元素 不重复的集合
        self.item_set = set()  # 新建一个self.item_set用于储存新的数据

    def process_item(self, item, spider):
        # 判断 数据 是否在集合中
        # 如果不在集合中
        if item['des'] not in self.item_set :
            # 将数据 添加到 集合中
            self.item_set.add(item['des'])
            # self.item_set.add(item)
            # 返回 item 数据
            return item'''


