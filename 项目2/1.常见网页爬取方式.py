# -*- coding: utf-8 -*-
"""
@author: 肖
"""
# 1.urllib.request.urlopen打开网页
import urllib.request  # urllib是python提供的以用于http请求的基础框架
import urllib.parse

url = "http://www.baidu.com/"
res = urllib.request.urlopen(url=url) # urlopen(url,data),作用根据url对后台发起请求，并且返回响应数据
print(res)    # <http.client.HTTPResponse object at 0x0000028F59C01AC8>
print(res.read().decode('utf-8'))   # read()函数从响应对象中取出响应体

# 2、urlretrieve(url,filename)，把数据从url后台下载下来，然后存储到filename中---这里是下载的图片
img_url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534779995412&di=d52b6f4d8f6ad11997f16a322500d317&imgtype=0&src=http%3A%2F%2Fwww.de99.cn%2Ftu%2F2014%2F010403.jpg"
r = urllib.request.urlretrieve(url=img_url,filename="./bush.jpg")
print(r)


'''2、urlencode()---urllib框架---针对get请求'''
# 2.1:
import urllib.request  
import urllib.parse
# 原url: https://www.baidu.com/s?ie=utf-8&wd=小布什
d = {"ie":"utf-8","wd":"小布什"}  # 把url的参数写成字典的形式
data = urllib.parse.urlencode(d)  # 把字典转化成请求体数据  
print(data)  # ans：ie=utf-8&wd=%E5%B0%8F%E5%B8%83%E4%BB%80
url = "https://www.baidu.com/s?" + data  # 把处理好的参数拼接到后面
res = urllib.request.urlopen(url=url) # urllib框架不识别url字符串中的汉语
print(res.read())

# 2.2:---2.1改进以下
from urllib import request,parse
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
d = {"ie":"utf-8","wd":"小布什"}  # 构造一个请求体字典，对于get请求，请求体拼接到url后面
data = parse.urlencode(d)      # 把字典转化成请求体数据---与上面是完全一样的  
url = "https://www.baidu.com/s?" 
ba_url = url + data   # 把data拼接到url后面，构成完整的get请求的url 
req = request.Request(url=ba_url,headers=headers)  # 创建请求对象---这里添加了请求头
res = request.urlopen(req)
print(res.read())


'''3.反爬处理---伪装请求头'''
# 3.1使用伪装请求头---法1------requests框架：它对urllib的功能做了一个深度的封装与拓展
import requests 
headers_bases = {
'Host': 'www.baidu.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'https://www.baidu.com/',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
}  # 这个摘抄自fiddler，raw（原始中），当然将除了'User-Agent'的删除也可获取，这也说明了'User-Agent'是最重要的

response = requests.get(url = 'http://www.baidu.com/',headers = headers_bases)  # get请求则为requests.get,post请求则为requests.post
print(response)  # 输出网页内容
print(response.text)  # 输出响应体，即网页内容
print(response.content)  # 输出网页内容
print(response.url)  # 输出网页url
print(response.headers)  # 输出网页响应头

# 3.2 requests框架---包含请求体---针对get请求
# 需要爬取的网址---https://www.baidu.com/s?wd=美国
import requests
# 注意: 若为get请求则为requests.get,如果是post请求则为requests.post
res = requests.get("http://www.baidu.com/s?")  # http://www.baidu.com/  使用这个也可以
print(res)   # <Response [200]>
url = "https://www.baidu.com/s" 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

# 创建参数（请求体）
data = {
    'wd':"美国"
}

res = requests.get(url=url,params=data,headers=headers)  # 传入请求头和请求体
print(res.text)     # 获取字符串格式的内容
print(res.content)  # 获取二进制格式的网页内容
print(res.url)      # 获取url
print(res.headers)  # 输出网页响应头
print(type(res.text))  # <class 'str'>
print(type(res.content))  # <class 'bytes'>

# 3.3 使用伪装请求头---法2---urllib框架 
import urllib.request
url = "http://weibo.cn/"
req = urllib.request.Request(url=url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'})
res = urllib.request.urlopen(req)  # 不一样的地方
print(res.read())
with open("wei.html",'w',encoding='utf-8') as fp:
    fp.write(res.read().decode('utf-8'))

# 3.4 使用伪装请求头---法3---add_header追加请求头法（注意这里将冒号改为逗号）：
import urllib.request
url = "http://weibo.cn/"
r = urllib.request.Request(url=url)
r.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
urllib.request.urlopen(r)


'''4.post爬虫---爬取百度字典'''
import urllib.request
import urllib.parse
import json
# 原url：http://fanyi.baidu.com   但这是get的url所以我们不能使用它！
url = "http://fanyi.baidu.com/sug"  # ！！！注意：这个地址也是post地址，并不是url，它在hearders---general的下面获取---（Request URL: http://fanyi.baidu.com/sug）
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

# 在post请求里面，由于请求的参数不能带到url中去，需要构造请求体数据,这个数据在headers--from data下获取
# 原来的 kw: apple   # 下面设置相应体：
data = {
    "kw":"pear"
}

data = urllib.parse.urlencode(data).encode("utf-8")  # 把data转成url参数的形式
req = urllib.request.Request(url=url,headers=headers,data=data)  # 用前面创建好的url、请求体、请求头来创建出请求对象
res = urllib.request.urlopen(req)  # 用请求对象来发起请求
# print(res)  # 这里如果随意打印可能会使请求失败
res_json = json.loads(res.read().decode('utf-8'))
print(res_json)

# 本例的几种数据：
# 1、请求下来的响应对象res，包含了响应头，响应体
# 2、响应体，从res中用read函数读取，取出的是二进制编码的字符串
# 3、utf-8编码的字符串，把真正的字符串从二进制中解码出来







