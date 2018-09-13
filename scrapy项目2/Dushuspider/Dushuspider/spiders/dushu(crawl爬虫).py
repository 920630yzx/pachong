# -*- coding: utf-8 -*-   Crawl爬虫--72课--2节
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Dushuspider.items import DushuspiderItem
# Crawl爬虫是spider的一个派生类，spider的设立理念只让爬虫从start_urls队列中去获取url
# CrawlSpider定义了一些规则，可以用于提供跟踪链接的方法，可以跟踪一堆的url

class DushuSpider(CrawlSpider):
    name = 'dushu'
    allowed_domains = ['dushu.com']
    start_urls = ['http://www.dushu.com/book/1077.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1077_\d\.html'), callback='parse_item', follow=True),
    )
    # \.表示转义成.   只有.也是可以的
    # rules规则：包含许多的Rule对象，Rule对象有三个参数，第一个参数是有个链接匹配对象（通过该对象，可以匹配出一堆的url）
    # 匹配规则可以用正则(用allow表示)、xpath（restrict_xpath表示）或者bs4（restrict_css表示）
    # 参数二、callback回调函数，通过Rule匹配出url以后就会对这些url逐一的进行请求，并且把请求的结果放到对应的回调函数中来处理
    
    def parse_item(self, response):
        # print(response)  # 获取全部的url
        book_list = response.xpath("//div[@class='book-info']")   # 在每个url中直接获取需要的内容,对比下basic爬虫是一样的
        for book in book_list: 
            item = DushuspiderItem()  # 调用DushuspiderItem()
            item["title"] = book.xpath(".//h3/a/text()").extract_first()
            item["author"] = book.xpath(".//p/text()").extract_first()
            item["info"] = book.xpath(".//p[2]/text()").extract_first()
            item["cover"] = book.xpath(".//img/@src").extract_first()
            # yield item
            
            # 提取二级页面的链接,由于是相对链接所以需要拼接：
            next_url = "http://www.dushu.com" + book.xpath(".//h3/a/@href").extract_first()
            yield scrapy.Request(url=next_url,callback=self.parse_next,meta={"shu":item})   # 传入item

    def parse_next(self, response):   # 爬取二级目录,而且刚好只需爬取二级目录的一项内容,如果需要爬取二级目录的多项内容又如何？（分开写）
        item = response.meta["shu"]  # 接受item       
        item['price'] = response.xpath("//p[@class='price']/span/text()").extract_first()   # 定价        
        item["author_info"] = response.xpath("//div[@class='text txtsummary']/text()").extract()[2]   # 作者简介
        yield item  # 返回item















