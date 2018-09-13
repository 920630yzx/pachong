# -*- coding: utf-8 -*-
"""
@author: 肖    这是一个爬取get请求的一个方法
"""

from urllib import request,parse

url = "http://tieba.baidu.com/f?"
# https://tieba.baidu.com/f?kw=马云
# https://tieba.baidu.com/f?kw=%E9%A9%AC%E4%BA%91

# 定义一个函数，用于处理url
def handle_url(url,baname):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    d = {"kw":baname}      # 构造一个请求体字典，对于get请求，请求体拼接到url后面！
    data = parse.urlencode(d)      # 把字典转化成请求体数据  
    ba_url = url + data   # 把data拼接到url后面，构成完整的get请求的url 
    req = request.Request(url=ba_url,headers=headers)  # 创建请求对象
    return req

# 定义一个函数，用于请求网页
def request_tieba(req):
    res = request.urlopen(req)
    r = res.read()
    return r

# 定义一个main函数，用于处理业务逻辑
def main():
    name = input("请输入你想爬取的吧名：")
    req = handle_url(url,name)      # 把url和吧名处理成一个请求对象
    res = request_tieba(req)      # 用上面的请求对象发起一个get请求，并且得到响应内容
    print(res)
    with open("tieba.html","wb") as fp:
        fp.write(res)
        
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    