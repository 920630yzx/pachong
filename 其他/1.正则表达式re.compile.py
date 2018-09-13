# -*- coding: utf-8 -*-
"""
Spyder Editor
ctrl+   方法字体
This is a temporary script file.
python爬虫(10k~43k)
    初级：10000-15000
    中高级：15K~43K
    
爬虫：采集互联网信息，代替人工。    

信息筛选-正则表达式
re.compile(正则表达式).findall(下载的数据中)

执行代码ctrl+回车
"""
"""
正则表达式：'yu'
信息数据：'aliyunedu'
\w   可以代表任意的[英文字母、
\n   代表换行

"""
# 1.匹配字符
import re

re.compile('yu').findall('aliyu=nedu')  
re.findall('yu','aliyu=nedu')  # 这样也是可以的
re.compile('yu').findall('aliyuneyudu')
re.match('\w*','aliyunedu').group()
re.match('.*','aliyunedu').group()
re.match('yu','aliyu=nedu').group()  # 这样会报错！

# 2.匹配字符
data='''aliyun
edu'''   # 三个单引号表示是一起的
re.compile('yun\n').findall(data) # 匹配换行
re.findall('yun\n',data) # 匹配换行
re.compile('al(.*)du',re.S).findall(data)  # 匹配换行,如果没有re.S则会失败

re.compile('\w').findall('、')  # \w匹配单个字符,这是正则表达式
re.compile('\w').findall('aliyu89787nedu') # u89787寻找目标
ret = re.match('\w*','aliyu89787nedu') # u89787寻找目标
print(ret.group())

"""
正则表达式中的字符代表：
普通字符	   正常匹配
.	   匹配除[换行]外任意一个字符
\n			   匹配换行符  
\t 			匹配制表符
\w 			匹配字母、数字、下划线word
\W 			匹配除字母、数字、下划线
\d 			匹配十进制数字digital
\D 			匹配除十进制数字
\s 			匹配空白字符
\S 			匹配除空白字符
[ab89x]		原子表，匹配ab89x五个字符中的任意一个
[^ab89x]		原子表，匹配除ab89x以外的任意一个字符
"""

# 3.匹配表示字符
re.compile('[ab89x]').findall('a8xy')  # ['a', '8', 'x']；[ab89x]是一个原子表,5个字符中任一一个

re.compile('\w897').findall('aliyu89787nedu')  # ['u897']

re.compile('t\w\w\we').findall('><title>百度一下，你就知道 </title><style ')  # ['title', 'title']
re.compile('t...e').findall('><title>百度一下，你就知道 </title><style ')  # ['title', 'title']
re.compile('^t...e').findall('><title>百度一下，你就知道 </title><style')  # 没有以t...e开始,固返回[]
re.compile('.tyle$').findall('><title>百度一下，你就知道 </title><style')  # 匹配以.tyle结尾,固返回['style']


"""
信息筛选---------正则表达式、想要字母、数字、以....开始的字符
基础2：
.	匹配除[换行]外任意一个字符
^	匹配开始位置
$	匹配结束位置
*	前一个字符出现0\1\多次 
?	前一个字符出现0\1次
+	前一个字符出现1\多次
{n}	前一个字符恰好出现n次
{n,}	前一个字符至少n次
{n,m}前一个字符至少n，至多m次 
|	模式选择符或
()	模式单元，通俗来说就是：[想提取出什么内容]，就在正则中用小括号将其括起来
"""

# 4.匹配表示数量
re.compile('\w{3}').findall('123a_') # ans=['123']
re.compile('\w{1,3}').findall('123a_') # 这样会先匹配3次的,再匹配2次的 ans=['123', 'a_']!


re.compile('<title>.*</title>').findall('><title>百度一下，你就知道了</title><style')  # ['<title>百度一下，你就知道了</title>']
re.compile('<title>(.*)</title>').findall('><title>百度一下，你就知道了</title><style')  # 添加括号出现区别

re.compile('<title>(.?)</title>').findall('><title>百111</title><style')  # 有四个当然找不到
re.compile('<title>(.?)</title>').findall('><title>百</title><style') # ans：['百']
re.compile('<title>(.?111)</title>').findall('><title>百111</title><style') # ans：['百111']
re.compile('<title>(.?百111)</title>').findall('><title>百111</title><style') # ans：['百111']

re.compile('<title>(.*)</title>').findall('><title>百</title><style')
re.compile('<title>(.{3})</title>').findall('><title>百度一下</title><style')
re.compile('<title>(.{4,})</title>').findall('><title>百度一下</title><style')



# 5.高级匹配：贪婪模式，懒惰模式
re.compile('py(.*)on').findall('pythonpythonpython')  # 会尽量多的匹配,不过这种模式很少用的

#提取列表,淘宝商品列表,招聘岗位列表,百度搜索列表；re.S 代表可以匹配多行的数据内容的！！！
re.compile('py(.*?)on',re.S).findall('pythonpythonpython')  # .*?注意下懒惰模式,常用！！！
re.compile('py(.*?)on').findall('pythonpythonpython')  # ans:['th', 'th', 'th']

'''.*?   是匹配（）两边字符之间的所有字符,非贪婪匹配.例如 a(.*?)b,匹配a和b之间的所有字符
,但是如果a后面有两个以上的b,只匹配到第一个b之间的字符,所以叫非贪婪匹配'''


# 6.匹配换行re.S   re.S代表可以匹配多行的数据内容的！！！
x='''pytho
n
kdjfon'''
re.compile('py.*?on').findall(x) # 匹配失败  需要使用re.S
re.compile('py.*?on',re.S).findall(x)  # ans：['pytho\nn\nkdjfon']   re.S 代表可以匹配多行的数据内容的！！！



# 7.re.I表示忽略大小写
x='''尽在智联招聘</title>
<META content
'''
re.compile('tle><ME').findall(x)

re.compile('A',re.I).findall('abc') # ignore忽略；re.I表示忽略大小写,re.S表示忽略换行

ls = re.compile('am',re.I|re.S).findall('''ami  
               ami
               ami''')



# 8.re.match
ret = re.match("[A-Z][a-z]*", "Ajfsdahsadfqwiweyue3hbdbnj")  # [A-Z]表示第一个字母；[a-z]表示第二个字母，*表示可有可无,可以出现0次到n次
print(ret.group())

re.compile('123^').findall('123a_') # ans=['123']


