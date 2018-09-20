# -*- coding: utf-8 -*-
"""
@author: 肖
"""

'''同时爬取多页'''

# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 19:59:19 2018
@author: 肖
"""
'''
http://so.hexun.com/list.do?
http://so.hexun.com/list.do?type=ALL&stype=ARTICLE&key=%B9%C9%C6%C0&page=1
http://so.hexun.com/list.do?type=ALL&stype=ARTICLE&key=%B9%C9%C6%C0&page=2
http://so.hexun.com/list.do?type=ALL&stype=ARTICLE&key=%B9%C9%C6%C0&page=3 '''

import requests
import json
import time
from lxml import etree
res = requests.get("http://so.hexun.com/list.do?")
print(res)  # 如果返回200则表示请求成功
# 伪装一个请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'} 

page_end = input("请输入需要爬取到第几页:")
hexun = []
for page in range(1,int(page_end)+1):
    print('开始爬取第%s页' %(page))
    time.sleep(0.8)  # 线程休息0.8秒
    url = "http://so.hexun.com/list.do?type=ALL&stype=ARTICLE&key=%B9%C9%C6%C0&page="+str(page)
    res = requests.get(url=url,headers=headers)
    html_tree = etree.HTML(res.text)  # 依然使用xpath来解析网页   
    img_list = html_tree.xpath("//table/tr")
    for i in img_list:
        author_name = i.xpath("./td[1]/a/text()")  # 作者姓名
        title = i.xpath("./td[2]/a/text()")       # 文章标题
        url_link = i.xpath("./td[2]/a/@href")    # 文章url链接
        datetime = i.xpath("./td[4]/text()")    # 文章发布的日期  
        item = {"author_name":author_name,"title":title,"url_link":url_link,"datetime":datetime}  
        hexun.append(item)   
        
print('爬虫运行完毕')

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



