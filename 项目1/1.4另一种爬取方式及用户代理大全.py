# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 20:28:24 2018

@author: 肖
"""
import urllib.request
import requests

# 1.定义请求头：这里用的是谷歌的请求头
headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
} 
url='https://www.baidu.com/'
req = urllib.request.Request(url, headers=headers)  # 2.发送请求：urllib.request.Request()函数 
response = urllib.request.urlopen(req)  # 3.获取响应：urllib.request.urlopen()函数
HTML = response.read().decode("utf-8")
print(HTML)
#换一个请求头试试:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'


'''
import requests
header = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}
response = requests.get(url = 'http://www.baidu.com',headers=header)
print(response.text)
clear
'''



# 案例：爬取糗事百科
"""
Created on Thu May 17 21:39:55 2018
有时候，经常需要将爬虫模拟成浏览器，接下来将为大家介绍具体的实
现。包括：
1、通过Opener添加headers
2、通过Request添加headers
3、批量添加headers

实际场景：
用手机发个说说，用苹果手机、安卓、PC
糗事百科-案例中需要用到伪装,否则会失效
错误信息：
raise RemoteDisconnected("Remote end closed connection without"
RemoteDisconnected: Remote end closed connection without
"""

url='http://www.qiushibaike.com/'
# 用户代理大全https://blog.csdn.net/tao_627/article/details/42297443,可以切换其他的请求头
# 注意可以查看浏览器的Network,User-Agent可以看见谷歌的请求头：
header={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
req=urllib.request.Request(url,headers=header)
data=urllib.request.urlopen(req).read().decode('utf-8','ignore')  # 得到网页
#print(data)


pat='<h2>(.*?)</h2>'  # 得到作者
pat='<div class="content">\n<span>(.*?)</span>'  # 得到说的信息
pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'  # 得到说的信息,与前面一样的
ls=re.compile(pat,re.S).findall(data)  #re.S,表示支持多行正则匹配
for i in ls:
    print(i)
#a={"address":'北京','name':'yq'}   
    
    
    
    
    
    
    
    
    
    