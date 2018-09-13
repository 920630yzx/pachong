# -*- coding: utf-8 -*-
"""
Created on Tue May 15 22:53:39 2018
根据用户输入的城市，通过网络得到天气和温度
@author: yq
"""
import re
import urllib.request as r

city=input('请输入您要查询的城市名称(英文拼音)')  #和程序可以进行交互,用户输入内容。例如：chengdu,beijing,Tokyo,New York
# print('http:'+city+'.com'),此为拼装方法;这个网址可以查询全球的天气
url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8','ignore')
print(data)

wea=re.compile('"description":"(.*?)",').findall(data)
temp=re.compile('"temp_min":(.*?),').findall(data)
print("天气是：",wea)
print('温度是：',temp)



'''
# 当然还可以循环查询
for i in range(0,1000):
    city=input('请输入您要查询的城市名称(英文拼音)')  #和程序可以进行交互，用户输入内容
    url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
    data=r.urlopen(url).read().decode('utf-8','ignore')
    wea=re.compile('"description":"(.*?)",').findall(data)
    temp=re.compile('"temp_min":(.*?),').findall(data)
    print("天气是：",wea)
    print('温度是：',temp)'''
    
    
    






