# -*- coding: utf-8 -*-
"""
@author: 肖
"""

# 保存至mysql中

import scrapy
import json
import time
from caijing.items import GupiaoItem

class GupiaoSpiderMysql(scrapy.Spider):
    name = 'gpmysql'

    start_urls = ['http://stock.10jqka.com.cn/']   # 该网站是同花顺财经

    custom_settings = {
        'ITEM_PIPELINES' : {'caijing.pipelines.GpPipeline': 200},  # 再定义一次'ITEM_PIPELINES'
    }

    def parse(self, response):
        a_list = response.xpath("//div[@id='rzrq']/table[@class='m-table']/tbody/tr/td[2]/a")
        for a in a_list:
            gp_name = a.xpath('./text()').extract()[0]   
            data_link = a.xpath('./@href').extract()[0]  # 获取子页面url连接

            yield scrapy.Request(data_link,
                                 callback=self.download_data,
                                 meta={'gp_name': gp_name,
                                       'url_base':data_link,
                                       'index':1})

    def download_data(self, response):
        print('url === ' + response.url)

        gp_item = GupiaoItem()  # 实例化
        tr_list = response.xpath("//table[@class='m-table']/tbody/tr")
        for tr in tr_list:
            content_list = tr.xpath('./td/text()').extract()   # 爬取详细数据
            content_list[1] = content_list[1].strip()   # 获取列表中的交易时间，并修改其格式 

            gp_item['xuhao'] = content_list[0]   # content_list[0]是字符串
            gp_item['jysj'] = content_list[1]
            gp_item['rz_ye'] = content_list[2]
            gp_item['rz_mre'] = content_list[3]
            gp_item['rz_che'] = content_list[4]
            gp_item['rz_rzjmr'] = content_list[5]
            gp_item['rq_ye'] = content_list[6]
            gp_item['rq_mre'] = content_list[7]
            gp_item['rq_che'] = content_list[8]
            gp_item['rq_rzjmr'] = content_list[9]
            gp_item['rzrqye'] = content_list[10]

            # print(gp_item)
            yield gp_item
            
        if response.meta['index'] >= 1 :   # 运行次数超过1次时，自动返回   (也就是只爬取子页面1页)
            return

        response.meta['index'] += 1   # 每运行一次response.meta['index']自动加一
           
        url_str = response.meta['url_base'] + 'order/desc/page/' \
                      + str(response.meta['index']) + '/ajax/1/'
                      
        yield scrapy.Request(url_str, callback=self.download_data,
                             meta={'gp_name':response.meta['gp_name'],
                                   'url_base':response.meta['url_base'],
                                   'index': response.meta['index']})



# GupiaoSpiderMysql上进一步修改

class GupiaoSpiderMysql_2(scrapy.Spider):
    name = 'gpmysql_2'

    start_urls = ['http://stock.10jqka.com.cn/']

    def str2num(self, string):
        num = 0
        try:
            num = eval(string)
        except:
            dw = string[-1:]
            if dw == '万':
                # num = round(eval(string[:-1]) * 10000.0, 3)
                num = eval(string[:-1]) * 10000.0
            elif dw == '亿':
                # num = round(eval(string[:-1]) * 100000000.0, 3)
                num = eval(string[:-1]) * 100000000.0
            else:
                print('Someting error !!!!!!!!!!!!!!!!')
        return num

    def parse(self, response):
        a_list = response.xpath("//div[@id='rzrq']/table[@class='m-table']/tbody/tr/td[2]/a")
        for a in a_list:
            gp_name = a.xpath('./text()').extract()[0]
            data_link = a.xpath('./@href').extract()[0]

            yield scrapy.Request(data_link,
                                 callback=self.download_data,
                                 meta={'gp_name': gp_name,
                                       'url_base':data_link,
                                       'index':1})

    def download_data(self, response):
        print('url === ' + response.url)

        gp_item = GupiaoItem()
        tr_list = response.xpath("//table[@class='m-table']/tbody/tr")
        for tr in tr_list:
            content_list = tr.xpath('./td/text()').extract()
            content_list[1] = content_list[1].strip()

            gp_item['xuhao'] = content_list[0]   # content_list[0]是字符串
            gp_item['jysj'] = content_list[1]
            gp_item['rz_ye'] = self.str2num(content_list[2])
            gp_item['rz_mre'] = self.str2num(content_list[3])
            gp_item['rz_che'] = self.str2num(content_list[4])
            gp_item['rz_rzjmr'] = self.str2num(content_list[5])
            gp_item['rq_ye'] = self.str2num(content_list[6])
            gp_item['rq_mre'] = self.str2num(content_list[7])
            gp_item['rq_che'] = self.str2num(content_list[8])
            gp_item['rq_rzjmr'] = self.str2num(content_list[9])
            gp_item['rzrqye'] = self.str2num(content_list[10])

            # print(gp_item)
            yield gp_item

        '''
        # print('\n'.join(table))
        # print('================================')

        time.sleep(1)
        with open('/root/PycharmProjects/myspider/files/'
                          + response.meta['gp_name'], 'a') as f:
            f.write('\n'.join(table)+'\n')
            f.close()
        '''

        if response.meta['index'] >= 1 :
            return

        response.meta['index'] += 1

        url_str = response.meta['url_base'] + 'order/desc/page/' \
                  + str(response.meta['index']) + '/ajax/1/'

        yield scrapy.Request(url_str, callback=self.download_data,
                             meta={'gp_name':response.meta['gp_name'],
                                   'url_base':response.meta['url_base'],
                                   'index': response.meta['index']})


            