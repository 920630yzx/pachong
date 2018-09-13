# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class MoviePipeline(object):
#     def process_item(self, item, spider):
#         return item    # 原来的  
    
    
import pymysql

class MoviePipeline(object):

    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='920630yzx',
            db='xiao',
            charset='utf8'
        )
        self.cur = self.conn.cursor()  # 通过链接创建游标

    def process_item(self, item, spider):
        sql = "INSERT INTO movie VALUES(NULL,'%s','%s','%s','%s','%s') " % (item["title"],item['info'],item['img_url'],item['story'],item['download_url'])       
        self.cur.execute(sql)  # 用游标执行      
        self.conn.commit()  # 用链接提交
        return item

    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()
        
        
'''
注意需要在mysql中设置列表名称,id作为主键需要设置成自动自增的类型'''        
        
        
        
        
        
        