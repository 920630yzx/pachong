# -*- coding: utf-8 -*-
"""
@author: 肖
"""
'''案例1：---cookie---通过谷歌浏览器即可获取'''
import urllib.request
url = "https://weibo.cn/6370062528/info?vt="

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    'Cookie':'SCF=Ahz9Jk7TyV7zzLvwoCxFjRRTbASUHA9Jp8RcRyRaht68K11D0lYQBg5j9No1B157Zgv7Lx5COUC7DNdjo8APyKc.; _T_WM=ae4d1af9302c562727db8db7ad8ef936; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W59rVpGeZ7yg7I7HR0hyYPg5JpX5KzhUgL.Foq0S057Sozfeon2dJLoI05LxKML1heLB-BLxKqL1heL1h-LxKML1-2L1hBLxKqLBoeLBKzLxKqLBoeLBKz41K.t; SUB=_2A252f8UDDeRhGeBN7FIR9izJyTSIHXVVg-tLrDV6PUJbkdANLVb7kW1NRFYvPyP4QibZHUFsFOFulm58dcuZWvfS; SUHB=08JL-Xfu0zeDJT'
}

req = urllib.request.Request(url=url,headers=headers)
res = urllib.request.urlopen(req)
with open("weibo.html","wb") as fp:
    fp.write(res.read())



'''案例2:---cookie---通过谷歌浏览器即可获取'''
import urllib.request

url = "https://weibo.com/u/6463150286/home?wvr=5"  # !这个网址为什么就不行?可能是cookie获取不全和不正确,request请求无法保存cookie等等原因,此时就只有采取登陆的方式了---参见案例3
url = "https://weibo.cn/6463150286/info?vt="
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    'Cookie':'SCF=AtXOtjhRgr1WBRPZvwJHZMQ5TK5n5ryP0TiF4_xf9x79M1zHe5nbA-YiLXFrjHREHu_f22FOb2GdZx1lfUrx0w0.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFVmH3jd4zWn6dk-YjWUXMp5JpX5K-hUgL.FoqXSoepSK5E1hq2dJLoIpRLxK-L12qLBoqLxK-LBo5L12qLxK-L1-BL129JdG.t; _T_WM=159e2ab94d0cf712b57fa50c45a5bae6; SUB=_2A252W6k1DeRhGeBK7VEQ9S7OwzqIHXVVpzd9rDV6PUJbkdANLW_BkW1NR7VmmXYCCcLYGMbOsp9kSRnB8xJ57Jvh; SUHB=0102MwQ1bbpObk'
}

req = urllib.request.Request(url=url,headers=headers)
res = urllib.request.urlopen(req)
with open("weibo.html","wb") as fp:
    fp.write(res.read())
    
    
    
'''案例3:---cookie的另外一套完整的登陆机制---通过fidder获取数据---针对于需要更深层次的伪装'''  
import urllib.request
import urllib.parse
from http import cookiejar  # 由于Request对象无法保存会话信息，我们需要用cookiejar机制来处理有会话信息的请求
# 微博登陆网址:https://passport.weibo.cn/signin/login
cookie = cookiejar.CookieJar()  # 1.创建一个cookiejar对象，用于保存页面上的cookie信息
handler = urllib.request.HTTPCookieProcessor(cookie)  # 2.创建一个handler，用于携带cookiejar
opener = urllib.request.build_opener(handler)   # 3.创建一个opener，用于发起请求

login_url = "https://passport.weibo.cn/sso/login"  # ！！在fiddler中直接复制url然后进行粘贴更好，这是原网址

# 请求头的信息不够完整的话，仍可能报错，这里补充完整请求头的信息，使其伪装的更好！
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    'Referer': 'https://passport.weibo.cn/signin/login?',
    'Origin': 'https://passport.weibo.cn',
    'Connection': 'keep-alive',
    'Host': 'passport.weibo.cn'
}

# 构造请求体（表单内容--直接复制即可）---这同样是通过抓包工具获取的
data = {
    'username':	'18161280526',
    'password':'920630650408',
    'savestate':'1',
    'r':'https://weibo.cn/',
    'ec':'1',
    'pagerefer':'https://login.sina.com.cn/sso/login.php?url=https%3A%2F%2Fpassport.weibo.cn%2Fsignin%2Flogin%3F&_rand=1535188656.8657&gateway=1&service=wapsso&entry=wapsso&useticket=1&returntype=META&sudaref=&_client_version=0.6.24',
    'entry':'mweibo',
    'wentry	':'',
    'loginfrom':'',
    'client_id':'',
    'code':'',
    'qq':'',
    'mainpageflag':'1',
    'hff':'',
    'hfp':''
}

data = urllib.parse.urlencode(data).encode('utf-8')  # 处理成url参数
req = urllib.request.Request(url=login_url,headers=headers,data=data)  # 发起一个post请求，注意Request对象无法保存会话信息
res = opener.open(req)  # res = urllib.request.urlopen(req) [参见1中2.2]，这个请求无法携带cookie
print(res.read().decode('utf-8'))  # 检验登陆是否成功，不报错就说明登陆成功了

# 登录成功了，现在访问个人资料---进行第二次网址的访问
url = "https://weibo.cn/6463150286/info?vt="   # 个人原网址 
req = urllib.request.Request(url=url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'})
# res = urllib.request.urlopen(req)  # 这个框架没法携带cookie，因此不能使用这个框架

res = opener.open(req)

with open("info.html",'wb') as fp:
    fp.write(res.read())











   
    
    
   
    
    
    
    
    
    