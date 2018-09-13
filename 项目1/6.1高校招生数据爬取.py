# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:45:10 2018
高考--高考派(统计全中国大学招生情况，例如北京大学(3000)在北京招多少人？在重庆？在全国？)
全中国有多少所大学？
全中国有多少个城市？
在某个城市文科招的人数？理科招生的人数？
====
全国大学招生人数排行：例如
郑州大学 8000
桂林大学 6000
=
家长帮班级项目：
注意点：同一时间，访问量过大，可能会导致本次项目无法进行，因为北京那边服务器奔溃。导致全国都无法访问。
导致对方程序员加班。所以我们整个班级，需要有一套策略，要拿到所有数据但不会导致奔溃。
策略例如：
======
题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
2.根据http://www.gaokaopai.com/daxue-zhaosheng-学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
@author: 肖
"""
'''相关网址：http://www.gaokaopai.com/daxue-zhaosheng-477.html
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
#'id=477&type=2&city=51&state=1'  #猜测: id=大学编号 ;type=文理科; city=城市编号
'''
import urllib.request as r

ls = []
for i in [477]:
    for j in [51]:
        for k in [1,2]:
            print('id={}&type={}&city={}&state=1'.format(i,k,j))
            ls.append('id={}&type={}&city={}&state=1'.format(i,k,j))
            
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36','X-Requested-With':'XMLHttpRequest'}
req = r.Request(url,data=ls[1].encode(),headers=headers) 
data = r.urlopen(req).read().decode('utf-8','ignore')

'''
这里的url获取方式:先点击检查,之后clear,再点击搜索,可以看见只有一行显示出来{并且这一行右边包含From data这一行}
headers请求头：这里请求头仍在Request Headers下面,不过在传统的只有User-Agent这一行下面还有X-Requested-With,所以请求头要写两个
data=ls[1]：在第四项From Data ,view parsed中
'''

req = r.Request(url,data='id=477&type=2&city=23&state=1'.encode(),headers=headers) 
data = r.urlopen(req).read().decode('utf-8','ignore')
area = {'黑龙江':'东北','吉林':'东北','辽宁':'东北'}
areaplan = {'东北':0,'华中':0,'华南':0}
import json
data_jn = json.loads(data) 
# 进行统计:
for i in data_jn['data']:  # 依次遍历data_jn['data']
    quyu = area[i['city']]  # 获得区域名称,如东北,华中,华南等等
    areaplan[quyu] = areaplan[quyu]+int(i['plan'])
    


# 获取文档
f=open('G:/anaconda/spyder 爬虫/all_school.txt', 'r',encoding='utf-8')
ls=f.readlines()
f.close()
# 画饼图
areaplan = {}
areaplan['华中'] = 30
areaplan['华南'] = 18
areaplan['东北'] = 12
areaplan['西南'] = 8
labels = list(areaplan.keys())
values = list(areaplan.values())
print(labels)
import matplotlib.pyplot as plot
plot.rcParams['font.sans-serif'] = ['SimHei']  # 给饼图命名,这里固定写法,不必深究
plot.pie(values,labels = labels)
plot.show()



