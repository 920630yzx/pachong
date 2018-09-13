# -*- coding: utf-8 -*-
# 对gupiao_1进行一些修改，首先进一步增加了爬取多页的功能同时对保存的方式也做了些修改，
import scrapy
import json
import time

class GupiaoSpider(scrapy.Spider):
    name = 'gupiao-2'

    start_urls = ['http://stock.10jqka.com.cn/']

    custom_settings = {
        'ITEM_PIPELINES' : {},
    }

    def parse(self, response):
        a_list = response.xpath("//div[@id='rzrq']/table[@class='m-table']/tbody/tr/td[2]/a")
        for a in a_list:
            gp_name = a.xpath('./text()').extract()[0]   # 提取子页面的元素(股票)名称
            data_link = a.xpath('./@href').extract()[0]  # 提取子页面的元素(股票)url
            
            yield scrapy.Request(data_link,
                                 callback=self.download_data,
                                 meta={'gp_name': gp_name,
                                       'url_base':data_link,
                                       'index':1})

    def download_data(self, response):
        print('url === ' + response.url)

        table = []

        tr_list = response.xpath("//table[@class='m-table']/tbody/tr")   # 爬取该页面的列表
        for tr in tr_list:
            content_list = tr.xpath('./td/text()').extract() # 获取列表内容
            content_list[1] = content_list[1].strip()  # 获取列表中的交易时间，并修改其格式            
            table.append('|,|'.join(content_list))  # 添加进列表table
        # print(content_list[1])
        # print(table)
        time.sleep(1)
        with open('G:/anaconda/spyder 爬虫/scrapy项目/caijing/'
                 + response.meta['gp_name'], 'a') as f:
            f.write('\n'.join(table)+'\n')
            f.close()

        if response.meta['index'] >= 3 :  # 运行次数超过3次时，自动返回
           return

        response.meta['index'] += 1  # 每运行一次response.meta['index']自动加一
        
        url_str = response.meta['url_base'] + 'order/desc/page/' \
                      + str(response.meta['index']) + '/ajax/1/'

        yield scrapy.Request(url_str, callback=self.download_data,
                             meta={'gp_name':response.meta['gp_name'],
                                   'url_base':response.meta['url_base'],
                                   'index': response.meta['index']})

        
        
        
        
        
