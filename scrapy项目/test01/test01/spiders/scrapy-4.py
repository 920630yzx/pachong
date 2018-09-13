# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 19:51:52 2018

@author: 肖
"""
# scrapy crawl scrapy-item -o table.xml
# 运行scrapy crawl scrapy-item -o table.json和scrapy crawl scrapy-item -o table.csv保存数据

# -*- coding: utf-8 -*-  设置items自动调整数据格式,换一种打印数据的方式;同时可以打开pipelines和settings下的pipelines看看又有什么变化
import scrapy
import json  # 引入模块
import time
from test01.items import WbtcItem  # 引入模块

class WbtcSpider(scrapy.Spider):  # 新建一个爬虫类，同样继承自scrapy.Spider
    name = 'scrapy-item'  # 定义爬虫名称
    
    # 局部项设置    通过局部项设置可以把默认的设置重新定义，使之与默认的设置隔离
    custom_settings = {
            'ITEM_PIPELINES' : {}  # 这里表示将setting中的 'ITEM_PIPELINES'项弃用(当然这里本身就没有打开,这一行也没有作用)
            }
    
    start_urls = ['http://bj.58.com/chuzu/?PGTID=0d200001-0000-1667-c912-e8843d0c8065&ClickID=1']   # 设置 url：
    wbtc_item = WbtcItem()  # 引入WbtcItem()类(该类在items中定义)
    def parse(self, response):  # 定义处理响应函数，函数名必须为parse
        
        li_list = response.xpath("//ul[@class='listUl']/li[@logr]")  # 另一种写法,拼接式写法
        
        for li in li_list:            
            #print(li.xpath("./div[@class='des']/p[@class='room']/text()").extract()[0].strip())  # 爬取住房面积;strip()表示去掉去除左右两边的空字符！       
            room_info = li.xpath("./div[@class='des']/p[@class='room']/text()").extract()[0].strip().split(' ')  # 爬取住房面积;不同之处在于修改了打印格式,上面的当然也可
            room_type = room_info[0]
            room_size = room_info[-1].strip()

            # 与item进行对比下
            self.wbtc_item['des'] = li.xpath("./div[@class='des']/h2/a[1]/text()").extract()[0].strip()  # 保存
            self.wbtc_item['room_type'] = room_type 
            self.wbtc_item['room_size'] = room_size
            self.wbtc_item['addr'] = li.xpath("./div[@class='des']/p[@class='add']/a[1]/text()").extract()[0]  # 有些stipe()可以去掉;strip()表示去掉去除左右两边的空字符！     
            self.wbtc_item['money'] = li.xpath("./div[@class='listliright']/div[@class][2]/b/text()").extract()[0].strip()
            #print(self.wbtc_item)  # 这个也行,但会导致运行scrapy crawl scrapy-item -o table.csv和scrapy crawl scrapy-item -o table.json失败
            yield self.wbtc_item  # 这种储存方式是否更好,自行体会
                    
            # 这种方式得到的结果与scrapy-2中得到的结果有些不同，但是大同小异，思想上是完全一致的
            
        '''两个yield并不会冲突,也支持同时爬取多页的形式
        return self.table
        print("index =========== "+ str(self.index))
        time.sleep(3)

        url_str = 'http://bj.58.com/chuzu/pn' + str(self.index)
        self.index += 20
        yield scrapy.Request(url_str, callback=self.parse)
        # 发送请求
        # 注意：1、在 请求函数前使用 yield；
        #      2、在请求函数中定义一个 callback 函数，这个函数用于除了请求后的响应信息
        '''
            
            