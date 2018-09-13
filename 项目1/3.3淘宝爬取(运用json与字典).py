# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 21:12:31 2018

@author: 肖
"""
import urllib.request as r
import json   # 将str类型转换成字典
url = 'https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
data = r.urlopen(url).read().decode('utf-8','ignore')  # 读取淘宝网页数据
data = json.loads(data)  # 将str类型转换成字典

# &ajax=true   网址加上&ajax=true可以看到json格式的网站
# https://www.json.cn/    这个网站可以看到json的编码

for i in range(len(data['mods']['grid']['data']['spus'])):
    k=data['mods']['grid']['data']['spus']
    if k[i]["cmt_count"] == 0:
       print(k[i]['title']+' '+k[i]['importantKey']+' 价格:'+k[i]['price']+' 运费:'+str(k[1]["cmt_count"]).replace('0','免运费')) 
    if k[i]["cmt_count"] != 0:
       print(k[i]['title']+' '+k[i]['importantKey']+' 价格:'+k[i]['price']+' 运费:'+tr(k[i]["cmt_count"]).replace('0','有运费')) 
'''
data['mods']['grid']['data']['spus'][1]['title']  # 商品名称
data['mods']['grid']['data']['spus'][1]['importantKey']  # 商品信息
data['mods']['grid']['data']['spus'][1]['price']  # 商品价格
data['mods']['grid']['data']['spus'][1]["cmt_count"]  # 商品运费
'''


# txt文件读取json的方式：
filename = open("G:/abcd.txt", 'r',encoding='UTF-8')   # 对应于第31行！
ans1 = filename.read()  # 读取全部内容
if ans1.startswith(u'\ufeff'):
   ans1 = ans1.encode('utf8')[3:].decode('utf8')
ans2 = json.loads(ans1)

