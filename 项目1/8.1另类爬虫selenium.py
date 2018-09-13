# -*- coding: utf-8 -*-
"""
另类爬虫selenium  @author: 肖   
"""
# 首先进行安装 执行： pip install -U selenium  /  pip install selenium
# test1：
from selenium.webdriver import PhantomJS
import re
web = PhantomJS(executable_path='F:/phantomjs-2.1.1-windows/bin/phantomjs')  # 需要设置PhantomJS的路径，否则无法运行

web.get('http://www.baidu.com')  # 获取网页
print(web.page_source)  # 打印网页源代码
print(web.page_source[0:300])  # 打印网页部分源代码，前面300个元素
web.get_screenshot_as_file('./baidu.png')  # 网页截图，可以看到一个网页图片，以png的格式保存到指定位置，名称为baidu.png

# test2：
element = web.find_element_by_xpath('//*[@id="kw"]')   # 通过xpath方式进行获取，定位百度的输入栏
element.send_keys('python')  # 输入关键字
element = web.find_element_by_xpath('//*[@id="su"]')  # 定位百度的百度一下按钮，定位方式都是通过右键copy xpath即可，不是以往的xpath定位
element.click()   # 促发按钮点击事件
web.get_screenshot_as_file('./baidusearch.png')  # 网页截图，可以看到一个网页图片，以png的格式保存到指定位置，名称为baidusearch.png

print(element)  # 打印此时的element
print(web.page_source)  # 打印源代码
re.compile('<title>(.*?)</title>').findall(web.page_source)  # 正则匹配而已



