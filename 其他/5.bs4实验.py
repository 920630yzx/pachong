# -*- coding: utf-8 -*-

page_text = '''
<html>
<title> This is Title </title>
<body>
	<h1> This is h1 </h1>
	<div> This is fisrt div </div>
	<div id="divid">
		<img src="1111.png"/>
		<span id="sp1"> desc 1111.png </span>

		<img src="2222.png"/>
		<span id="sp2"> desc 2222.png </span>

		<p>
			<a href="http://www.xxxxx.com/"> link-of-xxxxxx </a>
		</p>

		<a href="http://www.yyyyyyy.com/"> link-of-yyyyyyyyy </a>
		<br/>
		<a href="http://www.zzzzzzz.com/"> link-of-zzzzzzzzz </a>

	</div>

	<p class="p_classname"> This is p with class name </p>

	<div class="div_classname"> This is div with class name </div>
	
	<!-- <div class="zhushi"> This is div with class name </div> -->

</body>
</html>
'''

from bs4 import BeautifulSoup

bsp = BeautifulSoup(page_text, 'lxml')  # 获得beautifulsoup对象

# 1.1获得title元素
print(bsp.title)  # <title> This is Title </title>
print(type(bsp.title))  # 类型是'bs4.element.Tag'
# 1.2获得title元素文本（两种写法）
print(bsp.title.text)  # This is Title 
print(bsp.title.string)  # This is Title 
  

# 2.1获得第一个 div元素（两种写法）
print(bsp.find('div'))  # <div> This is fisrt div </div>
print(bsp.div)  # <div> This is fisrt div </div>
# 2.2获得所有div元素（两种写法）
print(bsp.find_all('div'))
print(bsp.select('div'))  # 推荐
# 2.3所有拥有id属性的div元素集合列表
print(bsp.select('div[id]'))  # 推荐

# 3.1所有class属性为div_classname的所有元素（三种写法）
print(bsp.select('div[class=div_classname]'))  # 推荐
print(bsp.find_all('div', attrs={'class':'div_classname'}))
print(bsp.select('.div_classname'))
# 3.2所有id属性为divid的所有元素（相当于特权吧）
print(bsp.select('#divid'))

# 4.1最后一个div元素
print( bsp.select('div')[-1] )  # bsp.select('')  的类型是list
# 4.2倒数第2个div元素，类型列表
print(bsp.select('div')[-2])  # 推荐
print(bsp.find_all('div')[-2])
# 4.3位置为最前面2个的div元素
print(bsp.find_all('div', limit=2))
print(bsp.select('div')[0:2])

# 5.1第一个 a元素的 href 属性
print(bsp.a.get('href'))
print(bsp.find('a').get('href'))
print(bsp.a.attrs['href'])

# 5.2第二个a元素的href属性
print( bsp.find_all('a')[1].get('href'))
print(bsp.select("a")[1].get('href'))
# 5.3第三个a元素的href属性
print( bsp.find_all('a')[2].get('href'))
print(bsp.select("a")[2].get('href'))
# 5.4第二个a元素的所有属性
print(bsp.find_all('a')[1].attrs)


# 6.1  id = divid的div元素下所有层的a元素 
print(bsp.select("div[id=divid] a"))  # 推荐
print(bsp.find("div", attrs={'id':'divid'}).find_all('a'))

# 6.2 id = divid的div元素下一层的a元素（第一个a元素略过）
print( bsp.select("div[id=divid] > a") )

# 6.3 id = divid 的div标签下第1个span的id属性值
print(bsp.select("div[id=divid] span")[0].get('id'))

# 6.4踢除最后一个div元素的所有 div
print(bsp.select("div")[:-1])

# 6.5获得所有a元素的href属性集合
print([ele.get('href') for ele in bsp.select("a")])

# 6.6所有属性非空的div元素集合列表
print([ ele for ele in bsp.select("div") if ele.attrs ])

# 6.7所有属性为空的div元素集合列表
print([ele for ele in bsp.select("div") if not ele.attrs])



'''案例2：'''
from bs4 import BeautifulSoup

# 创建一个BeautifulSoup对象
soup = BeautifulSoup(page_text, 'lxml') 
# 第一个参数是一个html字符串，第二个参数是一个解析器，加上解析器以后可以增加网页的解析速度
# print(soup)

# 1、根据标签名来取对象
print(soup.title)
print(soup.a) # 从所有的a中取第一个

# 2、获取节点的属性值
obj = soup.a
print(obj.get("href"))
# print(obj['title'])
print(obj.attrs)
print(obj.name)

# 3、获取节点内容
print(obj.string)
print(obj.get_text())

# 4、用css选择器来获取
print(soup.select("div[id=divid] span")[0].string)
print(soup.select("div[id=divid] span")[1].string)
print(soup.select("div[id=divid] a")[0].string)
print(soup.select("div[id=divid] a")[1].string)
print(soup.select("div[id=divid] a")[2].string)

