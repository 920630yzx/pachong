# -*- coding: utf-8 -*-
"""
@author: 肖
chinaunix登陆---采用requests框架爬取---70节3部分案例
登陆账号:MrFan666    密码:f12345678
登陆地址:http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes
登陆成功后网址:http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lenn4
可以发现 loginhash和formhash需要动态获取
"""

import requests
from bs4 import BeautifulSoup
# proxy = {"https":"218.60.8.83:3129"}  # 设置代理

# 创建一个Session对象
s = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

login_page = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes'  # 登陆地址
res = s.get(login_page,headers=headers)
# res = s.get(login_page,headers=headers,proxies=proxy)  # 设置代理
soup = BeautifulSoup(res.text,'lxml')  # 用bs4读取页面源码

# 分析反爬：提交网址动态  formhash表单动态
login_params = soup.select("form.cl")[0].attrs.get("action")  # 获取动态的表单提交地址参数loginhash  # form.cl是组合选择器,当然用[name=login]也可以
formhash = soup.select("[name=formhash]")[0].attrs.get("value")  # 获取动态生成一个formhash, input[name=formhash]也可以 
# 页面源码： <input type="hidden" name="formhash" value="850cc022">

# post的url
post_url = "http://bbs.chinaunix.net" + login_params  # 登陆成功后网址
print(post_url)

# 构建post参数(表单数据---根据抓包工具获取)
data = {
    'formhash':	formhash,
    'loginsubmit':'true',
    'password':'f12345678',
    'referer':	'http://bbs.chinaunix.net/',
    'return_type':'',
    'username':	'MrFan666'
}
print(data)

r = s.post(url=post_url,headers=headers,data=data)  # 发起post请求登录
print(r.text)



