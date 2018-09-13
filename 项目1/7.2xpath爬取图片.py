# -*- coding: utf-8 -*-
import requests
from lxml import etree
import time

headers_base = {
'Host': 'www.gandianli.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
}
# 1.爬取一张图片的方法
# 提交图片url请求
response = requests.get("http://img.gandianli.com/201611/14/20305643732.png.thumb.png",
             headers=headers_base)

# A = response.text
# B = response.content
with open("tu.jpg", 'wb') as f:  # 保存的方式必须是以wb的方式
    f.write(response.content)  # 1.注意保存图片必须是response.content不能是response.text



# 2.笔记本信息爬取（爬取一个网页中多张图片）
'''笔记本网址:
https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BAmagicbook&enc=utf-8&wq=%E5%8D%8E%E4%B8%BA   # 第一页
https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BAmagicbook&enc=utf-8&wq=%E5%8D%8E%E4%B8%BA&page=3  # 第二页
'''
url='http://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BAmagicbook&enc=utf-8&wq=%E5%8D%8E%E4%B8%BA'
response = requests.get(url, headers=headers_base)
response.encoding = 'utf-8'  # 对乱码进行修改
html = etree.HTML(response.text)  # html的类型为lxml.etree._Element
'''
html = response.text
with open ('abc.txt','w',encoding='gbk',errors='ignore') as f:
    f.write(html)'''  # 由于检查的网页代码与源代码不完全相同，可以运行这个在txt文件中看看

# 2.1从获取到的html页面中使用xpath提取title信息和href信息
title_list = html.xpath("//div[@class='gl-i-wrap']/div[@class='p-name p-name-type-2']/a/@title|\
                      //div[@class='gl-i-wrap']/div[@class='p-name p-name-type-2']/a/@href",ensure_ascii = False)
for title in title_list:
    print(title)
    
# 2.2从获取到的html页面中使用xpath提取图片url列表，根据图片名称进行打印到指定的位置。
src_list = html.xpath("//div[@class='gl-i-wrap']/div[@class]/a/img/@source-data-lazy-img")  # 图片
for src in src_list:
    print(src)
    img_name = src.split('/')[-1]  # 获取图片名称
    print(img_name)
    response = requests.get("http:" + src, headers=headers_base)
    time.sleep(0.1)
    with open('F:/pa/' + img_name, 'wb') as f:
         f.write(response.content)
    
    
   
# 2.3爬取多页多张图片  
for index in [1,3]:
    url = 'http://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BAmagicbook&enc=utf-8&wq=%E5%8D%8E%E4%B8%BA&page='+str(index)
    response = requests.get(url, headers=headers_base)
    response.encoding = 'utf-8'  # 对乱码进行修改
    html = etree.HTML(response.text)  # html的类型为lxml.etree._Element
    src_list = html.xpath("//div[@class='gl-i-wrap']/div[@class]/a/img/@source-data-lazy-img")  # 使用xpath爬取图片信息
    for src in src_list:
        print(src)
        img_name = src.split('/')[-1]  # 获取图片名称
        print(img_name)
        response = requests.get("http:" + src, headers=headers_base)
        time.sleep(0.1)
        with open('F:/pa/' + img_name, 'wb') as f:
             f.write(response.content)
    
    
        
'''当然也可以写成函数的形式
def download_onepage_img(page_url):
    response = requests.get(page_url, headers=headers_base)
    html = etree.HTML(response.text)
    src_list = html.xpath("//img[@class='sell_img']/@src")
    for src in src_list:
        img_name = src.split('/')[-1]  # 提取图片名称
        print(img_name)    
        img_response = requests.get(src, headers=headers_base)  # 发送请求，获得响应
        with open('/root/PycharmProjects/img_files/'+img_name, 'wb') as f:
            f.write(img_response.content)


for index in range(1,142):
    page_url = "http://www.gandianli.com/sell/list.php?catid=&page=" + str(index) + \
           "&price=0&thumb=0&vip=0&day=0&order=&list=1"
    time.sleep(2)
    download_onepage_img(page_url)'''




