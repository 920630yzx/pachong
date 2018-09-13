# -*- coding: utf-8 -*-
"""
@author: 肖    # 69课(3)---可以再去看看---这是完整版---同时可以试试改成xpath版本的
这里是爬取智联的案例---
如果使用urllib获取会得到js加密的源代码，没有任何意义，因此需要借助浏览器来执行---selenium,PhantomJS
如何知道是js加密的源码：1.源代码与检查下的代码之间差距过大; 2.使用xpath,bs4时是无法解析的（理由还是差距过多,需要动态加载）
"""

import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.parse
from time import sleep
import json

class ZhilianSpider(object):

    def __init__(self,url,job,area,start,end):
        self.url = url
        self.start = start
        self.end = end
        self.job = job
        self.area = area
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    # 定义一个成员方法，用于处理url
    def handle_url(self,page):
        # 处理请求体数据
        d = {
            'jl':self.area,
            'kw':self.job,
            'p':page,
            'kt':3
        }
        data = urllib.parse.urlencode(d)
        # 处理url
        url = self.url + data
        # 创建请求对象
        # req = urllib.request.Request(headers=self.headers,url=url)
        return url
    
    # 定义一个方法，抓取网页内容
    def request_jobs(self,req):
        # res = urllib.request.urlopen(req)
        # 创建一个webdriver对象
        driver = webdriver.PhantomJS('F:/phantomjs-2.1.1-windows/bin/phantomjs')
        driver.get(req)
        sleep(2)
        res = driver.page_source
        driver.quit()
        soup = BeautifulSoup(res,'lxml')
        # 选取出所有的招聘信息
        job_list = soup.select(".infoBox")
        # print(job_list)
        for job in job_list:           
            job_name = job.select(".job_title")[0].get_text()  # 岗位信息,get_text()替换成extract也是可以的；[0]表示访问列表第一个元素
            com_name = job.select(".company_title")[0].get_text()  # 公司名称         
            salary = job.select(".job_saray")[0].get_text()  # 薪资          
            address = job.select(".demand_item")[0].get_text()   # 工作地点        
            welfare = job.select(".job_welfare")[0].get_text()   # 福利
            # 创建一个字典，用于整合所有的信息
            item = {"job_name":job_name,"company":com_name,"salary":salary,"address":address,"welfare":welfare}
            yield item  # 这里理解起来有些难度

    # 定义一个方法，提供对外接口
    def start_request(self):
        # 定义一个列表用于整合所有的信息
        jobItems = []
        for page in range(int(self.start),int(self.end)+1):
            # 调用业务方法，取处理页面的爬取逻辑
            req = self.handle_url(page)
            items = self.request_jobs(req)
            for item in items:  # 跟yield item联系起来
                jobItems.append(item)

        with open("zhilian.json",'w',encoding='utf-8') as fp:
            fp.write(json.dumps(jobItems))

# 定义一个main函数，用于处理业务逻辑
def main():
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?"
    area = input("请输入工作地点：")
    job = input("请求输入岗位名称：")
    start = input("请输入起始页：")
    end = input("请输入终止页：")

    zhi = ZhilianSpider(url=url,job=job,area=area,start=start,end=end)
    zhi.start_request()

if __name__ == '__main__':
    main()





