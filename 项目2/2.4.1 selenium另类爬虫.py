# -*- coding: utf-8 -*-
"""
@author: 肖
"""

from selenium import webdriver
from time import sleep

# 创建chrome浏览器的驱动
driver = webdriver.Chrome('F:/phantomjs-2.1.1-windows/chromedriver.exe')

# 用driver打开百度
driver.get("http://www.baidu.com/")

# 点击设置按钮
driver.find_elements_by_link_text("设置")[0].click()
sleep(2)

# 让百度去搜索一个关键字
driver.find_element_by_id('kw').send_keys("赵丽颖")

# 获取到selenium加载网页以后的那些源码
print(driver.page_source)
driver.quit()


