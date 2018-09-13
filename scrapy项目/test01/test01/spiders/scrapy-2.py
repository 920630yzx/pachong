# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 22:04:00 2018

@author: 肖
"""

# -*- coding: utf-8 -*-  
#  爬取多页数据
import scrapy
import json  # 引入模块
import time

class WbtcSpider(scrapy.Spider):  # 新建一个爬虫类，同样继承自scrapy.Spider
    name = 'scrapy-3'  # 定义爬虫名称
    # allowed_domain = ()  # 域名可以不用
    start_urls = ['http://bj.58.com/chuzu/?PGTID=0d200001-0000-1667-c912-e8843d0c8065&ClickID=1']   # 设置 url：
    table = []
    row = {}
    index = 2
    def parse(self, response):  # 定义处理响应函数，函数名必须为parse
        # li_list = response.xpath("//ul[@class='listUl']/li[@logr]/div[@class='des']/h2/a[1]/text()").extract()
        # for li in li_list:
             #print(i)
        li_list = response.xpath("//ul[@class='listUl']/li[@logr]")  # 另一种写法,拼接式写法
        if not li_list :  # 通过判断页面相关元素是否有值，来确定爬虫是否退出(为空则退出)
            print(self.table)  # 如果为空则打印此时的table
            return self.table
        
        for li in li_list:
            print(li.xpath("./div[@class='des']/h2/a[1]/text()").extract()[0].strip())  # 爬取住房概述;会返回一个列表,[0]表示取列表第一个元素,strip()表示去掉去除左右两边的空字符！
            
            #print(li.xpath("./div[@class='des']/p[@class='room']/text()").extract()[0].strip())  # 爬取住房面积;strip()表示去掉去除左右两边的空字符！       
            room_info = li.xpath("./div[@class='des']/p[@class='room']/text()").extract()[0].strip().split(' ')  # 爬取住房面积;不同之处在于修改了打印格式,上面的当然也可
            room_type = room_info[0]
            room_size = room_info[-1].strip()
            print(room_type)
            print(room_size)
            
            print(li.xpath("./div[@class='des']/p[@class='add']/a[1]/text()").extract()[0].strip())  # 爬取地址;strip()表示去掉去除左右两边的空字符！
            
            print(li.xpath("./div[@class='listliright']/div[@class][2]/b/text()").extract()[0].strip())  # 爬取费用;strip()表示去掉去除左右两边的空字符！         
            
            self.row['des'] = li.xpath("./div[@class='des']/h2/a[1]/text()").extract()[0].strip()  # 保存
            self.row['room_type'] = room_type
            self.row['room_size'] = room_size
            self.row['addr'] = li.xpath("./div[@class='des']/p[@class='add']/a[1]/text()").extract()[0].strip()
            self.row['money'] = li.xpath("./div[@class='listliright']/div[@class][2]/b/text()").extract()[0].strip()
            # 将每一行加入表中:
            self.table.append(self.row)
            # 一定要清空行,不然打印table全部为最后一项:(新建一个地址,这里设计到c语言底层)
            self.row = {}

        print("index =========== "+ str(self.index))
        time.sleep(3) 
        url_str = 'http://bj.58.com/chuzu/pn' + str(self.index)
        self.index += 30  # 这样会依次打印1页 ，2页，32页，62页，92页...
        yield scrapy.Request(url_str, callback=self.parse)  # 当然,这里可以将self.parse改为self.parse2以使其迭代下方的parse2
        # 发送请求
        # 注意：1、在 请求函数前使用 yield；这是一个迭代器,有卡住程序等待进行下一步的作用
        #      2、在请求函数中定义一个 callback 函数，这个函数用于请求后的响应信息，会继续调用parse
       
        # 最后执行保存:
        with open('wbtc.json2','w') as f:
            # 注意，要加上参数 ensure_ascii=False，避免中文变成 Unicode格式(ascii码格式)
            f.write(json.dumps(self.table, ensure_ascii=False))
            
    def parse_2(self, response):  # 定义处理响应函数，函数名必须为parse
        print('you choice parse2')
        
      
            
            