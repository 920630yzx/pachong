# -*- coding: utf-8 -*-
"""
Created on Thu May 17 21:22:23 2018

数学家：
勾股定理
鲁迅：
中国历史是什么？ 看到 ‘吃人’
学会编程：
10万行代码=一个程序
5000行代码=会写代码
拿来主义：
拷贝

@author: yq
"""

import urllib.request as r
import re
for page in range(1,3):
    print('第{%s}页' %page)

    url='http://www.baidu.com/s?wd={}&pn={}'
    url=url.format('python',(page-1)*10)
    data=r.urlopen(url).read().decode('utf-8','ignore')
    ls=re.compile('data-tools=.*?{"title":"(.*?)",').findall(data)  # 原正则表达式:'{"title":"(.*?)",'
    #print(ls)
    for i in ls:
        print(i)

    
'''ans:
第{1}页
Welcome to Python.org
Python教程 - 廖雪峰的官方网站
Python 基础教程 | 菜鸟教程
Download Python | Python.org
Python 简介 | 菜鸟教程
PythonTab:Python中文开发者社区门户
Python中国
Python - 伯乐在线
Python开源软件 - 开源中国社区
第{2}页
玩蛇网 - Python教程学习与Python资源分享平台
Python3 教程 | 菜鸟教程
Python Releases for Windows | Python.org 
Download Python | Python.org
python基础教程_python高级教程_python手册_python实例 - 红黑联盟
Python(计算机程序设计语言)_百度百科
Python - 开源中国社区
python教程_python基础教程_python视频教程-慕课网 
python视频教程_python中文学习视频_python基础教程-极客学院
Python快速教程 - Vamei - 博客园
需要注意的是该方法有失败的可能,百度可不是那么好爬的'''   


    
