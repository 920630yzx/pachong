# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:36:55 2018

@author: 肖
"""

# -*- coding: utf-8 -*-
# 爬取股票表格数据，并且以股票名为划分分别保存爬取的数据
import scrapy
import time

class Gupiao1Spider(scrapy.Spider):
    name = 'test'
    start_urls = ['http://stock.10jqka.com.cn/']  # 同花顺财经股票栏目
    
    def parse(self, response):       
        a_list = response.xpath("//div[@id='rzrq']/table[@class='m-table']/tbody/tr/td[2]/a")
        # 拼接法进行遍历
        for a in a_list:  
            gp_name = a.xpath("./text()").extract()[0]  # 提取子页面的元素名称,[0]的作用是提取列表元素返回字符串
            url_str = a.xpath("./@href").extract()[0]  # 提取子页面的元素url
            yield scrapy.Request(url_str,
                                     callback=self.download_data,  # 迭代download_data函数
                                     meta={'gp_name':gp_name}) # 这里定义一个字典 
        
    def download_data(self, response): 
        print(response.url)
        print(response.meta['gp_name'])  # 对应于前面yield中meta={'gp_name':gp_name}的定义
        gp_name = response.meta['gp_name']
        time.sleep(1)

        tr_list = response.xpath("//table[@class='m-table']/tbody/tr")    # 爬取子页面的列表
        for tr in tr_list:
            td_list = tr.xpath("./td/text()").extract()  # 获取表中的数据，返回多个列表
            print(td_list)
            with open(gp_name, 'a') as f:
                 f.write('|+|'.join(td_list) + '\n' )
            


