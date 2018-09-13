# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor  # 新增的模块
import time

# 通过LinkExtractor方法快速获取url连接及其文字说明，特别是当连接很多时这种方法可以快速获取连接，不过经过实验表明该方法可能会遗漏部分结果！

class Link01Spider(scrapy.Spider):
    name = 'link01'
    start_urls = ['http://www.sina.com.cn/']

    def parse(self, response):
        new_link_list = LinkExtractor(allow=r'news.sina.com').extract_links(response)  # 凡是有连接中有news.sina.com全部获取
        sports_link_list = LinkExtractor(allow=r'sports.sina.com.cn/nba/').extract_links(response)
        i,j= 0,0
        for new_list in new_link_list:
            # print(type(new_link_list))  # 可以看出该类型是一个list
            print(new_list.url)  # 获得url
            print(new_list.text)  # 获得文字描述
            i += 1
        for sports_link in sports_link_list:
            print(sports_link.url)
            print(sports_link.text) 
            j += 1
        print(i)
        print(j)
        
        
        
class IfengSpider(scrapy.Spider):
    name = 'link02'
    start_urls = ['http://www.ifeng.com/']   # 凤凰网

    def parse(self, response):
        new_link_list = LinkExtractor(allow=r'news.ifeng.com/a').extract_links(response)
        tech_link_list = LinkExtractor(allow=r'tech.ifeng.com/a').extract_links(response)
        
        for new_link in new_link_list:
            print(new_link.url)
            print(new_link.text)
            yield scrapy.Request(new_link.url, callback=self.download_data_new)
            
        for tech_link in tech_link_list:
            print(tech_link.url)
            print(tech_link.text)

            yield scrapy.Request(tech_link.url, callback=self.download_data_tech)
     
    # 获取子连接下的文本信息，注意使用了xpath的or功能
    def download_data_new(self, response):
        text = response.xpath("//div[@id='main_content' or @id='yc_con_txt']//text()").extract()
        print(text)
        print('new =========================================')
        time.sleep(1)
        
    # 对上面进行了一些修改，使输出格式更好，同时修改了访问地址与匹配方式  
    def download_data_tech(self, response):
        text = ''.join(response.xpath("//div[@id='main_content' or @id='yc_con_txt']//text()").extract())
        print(text)
        print('tech =========================================')
        time.sleep(1)


        
      
