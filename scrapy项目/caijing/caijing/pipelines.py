# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 再数据过滤条件中写上保存到mysql中
import pymysql

'''
class CaijingPipeline(object):
    def process_item(self, item, spider):
        return item '''  # 原有的

class GpPipeline(object):
    
    def __init__(self):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, db='xiao2',
                               user='root', passwd='920630yzx', charset='utf8')   # 连接mysql
        self.cursor = self.conn.cursor()  # 建立一个游标

    def process_item(self, item, spider):
        sql = "insert into gupiao values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                            item['xuhao'], item['jysj'], item['rz_ye'], item['rz_mre'], item['rz_che'], item['rz_rzjmr'], item['rq_ye'],
                            item['rq_mre'], item['rq_che'], item['rq_rzjmr'], item['rzrqye'])  # 添加到mysql中
        self.cursor.execute(sql) 
        return item

    def close_spider(self, spider):
        self.cursor.execute('commit')
        self.cursor.close()
        self.conn.close()


