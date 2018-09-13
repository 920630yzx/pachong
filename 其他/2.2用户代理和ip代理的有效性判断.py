# -*- coding: utf-8 -*-
"""
Created on Tue May 22 22:09:25 2018

@author: yq
"""

import random
#ip代理池
ips=['113.200.214.164:9999',
     '125.46.0.62:53281',
     '114.250.25.19:80',
     '123.161.16.20:9797',
     '114.215.95.188:3128']
import urllib.request as r
def ipproxy(ips):
    ip=random.choice(ips)
    print('IP地址',ip)
    proxy=r.ProxyHandler({'http':ip})
    opener=r.build_opener(proxy,r.HTTPHandler)
    r.install_opener(opener)
    return ip
url='http://weixin.sogou.com/'
header={'user-agent':random.choice(uas)}

for i in range(0,100):
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
    
