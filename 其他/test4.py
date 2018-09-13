# -*- coding: utf-8 -*-
# www.bing.com/translator/?mkt=zh-CN
'''
爬取前的准备：
# url:http://cn.bing.com/ttranslate?&category=&IG=DD37F1EA27E648F7938FD1B5E504F23F&IID=translator.5036.4 
# &text=%E4%BD%A0%E5%A5%BD%E5%90%97%0D%0A%0D%0A%0D%0A%0D%0A%0D%0A&from=zh-CHT&to=en
# Cookie: MUID=26C2A3F159AC6FF538F9AFE95DAC6C9C; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=DA92A0B2D0354772B5F2426C009EFD1B&dmnchg=1; MUIDB=26C2A3F159AC6FF538F9AFE95DAC6C9C; MSCC=1; SRCHUSR=DOB=20180802&T=1533432677000; _EDGE_S=mkt=zh-cn&SID=0FB34A5E8E9F69C72635461C8FB16833; SNRHOP=I=&TS=; _TTSS_OUT=hist=["de","zh-CHT"]; SRCHHPGUSR=WTS=63669071101; _SS=SID=0FB34A5E8E9F69C72635461C8FB16833&HV=1533474302; btstkn=SNpQfrSltywF7m%252FLPGyWtFuIHkBdT5WmBWPLUFBtw2wLlSWLsZCsTrXQP4lwSmDJ

Host: cn.bing.com
Connection: keep-alive
Content-Length: 81
Origin: http://cn.bing.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36
Content-type: application/x-www-form-urlencoded
Accept: */*
Referer: http://cn.bing.com/translator/?mkt=zh-CN
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
'''
'''
表单：
category	
IG	FDCDA2DF14424F81835866C70D72E621
IID	translator.5036.2
text	你好
from	zh-CHS  to	en
'''

# 爬虫代码如下:

import requests
from lxml import etree
import time
sess = requests.session()  # 生成session对象

headers_base = {
'Host': 'cn.bing.com',
'Connection': 'keep-alive',
'Content-Length': '81',
'Origin': 'http://cn.bing.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
'Content-type': 'application/x-www-form-urlencoded',
'Referer': 'http://cn.bing.com/translator/?mkt=zh-CN',
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
}

response = requests.get("http://cn.bing.com/ttranslate?&category=&IG=DD37F1EA27E648F7938FD1B5E504F23F&IID=translator.5036.4",
             headers=headers_base)
print(response.text)


sess.cookies.set('MUID':'26C2A3F159AC6FF538F9AFE95DAC6C9C')
sess.cookies.set('SRCHD':'AF=NOFORM')
sess.cookies.set('SRCHUID':'V=2&GUID=DA92A0B2D0354772B5F2426C009EFD1B&dmnchg=1')
sess.cookies.set('MUIDB':'26C2A3F159AC6FF538F9AFE95DAC6C9C; MSCC=1')
sess.cookies.set('SRCHUSR':'DOB=20180802&T=1533432677000')
sess.cookies.set('_EDGE_S':'mkt=zh-cn&SID=0FB34A5E8E9F69C72635461C8FB16833')
sess.cookies.set('SNRHOP':'I=&TS=')
sess.cookies.set('_TTSS_OUT':'hist=["de","zh-CHT"]')
sess.cookies.set('SRCHHPGUSR':'WTS=63669071101')
sess.cookies.set('_SS':'SID=0FB34A5E8E9F69C72635461C8FB16833&HV=1533474302')
sess.cookies.set('btstkn':'SNpQfrSltywF7m%252FLPGyWtFuIHkBdT5WmBWPLUFBtw2wLlSWLsZCsTrXQP4lwSmDJ')

response = requests.get("http://www.bing.com/translator/api/Translate/TranslateArray?from=-&to=en",
             headers=headers_base)
print(response.text)



















import requests
sess = requests.session()  # 生成session对象

sess.get('http://www.bing.com/translator/?mkt=zh-CN')
print({ e.name:e.value for e in sess.cookies})  # 获取cookies

headers_base = {
#'Host': 'www.bing.com',
#'Connection': 'keep-alive',
# 'Content-Length': '31',
# 'Accept': 'application/json, text/javascript, */*; q=0.01',
#'Origin': 'http://www.bing.com',
#'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
'Content-Type': 'application/json; charset=UTF-8',
'Referer': 'http://www.bing.com/translator/?mkt=zh-CN',
#'Accept-Encoding': 'gzip, deflate',
#'Accept-Language': 'zh-CN,zh;q=0.8',
}

tran_data = '[{"id":123,"text":"吃饭"}]'.encode('utf-8')


# 手动设置 cookie
sess.cookies.set('mtstkn','WeiZJd4tGMwLFf%2Fhih5ZlcFhKEKqPUAXAMq8LiRzg3wYmR566typO58n0Wl4NgSB')
sess.cookies.set('MicrosoftApplicationsTelemetryDeviceId','a3dafa5e-d481-53a8-96b9-73acbd1c958c')
sess.cookies.set('MicrosoftApplicationsTelemetryFirstLaunchTime','1509536001304')
sess.cookies.set('destLang','en')
sess.cookies.set('dmru_list','da%2Cen')
sess.cookies.set('destDia','en-US')
sess.cookies.set('srcLang','-')
sess.cookies.set('smru_list','')
sess.cookies.set('sourceDia','zh-CN')
sess.cookies.set('_EDGE_V','1')
sess.cookies.set('MUID','1E6E8286E0CC6900340289ABE1106855')
sess.cookies.set('MUIDB','1E6E8286E0CC6900340289ABE1106855')
sess.cookies.set('SRCHD','AF=NOFORM')
sess.cookies.set('SRCHUID','V=2&GUID=E21622FC50A24DBA93299CD99245CA75&dmnchg=1')
sess.cookies.set('SRCHUSR','DOB=20171101')
sess.cookies.set('_SS','SID=3D64FAD3A98360162E13F1FDA85F61A7&HV=1509584433&bIm=757615')
sess.cookies.set('_EDGE_S','mkt=zh-cn&SID=3D64FAD3A98360162E13F1FDA85F61A7')
sess.cookies.set('SRCHHPGUSR','WTS=63645181797&CW=1019&CH=546&DPR=1&UTC=480')


# response = requests.post("http://www.bing.com/translator/api/Translate/TranslateArray?from=-&to=en",
response = sess.post("http://www.bing.com/translator/api/Translate/TranslateArray?from=-&to=en",
              headers=headers_base,
              data=tran_data
              )

print(response.text)


# https://blog.csdn.net/BeMoreQuiet/article/details/54616527
