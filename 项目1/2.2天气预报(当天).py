# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 17:21:39 2018

@author: 肖
"""
# http://api.openweathermap.org/data/2.5/weather?q=yancheng&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996  #当天天气网址
# http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric   # 未来5天天气网址
# 1.当天天气预报
import re
import urllib.request as r
import json   # 可以在https://www.json.cn中查找json解码!!
url = 'http://api.openweathermap.org/data/2.5/weather?q=chengdu&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'  #当天天气网址,q=后面是城市名,这里是成都
data = r.urlopen(url).read().decode('utf-8','ignore')

data = json.loads(data)  # 将str类型转换成dict类型  # 可以在https://www.json.cn中查找编码
today = data['main']['temp']  # 得到当天温度  



# 2.未来5天天气预报
url2 = 'http://api.openweathermap.org/data/2.5/forecast?q=chengdu,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'  #未来5天天气网址,q=后面是城市名
data2 = r.urlopen(url2).read().decode('utf-8','ignore')
data2 = json.loads(data2)  # 将str类型转换成dict类型  # 可以在https://www.json.cn中查找json解码!!
data2['list'][0]['main']['temp']  # 获取当天某天时间的温度
len(data2['list'])



