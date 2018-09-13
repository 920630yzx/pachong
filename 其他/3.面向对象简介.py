# -*- coding: utf-8 -*-
"""
@author: 肖
"""
monkey = {'绰号':'星期五','公母':'公','毛色':'黄色','年龄':6}

class Monkey():
    def __init__(self,name,sex,color,age):
        self.name = name   # 添加属性
        self.sex = sex
        self.color = color
        self.age = age
    def suanshu(self,x,y):
        print(x+y)


a = Monkey('星期五','公','黄色','3')
print(a.name) 
print(a.color) 
a.suanshu(1,2)  
b = Monkey('星期三','母','白色','2')   
print(b.name)
print(b.sex)
b.suanshu(6,7)

















