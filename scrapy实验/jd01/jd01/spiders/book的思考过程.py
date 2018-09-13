# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:01:21 2018

@author: 肖
"""

import re
pat = '"URL":"\\\\/\\\\/channel.jd.com.*?.html"'    # 匹配第一种格式
pat = '"URL":"\\\\/\\\\/channel.jd.com.{2}\d{4}.{1}\d{4}.html"'   # 严密匹配
pat = '"URL":"\\\\/\\\\/channel.jd.com\\\\/\d{4}.{1}\d{4}.html"'   # 这种匹配方式更为严密 
pat = '"URL":"(\\\\/\\\\/channel.jd.com\\\\/\d{4}.{1}\d{4}.html)"'   # 这种匹配方式更为严密 
ls = re.compile(pat,re.S).findall('"URL":"\/\/channel.jd.com\/1713-3267.html"')



pat = 'href="..(list.jd.com/list.html.cat=[0-9,]*)"'   # 匹配另一种格式,这里使用了原子表需注意下
ds = re.compile(pat,re.S).findall('href="//list.jd.com/list.html?cat=1713,3258,3304"')



pat = '<em>共<b>(.*?)</b>页&nbsp' 
ds = re.compile(pat,re.S).findall('<em>共<b>242</b>页&nbsp;&nbsp')
ds = ds[0]

# https://blog.csdn.net/zuochao_2013/article/details/77801261