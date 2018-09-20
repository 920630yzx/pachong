# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:45:46 2018
@author: 肖
"""
# daileizixun-爬虫

import requests
import re
from lxml import etree
# 目标url
# url = 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI5MDA3NTk1Mw==&scene=124#wechat_redirect'
url = "https://mp.weixin.qq.com/s/EU_GBwqEs3N_h6fYS9ffcA"
url = "https://mp.weixin.qq.com/s/jVPYZuUiEQpq_9eGIPgB1g"
headers = {
    "Cookie": "rewardsn=; wxtokenkey=777; wxuin=822930436; devicetype=Windows10; version=62060426; lang=zh_CN; pass_ticket=WxhYN2P4j1OFSTLHgHnPG8OUyJp86Q0TRpm2oTFL9u9S9mFiAircpUVu10N0Y3SB; wap_sid2=CITYs4gDElxPbXpFbTQtYmR0dGJ2WlRuZThDTHNGSHh3Sng1ZDN3LU0tWDAxQTF5bUJSQlNjbmJybFVxY2pXSmFEZmVpTTd2Mk5zWWVpVmlWYXN5STh4OW84WEktTTBEQUFBfjDp4dzcBTgNQAE=",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.27.400 QQBrowser/9.0.2524.400"
}

content = requests.get(url, headers=headers)
text = content.text
html_tree = etree.HTML(text)  # 调用xpath
text_2 = html_tree.xpath("string(.)")  # xpath("string(.)")这个方法用于直接提取网页的内容,标签内容全部被清除。
text_3 = re.sub('[A-Za-z<>/="":;{}!]()',"",text_2)
text_final = re.compile('股王论剑之代磊看盘(.*?)股市有风险，入市需谨慎，盈亏自负').findall(text_3 )  

with open('./daileikanpan.txt', "w", encoding='gbk',errors='ignore') as f: # 默认模式为‘r’，只读模式
     f.write(text_final[0])




