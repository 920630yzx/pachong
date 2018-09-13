# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:33:26 2018

@author: 肖  还可以进一步改进---多页爬取,输入法
"""

import urllib.request
import urllib.parse
import json
from selenium import webdriver

url = "http://sou.zhaopin.com/jobs/searchresult.ashx?"
url = 'https://sou.zhaopin.com/?'  # 这个网址也是可以的
# area = input("请输入工作地点：")
# job = input("请求输入岗位名称：")
# start = input("请输入起始页：")
# end = input("请输入终止页：")
d = {
     'jl':'成都',
     'kw':'python',
     'p':1,
     'kt':3
     }
data = urllib.parse.urlencode(d)
url = url + data  # 处理url

driver = webdriver.PhantomJS('F:/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get(url)

res = driver.page_source
driver.quit()  # 关闭
req = urllib.request.urlopen(res)
# html = req.read().decode('utf-8')

from lxml import etree
html_tree = etree.HTML(res)
# img_list = html_tree.xpath("//div[@class='itemBox nameBox']/div[@class='commpanyName']/a/text()")
# img_list = html_tree.xpath("//div[@class='itemBox nameBox']/div[@class='jobName']/a/span/@title")
jobItems = []
img_list = html_tree.xpath("//div[@class='itemBox nameBox']")
for a in img_list:
    com_name = a.xpath("./div[@class='commpanyName']/a/text()")
    job_name = a.xpath("./div[@class='jobName']/a/span/@title")
    item = {"job_name":job_name,"company":com_name}   
    jobItems.append(item)
           
with open("zhilian.json",'w',encoding='utf-8') as fp:
     fp.write(json.dumps(jobItems))
     
''' json.dumps()用于将dict类型的数据转成str，    
json.loads()用于将str类型的数据转成dict'''    

# 读取
with open("zhilian.json",'r') as f:
     print(type(f))  # <class '_io.TextIOWrapper'>  也就是文本IO类型
     result=json.load(f)
     
     
     
     
     
     
     
     
     
     