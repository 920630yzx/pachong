# -*- coding: utf-8 -*-
"""
@author: 肖
"""
'''
http://so.hexun.com/list.do?
http://so.hexun.com/list.do?type=ALL&stype=ARTICLE&key=%B9%C9%C6%C0&page=2
http://so.hexun.com/list.do?type=ALL&stype=ARTICLE&key=%B9%C9%C6%C0&page=3 '''
import urllib.request
import urllib.parse
import requests
import json
res = requests.get("http://so.hexun.com/list.do?")
# print(res)  # 如果返回200则表示请求成功
# 伪装一个请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'} 

# 初始url
url = "http://so.hexun.com/list.do?"
# http://so.hexun.com/list.do?type=ALL&stype=ARTICLE&key=%B9%C9%C6%C0&page=1
# 创建参数（请求体）
data = {
    'type':"ALL",
    'stype':"ARTICLE",
    'key': "股评".encode('gbk'),
    'page':"1"
}

data = urllib.parse.urlencode(data)
url = url + data  # 处理url
req = urllib.request.Request(url=url,headers=headers) 
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8','ignore')
html = res.read()

# 保存这一页面
# with open("hexun.html",'w',encoding='utf-8') as f:
 #    f.write(res.text)

from lxml import etree  # 使用xpath来解析网页
html_tree = etree.HTML(html)
hexun = []
img_list = html_tree.xpath("//table/tr/td[2]/a/@href")
img_list = html_tree.xpath("//table/tr")

for i in img_list:
    author_name = i.xpath("./td[1]/a/text()")  # 作者姓名
    title = i.xpath("./td[2]/a/text()")       # 文章标题
    url_link = i.xpath("./td[2]/a/@href")    # 文章url链接
    datetime = i.xpath("./td[4]/text()")    # 文章发布的日期  
    item = {"author_name":author_name,"title":title,"url_link":url_link,"datetime":datetime}  
    hexun.append(item)

with open("hexun.json",'w',encoding='utf-8') as fp:   # 写入hexun.json
     fp.write(json.dumps(hexun))

html_tree.xpath("//tr/td[2]/a/@href")

'''中文请求体处理方式：
import urllib
dc = {'key': "股评".encode('gbk')}
dc = urllib.parse.urlencode(data)'''

'''get请求'''

# 3.2 requests框架---包含请求体---针对get请求
import requests
# 注意: 若为get请求则为requests.get,如果是post请求则为requests.post
res = requests.get("http://so.hexun.com/list.do?")  # http://www.baidu.com/  使用这个也可以
print(res)   # <Response [200]>
url = "http://so.hexun.com/list.do?" 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

# 创建参数（请求体）
data = {
    'type':"ALL",
    'stype':"ARTICLE",
    'key': "股评".encode('gbk'),
    'page':"1"
}

res = requests.get(url=url,params=data,headers=headers)  # 传入请求头和请求体
html = res.text

from lxml import etree  # 使用xpath来解析网页
html_tree = etree.HTML(html)
img_list = html_tree.xpath("//table/tr[position()>1]/td[1]/a/text()")







