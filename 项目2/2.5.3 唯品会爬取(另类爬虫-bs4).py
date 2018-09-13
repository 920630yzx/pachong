# -*- coding: utf-8 -*-
"""
@author: 肖    # 仅一页需要完整下
"""

from selenium import webdriver
from time import sleep
from bs4 import  BeautifulSoup

driver = webdriver.PhantomJS()

url = "http://category.vip.com/suggest.php?keyword=%E8%BF%9E%E8%A1%A3%E8%A3%99&page=3&count=100"

# 用driver打开网页
driver.get(url)
sleep(3)

html = driver.page_source

# print(html)
soup = BeautifulSoup(html,"lxml")
goods_list = soup.select(".goods-inner")  # 拿到goods-inner标签全部内容
print(goods_list)
print(goods_list[0])  # 拿到第一个

goods_items = []
for goods in goods_list:  # 字典式另一种写法---对比2.5.2中的内容
    item = {}
    item["title"] = goods.select(".goods-title-info")[0].get_text()  # get_text()表示获取内容
    item["price"] = goods.select(".price")[0].get_text()  
    goods_items.append(item)

print(goods_items)

goods_items_2 = []    
for goods in goods_list:  # 对比下为何不宜用这种方法
    item = {}
    item["title"] = goods.select(".goods-title-info")
    item["price"] = goods.select(".price")
    goods_items_2.append(item)

print(goods_items_2)


