# -*- coding: utf-8 -*-
"""
用户   存在header里面
本机IP: 125.70.166.23    (在百度里直接搜索'查看本机IP'即可以找到)
"""
import random
#用户代理池
uas=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
     'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)']
#其他谷歌代理请求头
#    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
#    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'

#ip代理池
"""在百度上搜索'ip代理地址大全'可以找到很多,不过能不能用有待验证;同时可以在讯代理上购买ip地址,这样比免费的效果会更好.
113.200.214.164	9999	陕西西安
125.46.0.62	53281	河南济源
114.250.25.19	80	北京
123.161.16.20	9797	河南安阳
114.215.95.188	3128	北京
"""
ips=['113.200.214.164:9999',
     '125.46.0.62	53281',
     '114.250.25.19:80',
     '123.161.16.20:9797',
     '114.215.95.188:3128']


import urllib.request as r
url='http://weixin.sogou.com/'
header={'user-agent':random.choice(uas)}  #从用户代理池随机加载一个请求头

#定义Proxy代理
def ipproxy(ips):
    ip=random.choice(ips)  #从ip代理池随机加载一个ip地址
    print('IP地址',ip)
    proxy=r.ProxyHandler({'http':ip})
    opener=r.build_opener(proxy,r.HTTPHandler)
    r.install_opener(opener)
    return ip

ipproxy(ips)  #设置ip代理上网
req=r.Request(url,header)
data=r.urlopen(url).read()
len(data)

# 循环使用
for i in range(0,10):
    currentip=ipproxy(ips)  #设置ip代理上网
    req=r.Request(url,header)
    data=r.urlopen(url).read()
    if len(data)>200:
        print("....")
    else:
        ips.remove(currentip)
        print('ip代理有问题.'+currentip)
        currentip=ipproxy(ips)#设置ip代理上网
        continue
    
##############既然我们这么强大,有无限的ip资源和用户代理
#######用什么方式拦截？让你登陆。。。验证码。。人工操作
######找到合适的IP地址和请求头








