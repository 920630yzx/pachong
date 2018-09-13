# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 17:40:48 2018

@author: 肖
"""

import re   # 导入正则表达式
import urllib.request as r  # 导入urllib
url='http://news.baidu.com/'
news = r.urlopen(url).read().decode('utf-8','ignore')
print(news)

# 正则匹配
re.compile('top&pn=2">(.*?)</a>',re.S).findall(news)


# 当然下面是标准写法：
news2 = r.urlopen('http://news.baidu.com/')
if news2.getcode()==200:
    data = news2.read().decode('utf-8','ignore')
    print(data)
else:
    print('无法爬取此网站内容')

# 保存到txt文件
filexiao = open("G:/abc.txt", "w")
filexiao.write(data)
filexiao.close()

# 如果对象不是str，就要先转换一下；超简单的一个保存方式
jsonobj = {'a':1,'b':2,'c':3}
filexiao = open("G:/abc.txt", "w")
filexiao.write(str(jsonobj))
filexiao.close()

# 法2：
with open('G:/abcde.txt', "w", encoding='gbk',errors='ignore') as f: # 默认模式为‘r’，只读模式
     f.write(data)



