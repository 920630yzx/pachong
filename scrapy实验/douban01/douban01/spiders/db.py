# -*- coding: utf-8 -*-
import scrapy
#from douban01.items import Douban01Item  # 新加入！

class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.douban.com/']

    def parse(self, response):
        print('sxac')
        captcha = response.xpath("//img[@id='captcha_image']/@src").extract()  # 使用xpath拿到验证码图片
        open('./temp.html','w').write(response.body.decode('utf-8'))
        print(captcha)
        params = {
        'source': 'None',
        'redir': 'https://www.douban.com/people/181509571/',
        'form_email': '18161280526',
        'form_password': password,
        'captcha-solution': captcha,
        'captcha-id': 'ILAghXm2A0InmxIk3f48woFS:en',
        'login': '登录'}
        print(str(params))
        
