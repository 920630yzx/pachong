# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 10:36:37 2018

@author: 肖
"""
import requests
# 方法1:
url='http://music.baidu.com'
r=requests.get(url)
r.encoding='utf-8'
print(r.text)

# 方法2:
url='http://music.baidu.com'
r = requests.get(url)
html=r.content
html_doc=str(html,'utf-8')  # html_doc=html.decode("utf-8","ignore")
print(html_doc)