# -*- coding: utf-8 -*-
import scrapy
import json
import time


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    # start_urls = ['https://weibo.cn/pub']   # 这个不用写！

    headers_base = {     # Raw(原始)中的信息:
        'Host': 'passport.weibo.cn',
        'Connection': 'keep-alive',
      # 'Content-Length': '184',    # 注意：将 Content-Length 去掉，否则会报错
        'Origin': 'https://passport.weibo.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }
    
    headers_2 = {   # 子页面('https://m.weibo.cn/api/container/getIndex?containerid=2304131642634100_-_WEIBO_SECOND_PROFILE_WEIBO') Raw(原始)中的信息:
        'Host': 'm.weibo.cn',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }
    
    login_info = {     # WebForms(表单)中的信息:
        'username': '18161280526',   # 用户名
        'password': '920630650408',  # 登陆密码
        'savestate': '1',
        'r': 'http://weibo.cn/',
        'ec': '0',
        'pagerefer': '',
        'entry': 'mweibo',
        'wentry': '',
        'loginfrom': '',
        'client_id': '',
        'code': '',
        'qq': '',
        'mainpageflag': '1',
        'hff': '',
        'hfp': '',
    }
      
# 登陆微博：
    def start_requests(self):        # 使用 start_requests 函数替代 start_urls 列表 
        yield scrapy.FormRequest(    # 使用FormRequest 函数，请求方式为post
            url='https://passport.weibo.cn/sso/login',  # 请求url，在上方的 Raw(原始)中第一行POST中获取（最后的HTTP/1.1不要）           
            formdata=self.login_info,   # 表单数据     
            headers=self.headers_base,  # 请求头        
            callback=self.parse,        # 响应处理函数
        )
      
    def parse(self, response):  # 获得登陆成功信息
        print(response.text)   # 查看登陆是否成功，如果成功则进入下面的网址
        yield scrapy.Request('https://m.weibo.cn/api/container/getIndex?containerid=2304131642634100_-_WEIBO_SECOND_PROFILE_WEIBO',
                             headers=self.headers_2,
                             callback=self.download_json,
                            )

        
     # 获取子页面数据：
    def download_json(self, response):
        # print(response.text)  # 这里返回的是一个超大型的json数据
        jsonobj = json.loads(response.text)
        print(type(jsonobj))  # jsonobj是一个字典
        # print(jsonobj)  # 超简单的一个保存方式！
        # filexiao = open("G:/abc.txt", "w")
        # filexiao.write(str(jsonobj))
        # filexiao.close()
        cards_list = jsonobj['data']['cards']
        print(type(cards_list))  # cards_list是一个字典
        for i in range(1,len(cards_list)):
            print(type(cards_list[i]['mblog']['text']))



