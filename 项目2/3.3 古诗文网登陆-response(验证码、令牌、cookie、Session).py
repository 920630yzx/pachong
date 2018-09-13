# -*- coding: utf-8 -*-
"""
@author: 肖
爬取古诗文网: 采用requests框架爬取---70节2部分案例
网址主页：https://www.gushiwen.org/
登陆页：https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx
登陆成功后网址: https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx   (动态页码,这里需要通过网页检查或者抓包工具获取)"""

# 分析反爬,用抓包工具抓取网页,表单有：  
# 用户名和密码   token令牌两个(__VIEWSTATE,在hidden下面)   验证码
import requests
from bs4 import BeautifulSoup

# 登录页接口:
post_page =  "https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx?type=d"   # 均是登录页
post_page =  "https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx"  # 均是登录页
# 访问登录页
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

# 创建一个Session对象,单独的requests无法保留cookie、令牌、验证码信息,所以需要创建一个Session对象
s = requests.Session()
res = s.get(post_page,headers=headers)

# 获取token信息(这个网站有两个token)---这个可以先通过抓包工具的表单中获取,之后可以再在检查下获取查看对比
soup = BeautifulSoup(res.text,'lxml')   # 转换成bs4读取
a = soup.select("#__VIEWSTATE")[0].attrs.get("value")  #  #表示使用id选择器进行选择,attrs.get("value")表示获取"value"下的属性值
b = soup.select("#__VIEWSTATEGENERATOR")[0].attrs.get("value")
print(a,b)

# 获取验证码信息,注意这里的验证码地址只是一个相对路径,所以需要加上一个绝对路径
code_url = "https://so.gushiwen.org" + soup.select("#imgCode")[0].attrs.get("src")  # attrs.get("src")表示获取属性为"src"的值
# 把验证码图片下载到本地,这里仍然必须用Session来下载,因为requests是无法保存cookie、令牌、验证码等信息的
img = s.get(code_url)  # 获取验证码
with open("yanzhengma.png",'wb') as fp:  # 下载并保存
    fp.write(img.content)
# 验证码的识别:  1.用AI框架(不过较难)  2.人工输入
code = input("请输入验证码：")

# post登录接口---(登陆成功后网页)
login_url = "https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx%3ftype%3dd"

# 登录参数(抓包工具表单数据)
data = {
    '__VIEWSTATE':a,
    '__VIEWSTATEGENERATOR':b,
    'from':	'http://so.gushiwen.org/user/collect.aspx?type=d',
    'email':'fanjianbo666@163.com',
    'pwd':'123456',
    'code':	code,
    'denglu':'登录'
}

# 发起post请求登录
r = s.post(url=login_url,headers=headers,data=data)
print(r.text)  # 看看是否登陆成功



