# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:48:28 2018
@author: 肖
原网址:http://ac.qq.com/ComicView/index/id/521825/cid/1
，但是该网址拒绝查看源代码，通过观察进一步发现给原网址添加一个view-source:
就可以出现园代码了，即view-source:http://ac.qq.com/ComicView/index/id/521825/cid/1
"""

from selenium.webdriver import PhantomJS,DesiredCapabilities
import time
import re

header = DesiredCapabilities.CHROME.copy()  # DesiredCapabilities可以伪装谷歌浏览器
web = PhantomJS(desired_capabilities=header,executable_path='F:/phantomjs-2.1.1-windows/bin/phantomjs')  # 需要设置PhantomJS的路径，否则无法运行
web.maximize_window()  # 设置浏览器屏幕最大化
web.get('http://ac.qq.com/ComicView/index/id/521825/cid/1')  # 获取网页
web.get_screenshot_as_file('./abc.png')  # 网页截图，可以看到一个网页图片，以png的格式保存到指定位置，名称为abc.png

for page in range(1,30):   # window.scrollTo(0,{})往下翻页
    web.execute_script('window.scrollTo(0,{})'.format(1080*page))  # execute_script表示执行翻页的脚本，1080*1表示第一页，1080*2表示第二页，以此类推。。。
    time.sleep(1)
web.get_screenshot_as_file('./abc.png')  # 下载最后一页


pat = 'https://manhua.qpic.cn/vertical/0/(.*?)"'   # 通过正则获取图片地址
ls = re.compile(pat,re.S).findall(web.page_source)  # web.page_source表示源代码


import urllib.request as r
for i in range(len(ls)):
    r.urlretrieve("http://www.baidu.com", filename="F:\pa/aa.html") 




