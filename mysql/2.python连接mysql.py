# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 10:06:42 2018

@author: 肖
"""
# 1.mysql基本操作
import pymysql

conn = pymysql.Connect(host='127.0.0.1', 
	                   port=3306, 
	                   user='root',
                      passwd='920630yzx', 
                      db='xiao2', 
                      charset='utf8')

cursor = conn.cursor()  # 拿到一个游标
cursor.execute("select * from grade")

onerow = cursor.fetchone()  # 进入下一行，这种方法会一行接着一行运行
print(onerow[0])
print(onerow[1])
print(onerow[2])
onerow = cursor.fetchone()  # 进入下一行
print(onerow[0])
print(onerow[1])
print(onerow[2])



# 2.定义函数读取表中全部的内容
def mysql(tablename):   
    cursor = conn.cursor()  # 拿到一个游标
    sql = "select * from {table}".format(table=tablename)
    print(sql)
    cursor.execute(sql)
    while True:
	       onerow = cursor.fetchone()
	       if not onerow:
		       break
	       print(onerow)

mysql('grade')           

# 3.也能输出表中全部内容
cursor = conn.cursor()  # 拿到一个游标
cursor.execute("select * from grade")
print(cursor.fetchall())

# 4.通过python执行mysql命令的方式
cursor.execute("insert into grade(name,type) values ('python03','python')")
cursor.execute('commit')  # 提交mysql命令
cursor.execute("delete from grade where name = 'python03'")
cursor.execute('commit')  # 提交mysql命令

cursor.close()
conn.close()


