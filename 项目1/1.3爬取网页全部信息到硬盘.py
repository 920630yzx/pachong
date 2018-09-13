# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 16:03:26 2018

@author: 肖
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 17 20:51:09 2018

我们可以使用Urllib模块快速地爬取某一个网页，接下来将具体介绍：

1、https与http协议
2、urlopen与urlretrieve以及Request
3、网页状态码
"""
import urllib.request as r
# 方式1:爬取到硬盘中(标准写法)（较慢）：
f=r.urlopen('http://www.baidu.com')  # 向指定的url地址发起请求,并返回服务器响应的数据（文件对象）
#f=r.urlopen('http://www.baidu.com').read().decode('utf-8','ignore')  # 直接读取文件的全部内容,粗暴的方法！

# 查看网页状态码
f.getcode()  #打开网页的状态。网页可以访问
if f.getcode()==200:    # f.getcode()=200则网页读取正常,详细情况可以查看网页状态码
    data=f.read().decode('utf-8','ignore')  # 读取网页全部内容
#下载硬盘中
r.urlretrieve('http://www.baidu.com',"./baidu.html") # urlretrieve表示下载,保存为html格式 
r.urlretrieve('http://www.baidu.com',"F:\pa/baidu.txt")  # 原路径:  ./baidu.txt,这里保存为txt格式



# 爬到内存中--方式2：
req=r.Request('http://www.baidu.com')  #放入用户名和密码
f=r.urlopen(req)
f.getcode()



# 爬到硬盘中--方式3：
r.urlretrieve("http://www.baidu.com", filename="F:\pa/aa.html")  # "http://www.baidu.com"访问地址; 保存至"G:/aa.html"中，"G:/aa.html"也即是html文件路径
# urlretrieve   该方法在执行的过程中会产生缓存   因此需要清除,以防内存占满
r.urlcleanup()  # 清除缓存

# 爬到硬盘中--方式3--下载的图片
import urllib.request
img_url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534779995412&di=d52b6f4d8f6ad11997f16a322500d317&imgtype=0&src=http%3A%2F%2Fwww.de99.cn%2Ftu%2F2014%2F010403.jpg"
r = urllib.request.urlretrieve(url=img_url,filename="./bush.jpg")
print(r)






# 文件读取：
filename = open("F:\pa/baidu.txt", 'r',encoding='UTF-8')   # 对应于第31行！
ans1 = filename.read()  # 读取全部内容
ans2 = filename.readlines() # 读取每一行,得到一个列表


with open("F:\pa/baidu.txt",'r',encoding='UTF-8') as data:  # "F:\pa/baidu.txt"为地址
    msg=data.readlines()  # 读取每一行,得到一个列表
    msg=str(msg)  # 将一个列表转成str形式
    print(msg)

with open("F:\pa/baidu.txt",'r',encoding='UTF-8') as data:
    msg1=data.read()  # 读取每一行,得到一个列表
    msg1=str(msg)  # 将一个列表转成str形式
    print(msg1)

with open("F:\pa/baidu1.txt",'r',encoding='UTF-8') as data:
    msg1=data.readlines()  # 读取每一行,得到一个列表
    msg1=str(msg)  # 将一个列表转成str形式
    print(msg1)


filename=open('all_school.txt','r',encoding='utf-8')  # 读取当前目录下文件
filename=open('F:/pa/all_school.txt', 'r',encoding='utf-8')
f=filename.readlines()
filename.close()


