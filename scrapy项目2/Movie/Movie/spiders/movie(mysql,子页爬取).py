# -*- coding: utf-8 -*-
# 72课---2节
import scrapy
from Movie.items import MovieItem  # 新导入的包

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        movie_list = response.xpath("//table[@class='tbspan']")
        # print(movie_list)
        for movie in movie_list:  # 遍历所有的电影信息，从中提取出我们想要的内容    
            item = MovieItem()  # 创建模型,把页面内容放入模型中---当然这需要先在items中进行设置  
            # 注意 extract_first()=== extract()[0],两者完全相等
            item["title"] = movie.xpath(".//a[@class='ulink']/text()").extract_first()  # 标题,extract()[0]效果与extract_first()相同
            item["info"] = movie.xpath(".//tr[last()]/td/text()").extract_first()  # 内容简介
            # print(item)
                        
            # item的其他内容需要去二级页面中来查找
            # 提取出二级页面的url,由于是相对路径所以需要改为绝对路径
            next_url = "http://www.dytt8.net" + movie.xpath(".//a[@class='ulink']/@href").extract_first()
            # 访问二级页面，需要手动的调取下载器取下载
            yield scrapy.Request(url=next_url,callback=self.parse_next,meta={"movie":item})  # 传入item才能继续使用
            # meta是下载器的一个参数，这个的参数的作用：可以将参数的值在请求结束，返回响应对象的作为响应对象的一个属性绑定过去

    def parse_next(self,response):   # 定义一个回调函数，用于解析二级页面（二级页面每种数据只需要爬取一条数据）
        # print(response)
        item = response.meta["movie"]  # 接收上级页面中绑定在response上的meta属性
        # print(item)  # 查看上面绑定item的效果
        item["img_url"] = response.xpath("//div[@id='Zoom']//img[1]/@src").extract_first()
        item["story"] = response.xpath("//div[@id='Zoom']").xpath("string(.)").extract_first()     # 获取剧情信息
        # xpath("string(.)")是一个函数,表示将所有字符串信息拿出来并拼接成一个大的字符串,标签等内容全部去除！
        item["download_url"] = response.xpath("//td[@bgcolor='#fdfddf']/a/@href").extract_first()  # 获取下载链接
        yield item  # 返回item,返回才可以出结果













