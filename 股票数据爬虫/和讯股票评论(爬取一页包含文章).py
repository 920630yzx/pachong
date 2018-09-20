# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 21:08:17 2018
@author: 肖
"""

'''
http://so.hexun.com/list.do?
http://so.hexun.com/list.do?type=ALL&stype=ARTICLE&key=%B9%C9%C6%C0&page=1
http://so.hexun.com/list.do?type=ALL&stype=ARTICLE&key=%B9%C9%C6%C0&page=2
http://so.hexun.com/list.do?type=ALL&stype=ARTICLE&key=%B9%C9%C6%C0&page=3 '''

import requests
import json
res = requests.get("http://caidao.hexun.com/4157532/article108001.html")
print(res)  # 如果返回200则表示请求成功
# 伪装一个请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'} 

# 初始url
url = "http://so.hexun.com/list.do?type=ALL&stype=ARTICLE&key=%B9%C9%C6%C0&page=1"

res = requests.get(url=url,headers=headers)
print(res.text) 

# 保存这一页面
with open("hexun.html",'w',encoding='utf-8') as f:
    f.write(res.text)

from lxml import etree
# 使用xpath来解析网页
html_tree = etree.HTML(res.text)
hexun = []
img_list = html_tree.xpath("//table/tr[position()>1]")
for i in img_list:
    author_name = i.xpath("./td[1]/a/text()")  # 作者姓名
    title = i.xpath("./td[2]/a/text()")       # 文章标题
    url_link = i.xpath("./td[2]/a/@href")    # 文章url链接
    datetime = i.xpath("./td[4]/text()")    # 文章发布的日期  
    item = {"author_name":author_name,"title":title,"url_link":url_link,"datetime":datetime}  
    hexun.append(item)

# 调整url的内容
url_new = []
import re
for i in range(0,len(hexun)):
    url = hexun[i]['url_link'] 
    a = re.compile('.com/(.*?)/article').findall(url[0])
    b = re.compile('article(.*?).html').findall(url[0])
    url = 'http://apicaidao.hexun.com/article/info/'+a[0]+'/'+b[0]
    url_new.append(url)

# 爬取并匹配文章
article = []
for j in range(0,len(hexun)):
    url = url_new[j]
    res = requests.get(url=url,headers=headers)
    text = json.loads(res.text)
    text_2 = text['data']['articleContent']
    text_3 = re.sub("[A-Za-z<>/\n]","",text_2)  # 用正则进行匹配替换！！！
    item = {"article":text_3}
    article.append(item)

# 保存为json格式：
# json.dumps()用于将dict类型的数据转成str  
with open("hexun.json",'w',encoding='utf-8') as fp:   # 写入hexun.json
     fp.write(json.dumps(hexun))

# 读取json格式：
# json.loads()用于将str类型的数据转成dict 
with open("hexun.json",'r') as f:
     print(type(f))  # <class '_io.TextIOWrapper'>  也就是文本IO类型
     result=json.load(f)

# 保存为txt格式:
# txt格式可以直接查看
with open("hexun.txt",'w',encoding='utf-8') as fp:   # 写入hexun.json
     fp.write(str(hexun))

# 保存article为txt格式
with open("article.txt",'w',encoding='utf-8') as fp:   # 写入hexun.json
     fp.write(str(article))
 
