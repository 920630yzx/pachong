# -*- coding: utf-8 -*-
"""
Created on Thu May 10 22:26:03 2018
目标-百度
任务-
下载百度互联网网页内容
数据筛选(正则表达式)
保存
"""
'''1.爬取网页'''
import re   # 导入正则表达式
import urllib.request as r  # 导入urllib
url='http://www.baidu.com'
url='http://m.baidu.com/'
url='https://www.qiushibaike.com/'
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=python&rsv_spt=1&oq=python&rsv_pq=b7565cd30000c303&rsv_t=de8eSbwm22IzOJtsCbp1bpi%2BmwJNEzPREKTZvjo8%2F1R3fRMbR1LKdyO4bRy7M4CLryog&rqlang=cn&rsv_enter=0&rsv_sug3=1&rsv_sug1=1&rsv_sug7=100&rsv_sug4=910'
ans=r.urlopen(url).read().decode('utf-8','ignore')
re.compile('{"title":"(.*?)",',re.S).findall(ans)
print(ans)

'''2.下载并保存网页源码'''
r.urlretrieve(url,filename="G:/aa.html") # 保存至"G:/aa.html"中，"G:/aa.html"也即是html文件路径
r.urlcleanup()  # 清除缓存

'''3.另一种爬取方式'''
# 3.1如果不用请求头:
import urllib.request
import requests
response = requests.get('http://www.baidu.com')
print(response)  # 输出网页内容
print(response.text)  # 输出网页内容
print(response.url)  # 输出网页url
print(response.headers)  # 输出网页url

# 3.2使用伪装请求头
headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}
# 这里有两种方式
# 方式1：requests.get方法
response = requests.get(url = 'http://www.baidu.com',headers=headers)
A = response.text
print(A)
# 方式2:r.urlopen(req).read().decode('utf-8','ignore')老方法
url = 'https://www.baidu.com'
req = urllib.request.Request(url, headers=headers)
data = r.urlopen(req).read().decode('utf-8','ignore')
print(data)

# 3.3.1使用伪装请求头---法1---requests.get方法：
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

response = requests.get(url = 'http://www.baidu.com/',headers = headers_bases)
print(response)  # 输出网页内容
print(response.text)  # 输出响应体，即网页内容
print(response.content)  # 输出网页内容
print(response.url)  # 输出网页url
print(response.headers)  # 输出网页响应头

# 3.3.2 requests框架它对urllib的功能做了一个深度的封装与拓展
import requests
res = requests.get("http://www.baidu.com/")
print(res)   # <Response [200]>
url = "https://www.baidu.com/s"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

# 创建参数
data = {
    'wd':"美国"
}

res = requests.get(url=url,params=data,headers=headers)
print(res.text)     # 获取字符串格式的内容
print(res.url)      # 获取url
print(res.content)  # 输出网页内容
print(res.headers)  # 输出网页响应头

# 3.3.3 使用伪装请求头---法2---urllib.request.Request法
import urllib.request
url = "http://weibo.cn/"
req = urllib.request.Request(url=url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'})
res = urllib.request.urlopen(req)  # 不一样的地方
print(res.read())
with open("wei.html",'w',encoding='utf-8') as fp:
    fp.write(res.read().decode('utf-8'))

# 3.3.4使用伪装请求头---法3---add_header追加请求头法（注意这里将冒号改为逗号）：
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


'''5 urlencode()爬取---拼接'''
import urllib.request
import urllib.parse
# 原url: https://www.baidu.com/s?ie=utf-8&wd=小布什
d = {"ie":"utf-8","wd":"小布什"}  # 把url的参数写成字典的形式
data = urllib.parse.urlencode(d)  # 把字典处理成url参数的形式
print(data)  # ans：ie=utf-8&wd=%E5%B0%8F%E5%B8%83%E4%BB%80
url = "https://www.baidu.com/s?" + data  # 把处理好的参数拼接到后面
res = urllib.request.urlopen(url=url) # urllib框架不识别url字符串中的汉语
print(res.read())


