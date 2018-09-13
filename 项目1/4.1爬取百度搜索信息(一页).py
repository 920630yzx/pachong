# -*- coding: utf-8 -*-
"""
Created on Thu May 17 21:06:08 2018

• 目标网址：http://www.baidu.com
• 需求：自动搜索某个关键词内容,并自动翻页:这里再百度中搜索python
第一页
https://www.baidu.com/s?wd=python&pn=0  
参数：
wd=python   搜索的内容word
第二页
https://www.baidu.com/s?wd=python&pn=10
第三页
https://www.baidu.com/s?wd=python&pn=20

参数规律：
(page-1)*10     0,10,20,30...
网页内容有：{"title":"Python (programming language) - Wikipedia",
{"title":"(.*?)",

"""
import urllib.request as r
import re
url='http://www.baidu.com/s?wd={}&pn={}'
url=url.format('python',(1-1)*10)  # url.format是个拼接函数,{}是依次的拼接内容,非常重要!!!
data=r.urlopen(url).read().decode('utf-8','ignore')
# data2=r.urlopen('http://www.baidu.com/s?wd=python&pn=0').read().decode('utf-8','ignore')
ls=re.compile('data-tools=.*?{"title":"(.*?)",').findall(data)  # .*也可,不必使用.*?
print(ls)

# https网页访问不了,可以改为http













