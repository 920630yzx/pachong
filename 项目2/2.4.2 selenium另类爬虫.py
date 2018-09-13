# -*- coding: utf-8 -*-
"""
@author: 肖
"""

from selenium import webdriver
from time import sleep

drvier = webdriver.PhantomJS('F:/phantomjs-2.1.1-windows/bin/phantomjs')

url = "https://www.zhihu.com/search?type=content&q=%E6%B8%85%E5%8D%8E"

drvier.get(url)
sleep(3)  # 需要线程休眠

drvier.save_screenshot("zhihu1.png")  # 网页截屏

# 上拉加载1000距离
js = "document.body.scrollTop=1000"
drvier.execute_script(js)

sleep(3)
drvier.save_screenshot("zhihu2.png") # 网页重新截屏

drvier.quit()  # 关闭


