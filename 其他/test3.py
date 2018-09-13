# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:36:27 2018

@author: 肖
"""
import re   # 导入正则表达式
import urllib.request as r  # 导入urllib
import requests
from lxml import etree

headers_base = {
'Host': 'www.gandianli.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
}

url='http://zdb.pedaily.cn/company/p2/'
news = r.urlopen(url).read().decode('utf-8','ignore')
html = etree.HTML(news)
text_info = html.xpath("//div[@class='txt']/h3/span/a/text()")
for ele in text_info:
    print(ele)

