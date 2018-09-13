# -*- coding: utf-8 -*-
""" 案例1：
@author: 肖   70节-1部分案例
笑话集登陆---get请求---requests框架
"""

import requests  # 【注意】requests这个对象无法保存会话信息，requests中保存会话信息要用Session对象
login_url = "http://www.jokeji.cn/user/c.asp"  # 登录的url
login_url = "http://www.jokeji.cn/User/Login.asp"  # 登录的url
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

# 请求体参数---这里仅需在谷歌浏览器,headers-第四行(query)中即可获取---这个网址的登陆设置的极其不严密这倒是方便了爬虫工程师们！
data = {
    'u': 'bobo666',
    'p':'a12345678',
    'sn': '1',
    't': 'big'
}

# 开始请求
r = requests.get(url=login_url,headers=headers,params=data)  # 直接使用requests.get来请求
print(r.text)     # 返回true则表示登陆成功了
print(r.content)  # 返回true则表示登陆成功了

# 访问主页
info_url = "http://www.jokeji.cn/User/MemberCenter.asp"  # 登陆成功则进一步请求网页
res = requests.get(url=info_url,headers=headers) # 登录成功了，但是这里仍然无法访问主页
print(res.text)  # 登录成功了，但是这里仍然无法访问主页，因为requests在登陆时无法保存cookie信息，导致即使登陆成功也无法进一步获取数据




""" 案例2：用requests.Session()保存登陆信息
@author: 肖   70节-1部分案例
笑话集登陆---get请求---requests框架
上面案例是个访问失败的案例,因为requests无法保存cookie信息,现在对其进行一些修改---添加requests.Session() 进行保存
"""
import requests  # 【注意】requests这个对象无法保存会话信息，requests中保存会话信息要用Session对象
s = requests.Session()  # 所以需要创建一个Session请求对象
login_url = "http://www.jokeji.cn/user/c.asp"  # 登录的url,http://www.jokeji.cn/user/c.asp?也是可以的
# login_url = "http://www.jokeji.cn/User/Login.asp"  # 登录的url,这个也是登陆网址
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

# 请求体参数---这里仅需在谷歌浏览器,headers-第四行(query)中即可获取---这个网址的登陆设置的极其不严密这倒是方便了爬虫工程师们！
data = {
    'u': 'bobo666',
    'p':'a12345678',
    'sn': '1',
    't': 'big'
}

# 开始请求---用上面定义的s进行进一步的请求
r = s.get(url=login_url,headers=headers,params=data)  # 此时请求接口以后都会在s对象中保存下来会话信息
print(r.text)  # 返回true则表示登陆成功了
print(r.content)  # 返回true则表示登陆成功了

# 访问主页
info_url = "http://www.jokeji.cn/User/MemberCenter.asp"  # 登陆成功则进一步请求网页
res = s.get(url=info_url,headers=headers)  # 用保存有会话信息的s对象来请求url
res.encoding = 'gbk'  # 表示解码?
print(res.text)



