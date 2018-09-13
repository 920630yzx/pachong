# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Test01Pipeline(object):
    
    def open_spider(self,spider):   # 链接mysql
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port = 3306,
            user='root',
            password='920630yzx',
            db='intersting',  # 数据库名
            charset='utf8'
        )
        # 创建一个数据库的游标：游标的作用，把sql语句提交给数据库连接
        self.cur = self.conn.cursor()
        
    def process_item(self, item, spider):
    
        # 第一个值是主键是自增的,所以传入为空值NULL; 第二个值和第三个值需要添加
        sql = "INSERT INTO interst VALUES (NULL,'%s','%s')" %(item['title'],item['img_url'])  # sql语句是关系型数据唯一能够识别编程语言
        self.cur.execute(sql)  # 把sql语句提交给连接
        self.conn.commit()  # 用连接把sql语句提交给mysql服务器去执行
        return item   # 这里的item必须return出去，如果不return这个item就会在这里被销毁，后面如果有另外的管道类要使用，就无法使用了

    def close_spider(self,spider): # 关闭游标和链接
        self.cur.close()  # 关闭游标
        self.conn.close() # 关闭链接
        
        
'''
    def process_item(self, item, spider):
        print('**********')
        print(item)  # 第一次打印
        print('-----------------') 
        return item  # 会打印第二次,同时需注意return必须要写        ''' 
    
    
    
    
    