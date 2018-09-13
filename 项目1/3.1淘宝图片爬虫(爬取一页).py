# -*- coding: utf-8 -*-
"""
Created on Wed May 16 22:29:31 2018
第三章：淘宝商品图片抓取
步骤：
1.分析人工查看淘宝商品图片
2.获取商品图片地址并保存
3.人工翻页查看下一页图片
4.查看网页的变化用python抓取多页图片
@author: yq
"""
url='https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91'  # 这里设计url自动转码的问题,此为淘宝中的笔记本电脑
import urllib.request as r
import re

data=r.urlopen(url).read().decode('utf-8','ignore')  # 读取淘宝网页数据
pat='"pic_url":"(.*?)",'  # 按照这个方式寻找
ls=re.compile(pat).findall(data)
print(ls)

#通过下载图片url
for i in range(0,len(ls)):
    r.urlretrieve('http:'+ls[i],'./'+str(i)+'.jpg')  # urlretrieve即下载,'http:'+ls[i]是下载的地址
# './'+str(i)+'.jpg'是路径;逗号后面是下载到哪里,特别'./'表示是在当前路径下进行下载,可以更换
    
    
    
for i in range(0,6):
    #取回=下载到本地,注意下载需要加上http:才行,不然下载会失败
    r.urlretrieve('http:'+ls[i],'F:\pa/'+str(i)+'.jpg')  # F:\pa保存到F:\pa中去



