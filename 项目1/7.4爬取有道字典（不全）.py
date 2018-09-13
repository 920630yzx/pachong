# -*- coding: utf-8 -*-
"""
@author: 肖    爬取有道翻译字典(并不完整)
"""
import requests
sess = requests.session()  # 生成session对象
sess.get('http://fanyi.youdao.com/')  # 初始网址
print({ e.name:e.value for e in sess.cookies})  # 获取cookies

headers_base = {
'Host':'fanyi.youdao.com',
'Connection':'keep-alive',
'Content-Length':'214',
'Accept':'application/json, text/javascript, */*; q=0.01',
'Origin':'http://fanyi.youdao.com',
'X-Requested-With':'XMLHttpRequest',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Referer':'http://fanyi.youdao.com/',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
}  # 填上raw中的部分数据

tran_data = {
'smartresult':'dict',
'smartresult':'rule',
'from':'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'i':'女朋友',
'salt':'1533562058259',
'sign':'c6b949d1d5043c909c0ed138c215eb57',
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_REALTIME',
'typoResult':'false',}  # 填上表单中的数据，调整顺序一般不受影响

response = sess.post("http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule",
              headers=headers_base,
              data=tran_data
              )

print(response.text)

'''
'i':'你好',
'salt':'1533525515867',
'sign':'9dfd4483a276ad14e9942a115dc2e857','''




'''
1. raw中数据
POST http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule HTTP/1.1
Host: fanyi.youdao.com
Connection: keep-alive
Content-Length: 214
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://fanyi.youdao.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://fanyi.youdao.com/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: OUTFOX_SEARCH_USER_ID=-1490980753@125.70.166.113; P_INFO=m13228160137_2@163.com|1531712797|0|other|00&99|null&null&null#sic&510100#10#0#0|132137&1|urs&unireg|13228160137@163.com; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcrE8P4ScP5-605H9muw; OUTFOX_SEARCH_USER_ID_NCOO=1045493282.2685945; _ntes_nnid=0448b1d000548eb7603094d1962a6c70,1533520804980; ___rl__test__cookies=1533525515855

i=%E4%BD%A0%E5%A5%BD&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=1533525515867&sign=9dfd4483a276ad14e9942a115dc2e857&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_REALTIME&typoResult=false



2.表单中的数据:
smartresult	dict
smartresult	rule
i	你好
from	AUTO
to	AUTO
smartresult	dict
client	fanyideskweb
salt	1533525515867
sign	9dfd4483a276ad14e9942a115dc2e857
doctype	json
version	2.1
keyfrom	fanyi.web
action	FY_BY_REALTIME
typoResult	false 
'''
