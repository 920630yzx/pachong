# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:28:34 2018
@author: 肖
"""
# coding = utf-8
import requests
from lxml import etree
import time

headers_base ={
'Host': 'www.douyu.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
}

# 1.发送请求，接受响应
response = requests.get("http://www.douyu.com/directory/all", headers=headers_base)
# 将html文本格式化成xpath可以解析的对象
html = etree.HTML(response.text)
table = []
row = []

'''
# 实验：获取首页的第一个主播名
first_name = html.xpath("//ul[@id='live-list-contentbox']/li[1]//span[@class='dy-name ellipsis fl']/text()")
print("first_name = ", first_name)'''

# 循环获取 li 标签
# 设置标志, 0 时表示主播名, 1 时表示在看人数

# 2.又是一个分步连接式爬取方式：
li_list = html.xpath("//ul[@id='live-list-contentbox']/li")
flag = 0

# 两种读取方式均可，第二种更容易理解
# 法1:
for li in li_list:    
    info_list = li.xpath(".//span[@class='dy-name ellipsis fl']/text() \
                          | .//span[@class='dy-num fr']/text()")   # 获得主播名和观看人数
    print(info_list)
    print(type(info_list))  # <class 'list'>

# 法2:
for li in li_list:    
    info_list = li.xpath(".//span[@class='dy-name ellipsis fl']/text() \
                          | .//span[@class='dy-num fr']/text()")   # 获得主播名和观看人数
    # print(info_list)
    # print(type(info_list))  # <class 'list'>
    for i in info_list:
        print(i)
        print(type(i))  # <class 'lxml.etree._ElementUnicodeResult'>
   
# 最终结果: 针对list中还有list的方式
for li in li_list:    
    info_list = li.xpath(".//span[@class='dy-name ellipsis fl']/text() \
                          | .//span[@class='dy-num fr']/text()")   # 获得主播名和观看人数
    for i in info_list:
        if not flag :
            row.append(i)  # row添加
            flag += 1  # 将标志改成 1，下次循环的时候，按人数处理
        else :
            row.append(i)  # # row添加人数信息
            table.append(row)   # 将一行row的信息添加到表中table
            row = []  # 清空row
            flag = 0  # 将标志改成0，下次循环的时候，按主播处理
        
for ii in table:
    print(ii)



# 通过ajax动态爬取数据
# 网页代码有时并非所见即所得，有些代码是通过浏览器运行 js 产生的
# 而requests模块并不是浏览器，它只能获取最初的 html 代码
# max_page_num = html.xpath("//div[@id='J-pager']/a[@class='shark-pager-item'][last()]/text()")
import requests
from lxml import etree
import time

headers_base ={
'Host': 'www.douyu.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
}
# 1.获取并保存一页的数据:
ajax_url = 'http://www.douyu.com/gapi/rkc/directory/0_0/3'  # 由于url没有变化，则这个url就从从抓包工具中获得
response = requests.get(ajax_url, headers=headers_base)
type(response.text)
with open ('douyu.txt','w+',encoding='gbk',errors='ignore') as f:
    f.write(str(response.text))
    
    

# 2.通过ajax爬取5页数据
table = []
row = []    
for page in range(1,6):
    ajax_url = 'http://www.douyu.com/gapi/rkc/directory/0_0/'+str(page)
    print(ajax_url)
    response = requests.get(ajax_url, headers=headers_base)
    html = etree.HTML(response.text)
    time.sleep(3)
    print(response.text)

file = open('douyu.txt','r')        
file = file.read()
import json
file = json.loads(file)
# 然后就可以通过json进行爬取







