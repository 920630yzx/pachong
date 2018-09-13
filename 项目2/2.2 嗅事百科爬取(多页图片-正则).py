# -*- coding: utf-8 -*-
"""
@author: 肖
"""
import urllib.request
import re

url = "https://www.qiushibaike.com/pic/page/"

# 定义函数用于处理url
def handle_url(url,page):
    page_url = url + str(page)
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    req = urllib.request.Request(url=page_url,headers=headers)
    return req

# 定义一个函数，处理每一个页面的请求
def request_pages(req):
    res = urllib.request.urlopen(req)
    # 解析出图片的url
    pat = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt=.*?>.*?</div>',re.S)
    img_list = pat.findall(res.read().decode('utf-8'))  # 分开写的正则表达式
    return img_list

# 定义一个函数，用于下载图片
def download_imgs(img_list):
    print(img_list)
    i = 0
    for img in img_list:
        img_url = "http:" + img   # 需要加上http才能进行下载
        print(img_url)
        urllib.request.urlretrieve(url=img_url,filename="./imgs"+str(i)+".jpg")
        i+=1

def main():
    start = input("请输入起始页：")
    end = input("请输入终止页：")
    # 从起始页遍历到终止页
    print("开始下载...")
    img_list = []
    for i in range(int(start),int(end)+1):
        req = handle_url(url,i)
        img_list += request_pages(req)   # 这里写的巧妙，仔细读读看

    download_imgs(img_list)

    print("下载完毕！")

if __name__=="__main__":
    main()



'''换一种写法'''
url = "https://www.qiushibaike.com/pic/page/"
page_url = url + str(1)  # 第一页
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
req = urllib.request.Request(url=page_url,headers=headers)
res = urllib.request.urlopen(req)
img_list = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt=.*?>.*?</div>',re.S).findall(res.read().decode('utf-8'))
i = 0
for img in img_list:
    img_url = "http:" + img   # 需要加上http才能进行下载
    urllib.request.urlretrieve(url=img_url,filename="./imgs"+str(i)+".jpg")
    i +=1






