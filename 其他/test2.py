# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:11:55 2018

@author: 肖
"""

import re   # 导入正则表达式
import requests

headers_base = {
'Host': 'www.gandianli.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
}

response = requests.get("http://www.360doc.com/content/17/0607/05/12097684_660819619.shtml",headers=headers_base)
ans = re.compile('</P>\n<P>\u3000\u3000(.*?)</P>',re.S).findall(response.text)

for i in range(len(ans)):
    with open('G:/abcde.txt', "a+", encoding='gbk',errors='ignore') as f: # 默认模式为‘r’，只读模式
         f.write(ans[i])

for i in range(len(ans)):
    with open('G:/abcde.doc', "a+", encoding='gbk',errors='ignore') as f: # 默认模式为‘r’，只读模式
         f.write(ans[i])

     
     
     
     