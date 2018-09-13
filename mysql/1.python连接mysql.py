# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 10:03:46 2018

@author: 肖
"""

import pymysql

client = pymysql.Connect(   # 在navacat中可以查询
    host="127.0.0.1",   # "127.0.0.1"代表本机
    port=3306,   # 端口
    user='root',   # 用户名
    password='920630yzx',  # 输入密码
    db='xiao2',   # 数据库名称
    charset='utf8'  # 指定编码格式
)

cursor = client.cursor()  # 拿到一个游标

# 1.关于操作数据库的代码如下：
def update_data():
    try:
        cursor.execute("UPDATE stu SET score=76 WHERE id=1")    # cursor.execute是执行mysql的语句
        cursor.execute("UPDATE stu SET name='Lili' WHERE id=2")  # cursor.execute执行mysql语句
    except:   # 如果程序有问题
        print('error')
        client.rollback()  # 如果程序有问题,则回滚；也就是之前执行的程序不执行了
    else:
        client.commit()  # 如果程序没问题,提交

# 2.关于取数据的代码如下：
def get_data(min_id):
    sql = "SELECT * FROM stu WHERE id>{my_id}".format(my_id=min_id)   # 拼接SQL
    print(sql)
    cursor.execute(sql)   # cursor.execute执行SQL
    # result = cursor.fetchall()  # 拿全部的结果
    result = cursor.fetchone()  # 拿一个结果,选择一个运行即可
    print(result)  # 打印结果
    print(cursor.description)  # 打印描述,这是对列情况的一个描述

update_data()  # 执行update_data函数
get_data(2)   # 执行get_data函数


''' 常用格式：
# 事务默认是开启
    try:
        cursor.execute("UPDATE stu SET name='zhangshan1' WHERE id=1")
        cursor.execute("UPDATE stu SET name1='lisi1' WHERE id=2")
    except:
        print('error')
        client.rollback()  #SQL出现异常的时候 回滚
    else:
        client.commit()  #没有问题就提交事务   
'''