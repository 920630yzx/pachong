# -*- coding: utf-8 -*-
"""淘宝裙子:
Created on Wed May 16 23:04:51 2018

加载多页图片  方法：找规律
https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&s=0
https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&s=44
https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&s=88
(page-1)*44
第一页：0
第二页：44
第三页：88
依次获取淘宝网页数据
依次获取每个网页中的图片
"""
import urllib.request as r
import re
for page in range(1,11):
    url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&s='+str((page-1)*44)
    import urllib.request as r
    import re
    #淘宝网页数据
    data=r.urlopen(url).read().decode('utf-8','ignore')
    pat='"pic_url":"(.*?)",'
    ls=re.compile(pat).findall(data)
    print(ls)
    #通过下载图片url
    for i in range(0,len(ls)):
        print('正在加载第'+str(page)+'页第'+str(i)+'张图片')
        r.urlretrieve('http:'+ls[i],'./'+str(page)+'_'+str(i)+'.jpg')




'''淘宝笔记本电脑：
https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&p4ppushleft=5%2C48&s=0
https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&p4ppushleft=5%2C48&s=48
https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&p4ppushleft=5%2C48&s=96
第一页：0
第二页：48
第三页：96
规律：(page-1)*48
'''
import urllib.request as r
import re

for page in range(1,11):
    url='https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&p4ppushleft=5%2C48&s='+str((page-1)*48)
    data=r.urlopen(url).read().decode('utf-8','ignore')   # 读取淘宝网页数据
    pat='"pic_url":"(.*?)",'  # 按照这个方式寻找
    ls=re.compile(pat).findall(data)  # 正则表达式匹配
    print(ls)
    #通过下载图片url
    for i in range(0,3):  # 每页前三张,不然太多；如要全部下载换成len(ls)
        print('正在加载第'+str(page)+'页第'+str(i)+'张图片')  # 下载提示
        r.urlretrieve('http:'+ls[i],'F:\pa/'+str(page)+'_'+str(i)+'.jpg') # 'http:'+ls[i]表示网址



