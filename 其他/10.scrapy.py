# -*- coding: utf-8 -*-
'''
常见指令
• scrapy startproject app01   创建爬虫项目(大文件夹)
• cd app01   调整至新创建的app01路径下(首先需要将路径调整app01的父级路径)
• scrapy genspider -l   查看爬虫模板(可以看见4个模板,分别是basic,crawl,csvfeed,xmlfeed)
• scrapy genspider -t basic ts baidu.com   创建爬虫程序
#-t是创建的意思,basic表示选择basic爬虫类型;ts是新建的爬虫程序名称,baidu.com是爬取的网站网址
• scrapy crawl ts   运行爬虫,ts是爬虫程序的文件名称 (最好在app01的路径下运行)
• scrapy crawl ts --nolog    运行爬虫,ts是爬虫程序的文件名称,不过这行会省略运行的日志(过程)
• scrapy list   查看有哪些爬虫程序
#scrapy crawl test1 --nolog  运行爬虫,不过爬虫程序名称不同


框架架构 总共分5个步骤,依次运行:settings.py;items.py;middlewares.py;ts.py;pipelines.py
• app01>scrapy crawl ts --nolog  运行爬虫程序
• settings.py  设置信息,设置配置
• items.py   爬取的数据有哪些
• middlewares.py SpiderMiddleware   爬取数据之前干嘛？爬虫中间处理过程
• middlewares.py DownloaderMiddleware  下载数据之前干嘛？爬虫中间处理过程
• ts.py  开始爬取数据,ts为创建的爬虫程序名称
• pipelines.py  爬取之后干嘛?保存到数据库


框架组件
• settings.py文件主要是对整个爬虫项目进行设置配置的
• items.py对爬虫的项目实体类保存
• middlewares.py 爬虫中间处理过程
• middlewares.py 下载之前想要设置代理等
• ts.py 爬虫项目
• pipelines.py 对数据进行后续处理实现对编写的数据爬后处理,比如写入数据库等


scrapy爬虫类型
• basic 常用爬虫
• crawl 通用爬虫(crawl爬取)
• csvfeed csv爬虫
• xmlfeed xml爬虫


数据提取-xpath表达式
• 是一种除了正则表达式之外,非常实用的一种表达式,是一种非常好用的信息筛选的工具
• /                                  逐层提取
• text()                          提取标签下面的文本
• //标签名**                     提取所有名为**的标签
• //标签名[@属性='属性值']         提取属性为XX的标签
• @属性名                           代表取某个属性值
'''








