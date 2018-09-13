# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 21:03:57 2018

@author: 肖
"""
import urllib.request as r
import re
import json
url = 'http://api.openweathermap.org/data/2.5/forecast?q=chengdu,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'  #未来5天天气网址,q=后面是城市名
data = r.urlopen(url).read().decode('utf-8','ignore')
data = json.loads(data)  # 将str类型转换成dict类型  # 可以在https://www.json.cn中查找json解码!!
for i in range(0,len(data['list'])):
    str1 = '的温度是：{}'  
    str2 = '的天气是：{}'
    if i == 0:
       A = data['list'][i]['dt_txt']
       print(data['list'][i]['dt_txt']+str1.format(data['list'][i]['main']['temp']))
       print(data['list'][i]['dt_txt']+str2.format(data['list'][i]['weather'][0]['description']))
    elif i == 7:
       print(data['list'][i]['dt_txt']+str1.format(data['list'][i]['main']['temp']))
       print(data['list'][i]['dt_txt']+str2.format(data['list'][i]['weather'][0]['description']))
    elif i == 15:
       print(data['list'][i]['dt_txt']+str1.format(data['list'][i]['main']['temp']))
       print(data['list'][i]['dt_txt']+str2.format(data['list'][i]['weather'][0]['description']))
    elif i == 23:
       print(data['list'][i]['dt_txt']+str1.format(data['list'][i]['main']['temp']))
       print(data['list'][i]['dt_txt']+str2.format(data['list'][i]['weather'][0]['description']))
    elif i == 31:
       print(data['list'][i]['dt_txt']+str1.format(data['list'][i]['main']['temp']))
       print(data['list'][i]['dt_txt']+str2.format(data['list'][i]['weather'][0]['description']))
    elif i == 31:
       print(data['list'][i]['dt_txt']+str1.format(data['list'][i]['main']['temp']))
       print(data['list'][i]['dt_txt']+str2.format(data['list'][i]['weather'][0]['description']))

