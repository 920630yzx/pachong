# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 21:03:57 2018

@author: 肖
"""

filename = open("D:\坦克世界/test.txt", 'r' )  # 打开python的文件
message = filename.readlines()  
print(message)
# 关流
filename.close()


xx = lambda x:x**2
xx(3)

ls = [10,10,15,20,15,10,20,15,10]
ls.count(10)
myls=[]
for i in ls:
    myls.append('{}-{}'.format(i,ls.count(i)))
myls.sort(key=lambda s:int(s.split('-')[1]))
myls[1].split('-')[1]














