# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:48:11 2018

@author: 肖
"""

# daileizixun

import time
import requests
import json
# https://mp.weixin.qq.com/s?__biz=MzI5MDA3NTk1Mw==&mid=2649365299&idx=1&sn=ca64b2932d86e858bf601f32ea41cf35&chksm=f43bdf6dc34c567b9774bc4bfd3d3ca324d3c3a574a6af6228fe56f2d733b6b86d2c8ff10b95&scene=38&key=ca10956a2f27c479ffa0cb2b10eb7af77019b5111ad9ecd208837040a0e6479a54130e451b2217eb96df8173ebaaea5091b5245693196dc1866a9c7d619739149c3c0a55471616c02547fc4d72d24204&ascene=7&uin=ODIyOTMwNDM2&devicetype=Windows+10&version=62060426&lang=zh_CN&pass_ticket=WxhYN2P4j1OFSTLHgHnPG8OUyJp86Q0TRpm2oTFL9u9S9mFiAircpUVu10N0Y3SB&winzoom=1

# 目标url
url = "https://mp.weixin.qq.com/s/EU_GBwqEs3N_h6fYS9ffcA"
# 添加Cookie避免登陆操作，这里的"User-Agent"最好为手机浏览器的标识
headers = {
    "Cookie": "rewardsn=; wxtokenkey=777; wxuin=822930436; devicetype=Windows10; version=62060426; lang=zh_CN; pass_ticket=WxhYN2P4j1OFSTLHgHnPG8OUyJp86Q0TRpm2oTFL9u9S9mFiAircpUVu10N0Y3SB; wap_sid2=CITYs4gDElxPbXpFbTQtYmR0dGJ2WlRuZThDTHNGSHh3Sng1ZDN3LU0tWDAxQTF5bUJSQlNjbmJybFVxY2pXSmFEZmVpTTd2Mk5zWWVpVmlWYXN5STh4OW84WEktTTBEQUFBfjDp4dzcBTgNQAE=",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.27.400 QQBrowser/9.0.2524.400"
}
'''
# 添加data，`req_id`、`pass_ticket`分别对应文章的信息，从fiddler复制即可。不过貌似影响不大
data = {
    "is_only_read": "1",
    "req_id": yourreq_id,
    "pass_ticket": yourpass_ticket,
    "is_temp_url": "0",
}'''
"""
添加请求参数
__biz对应公众号的信息，唯一
mid、sn、idx分别对应每篇文章的url的信息，需要从url中进行提取
key、appmsg_token从fiddler上复制即可
pass_ticket对应的文章的信息，貌似影响不大，也可以直接从fiddler复制
"""
data = {
    "__biz": 'MzI5MDA3NTk1Mw==',
    "mid": '2649365299',
    "sn": 'ca64b2932d86e858bf601f32ea41cf35',
    "idx": '1',
    "r": '0.8905830557923764',
    "pass_ticket": 'WxhYN2P4j1OFSTLHgHnPG8OUyJp86Q0TRpm2oTFL9u9S9mFiAircpUVu10N0Y3SB',
    "appmsg_type": '9',
}
# 使用post方法进行提交
content = requests.post(url, headers=headers, params=data)
content = requests.get(url, headers=headers, params=data)
# 由于上面这种方法可能会获取数据失败，可以采取字符串拼接这种方法
origin_url = "https://mp.weixin.qq.com/mp/getappmsgext?"
appmsgext_url = origin_url + "__biz={}&mid={}&sn={}&idx={}&appmsg_token={}&x5=1".format(your__biz, article_mid, article_sn, article_idx, yourappmsg_token)
content = requests.post(appmsgext_url, headers=headers, data=data).json()

# 提取其中的阅读数和点赞数
print(content["appmsgstat"]["read_num"], content["appmsgstat"]["like_num"])

a = content.text











