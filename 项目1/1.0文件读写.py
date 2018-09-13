#-*- coding:utf-8 -*-
# 写上上面这一句在我们使用中文的时候不会报错
# 同时经过验证，当写入文件时如果发现目标没用这个文件，则会自动的在目标处创建一个新的文件，用于打开
# 1.w: 写入,如果该文件存在则将其覆盖；如果不存在该文件则创建一个；当然写入也会首先清空文件本来的内容，再进行写入操作。
filename = open("hi.py", 'w')  # 打开python的文件
# 向里面写入内容
filename.write('import math')  # 写入时会覆盖原内容
filename.close()  # 关流
# 法2：
with open('G:/abc.txt') as f: # 默认模式为‘r’，只读模式
     contents = f.read() # 读取文件全部内容


# 1.1 强制打开, encoding='gbk'和errors='ignore'选一个也可能可以
filename7 = open("G:/abc.txt", "r", encoding='gbk',errors='ignore')  # 无论读写都可加这个encoding='gbk',errors='ignore'
message = filename7.read()
# 法2：
with open('G:/abc.txt', "r", encoding='gbk',errors='ignore') as f: # 默认模式为‘r’，只读模式
     contents = f.read() # 读取文件全部内容



# 2.r表示读取文件;rb表示以二级制的方式读取文件
# 打开hello.py 文件.以二进制的方式将他读取出来
filenamer = open("hello", 'r')
# filenamer = open("hello", 'r', encoding='utf-8')  # encoding='utf-8'用于解决编码问题！！！！！！
message1 = filenamer.read()  # 读取全部内容。这里要注意，已经读取的行不会再次被读取，除非关流重开
print(message1)
message2 = filenamer.readline()  # 读取第一行,如果再运行一次则读取第二行
print(message2)
message3 = filenamer.readlines()  # 读取所有的行，返回一个列表
print(message3)
filenamer.close()


'''
3.测试用只写的方式写入内容,通过读取看看能不能成功
打开一个文件,通过只写入的方式，（既然是只能写入当然就不能读取了）
filetest = open("hello.py", "w")

# 在里面写入 我爱中华
filetest.write("我爱中华")

# 测试读取,注意会报 IOError: File not open for reading
message = filetest.readline()  
message.close()'''



# 3.又想读取又想写，怎么办呢？ r+，rb+方法
# r+  打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+ 以二进制格式打开一个文件用于读写,文件指针将会放在文件的开头,不会覆盖文件。
filename2 = open("abc.txt" , "r+")
filename2.write("abcdefg")
message = filename2.read()  # 由于未关闭，所以仍然读取的是以前的数据，即新写入的abcdefg不会读取出来
print(message)
filename2.close()



# 4.以w+打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除，如果该文件不存在，创建新文件。
filename7 = open("abc.txt", "w+")  
filename7.write("abcdefg")  # 写入内容
filename7 = open("abc.txt", "r")  # 再次打开读取
message = filename7.read()
print(message)
filename7.close()

# 4.1
with open('G:/abc.txt', "w", encoding='gbk',errors='ignore') as f: # 默认模式为‘r’，只读模式
     f.write('you are bitch')

# 5.追加模式a  打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。
# 如果该文件不存在，创建新文件进行写入ab 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
# 也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入

filexiao = open("abc.txt", "a")
filexiao.write(" an apple \n a bitch")
filexiao.close()



# 6.追加模式 a+ ab+ 以二进制的方式读写同时追加到后面
filenamexiaomib = open("abc.txt", "a+")
filenamexiaomib.write("面朝大海,春暖花开")  # 写入面朝大海,春暖花开
filenamexiaomib.close()





'''r：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。如果文件不存在，会报错。
rb：以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+：打开一个文件用于读写。文件指针将会放在文件的开头。如果文件不存在，会报错。
rb+：以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w：打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb：以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+：打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+：以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a：打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab：以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+：打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+：以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。'''
'''总的来说，b号表示二进制格式，+号表示既能读又能写。文本方式打开的文件具有一定的格式，说明读取时是要按照一定的编码规范来读取的，而二进制方式读取是直接从文件中读取包含0，1的二进制流，没有任何格式。
'''



#读取csv文件
import csv
"""
是否需要传参
是否需要返回  返回值
"""
def readcsv(path):  # 注意：该函数可用于csv，txt，python文件，不能用于读取excel
    infoList = []  # 定义一个列表
    with open(path, "r") as f:
        #reader()---->f
        allFileInfo = csv.reader(f)
        for row in allFileInfo:  # 遍历每一行
            infoList.append(row)
    return infoList

path = r"G:\pycharm\pycharm学习-进阶篇\文件读写\abc.txt"
info = readcsv(path)
print(info)


# 写入文件
import csv

def writeCsv(path,data):  # 注意：该函数可用于csv，txt，python文件，不能用于读取excel；写入后会覆盖原来的文件
    with open(path, "w") as f:
        writer = csv.writer(f)  # csv.writer是写入方法
        for rowData in data:  # 遍历每一行
            print(rowData)
            writer.writerow(rowData)  # writer.writerow方法完成每一行的写入

path = r"G:\pycharm\pycharm学习-进阶篇\文件读写\abc.txt"
writeCsv(path, [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])

"""
doc
docx
ppt
pdf
课下   pip
"""
