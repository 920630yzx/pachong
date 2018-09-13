
# -*- coding: utf-8 -*-
"""
@author: 肖
"""

import urllib.request
from lxml import etree
from time import sleep

# 定义个函数，用于将url和页面页码处理成一个请求对象
def handle_url(url,page):
    if page == 1:  # 其实可以不写这段
        page_url = url
    else:
        page_url = url + "index_" + str(page) + ".html"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    req = urllib.request.Request(headers=headers,url=page_url)
    return req

# 定义一个函数，用于发起网络请求，并且把所有的图片地址返回
def request_img(req):
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    html_tree = etree.HTML(html)
    img_list = html_tree.xpath("//div[starts-with(@class,'box')]//a/img/@src2")
    return img_list

# 定义一个函数，下载所有的图片
def download_imgs(img_list):
    path = "./imgs"
    for img in img_list:
        # suffix = os.path.splitext(img)[-1]
        filename = img.split("/")[-1]
        print(filename)
        print("当前正在下载：",img)
        sleep(0.5)
        urllib.request.urlretrieve(img,path+filename)

def main():

    start = input("请输入起始页：")
    end = input("请输入终止页：")
    url = "http://sc.chinaz.com/tupian/"
    print("开始下载...")
    img_urls = []
    # 遍历所有的页面
    for page in range(int(start),int(end)+1):
        req = handle_url(url,page)
        im_list = request_img(req)
        img_urls += im_list
        download_imgs(im_list)

if __name__ == '__main__':
    main()


'''换一种写法'''
url = "http://sc.chinaz.com/tupian/"
page_url = url + "index_" + str(2) + ".html"  # 注意：http://sc.chinaz.com/tupian/index_1.html是不存在的,这里的第一页即是http://sc.chinaz.com/tupian/
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
req = urllib.request.Request(url=page_url,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')
html_tree = etree.HTML(html)
img_list = html_tree.xpath("//div[starts-with(@class,'box')]//a/img/@src2")
i = 0
for img in img_list:
    filename = img.split("/")[-1]
    print(filename)
    print("当前正在下载：",img)
    sleep(0.5)
    urllib.request.urlretrieve(img,"./imgs"+filename)













