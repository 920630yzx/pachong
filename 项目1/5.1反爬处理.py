# -*- coding: utf-8 -*-
"""
常见的反爬虫机制:
1.直接屏蔽程序爬取数据
2.如果访问对方服务器次数过多，对方会屏蔽你的IP地址（可能是10分钟）
@author: 肖
"""
import re   # 导入正则表达式
import urllib.request as r  # 导入urllib
url = 'http://www.qiushibaike.com/'  # 爬取糗事百科,这是网址
news = r.urlopen(url).read().decode('utf-8','ignore')

'''有的网址会报这个错：Remote end closed connection without response;
这说明这个网址有反爬机制,拒绝非浏览器的访问'''


# 解决方法：伪装成网站的请求头,让网站认为是浏览器在登陆,也就是请求头伪装技术;
import re   # 导入正则表达式
import urllib.request as r  # 导入urllib
import requests
url = 'http://www.qiushibaike.com/'  # 爬取糗事百科,这是网址

''' # 另外一个请求头(备用)
headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}
'''
# 这里使用自己的请求头；
headers = {      
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36', 
}

req = r.Request(url, headers=headers)  # 爬取数据
# 打印方式1:r.urlopen(req).read().decode('utf-8','ignore')老方法
data = r.urlopen(req).read().decode('utf-8','ignore')
print(data)

# 打印方式2:requests.get新方法,两种理论上结果完全相同
response = requests.get(url = 'http://www.qiushibaike.com/',headers=headers)
print(response.text)















