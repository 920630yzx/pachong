# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:13:37 2018

@author: 肖
项目：火车票爬取   网址：http://www.12306.cn/mormhweb/
# &ajax=true   网址加上&ajax=true可以看到json格式的网站
"""
import re
def huoche_find(s):
  ls = open('火车站编码.txt','r',encoding='utf-8').readlines()
  for i in ls:
      out = re.sub(r"\s{1,}", " ", i) #将多个空格换成一个空格,运用正则表达式
      out = out.split(' ')
      if s == out[1]:
          return out[2]

huoche_find('成都')   

import urllib.request as r
url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
data = '2018-07-16'
from_station = input('请输入出发站：')
from_station = huoche_find(from_station)  
to_station = input('请输入终点站：')
to_station = huoche_find(to_station)
url = url.format(data,from_station,to_station)
data=r.urlopen(url).read().decode('utf-8','ignore') 

import json   # 将str类型转换成字典
data = json.loads(data)  # 将str类型转换成字典

# 正则爬取
A = data['data']['result'][1]
re.compile('(KXY\||XAY\|)(.*?)\|').findall(A)




