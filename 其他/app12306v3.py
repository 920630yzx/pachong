# -*- coding: utf-8 -*-
"""
Created on Sun May 27 22:05:03 2018

@author: yq
"""
import urllib.request
import re
import ssl
import urllib.parse
import http.cookiejar
import datetime
import time
import json     
import sys   
import urllib.request as r
#将对象中的url和请求参数__str__提取进行网络请求
getobj=lambda obj:r.urlopen(obj.url+"?"+str(obj)).read().decode("utf-8","ignore")
postobj=lambda obj:r.urlopen(r.Request(obj.url,str(obj).encode('utf-8'))).read().decode("utf-8","ignore")  
#将url和请求参数进行网络请求
get=lambda url,params:r.urlopen(url+"?"+params).read().decode("utf-8","ignore")
getnoparams=lambda url,params:r.urlopen(url).read().decode("utf-8","ignore")
post=lambda url,params:r.urlopen(r.Request(url,params.encode('utf-8'))).read().decode("utf-8","ignore")  


class Ticker:#GET
    """用于12306 余票查询的信息"""
    url='https://kyfw.12306.cn/otn/leftTicket/query'
    def __init__(self,start='北京',to='上海',student='ADULT',date=None):
        self.start = self.__areatocode__(start)
        self.start1=start
        self.to = self.__areatocode__(to)
        self.to1=to
        self.student = student#是学生0X00
        self.date = date#time.strftime('%Y-%m-%d',time.localtime(time.time()))
    def __areatocode__(self,city):
        import pandas
        data=pandas.read_excel('./火车站编码.xls',sheetname=0)
        code=data[data.station == city].code.values[0] 
        return code
    
    def showcheci(self,allcheci,checimap):
        self.code=[]
        self.secretStr=[]
        self.zy=[]
        
        print("车次\t出发站名\t到达站名\t出发时间\t到达时间\t一等座\t二等座\t硬座\t无座")
        for i in range(0,len(allcheci)):
            thischeci=allcheci[i].split("|")
            #[3]---code
            codet=thischeci[3]
            #[6]---fromname
            fromname=checimap[thischeci[6]]
            #[7]---toname
            toname=checimap[thischeci[7]]
            #[8]---stime
            stime=thischeci[8]
            #[9]---atime
            atime=thischeci[9]
            #[28]---yz
            yz=thischeci[31]
            #[29]---wz
            wz=thischeci[30]
            #[30]---ze
            ze=thischeci[29]
            #[31]---zy
            zyt=thischeci[26]
            
            print(codet+"\t"+fromname+"\t"+toname+"\t"+stime+"\t"+atime+' \t    一等{}     二等{}          无坐{}'.format(yz,wz,zyt))
            #########
            thiscode1=thischeci[3]
            self.code.append(thiscode1)
            #[0]---secretStr
            self.secretStr.append(thischeci[0].replace('"',""))
            #[31]-zy
            thiszy=thischeci[31]
            self.zy.append(thiszy)
        
        #用字典trainzy存储车次有没有票的信息
        self.trainzy={}
        for i in range(0,len(self.code)):
            self.trainzy[self.code[i]]=self.zy[i]
        #用字典traindata存储车次secretStr信息，以供后续订票操作
        #存储的格式是：traindata={"车次1":secretStr1,"车次2":secretStr2,…}
        self.traindata={}
        for i in range(0,len(self.code)):
            self.traindata[self.code[i]]=self.secretStr[i]
            
    def __str__(self):
        queryparams='leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes={}'
        return queryparams.format(self.date,self.start,self.to,self.student)

class LoginUser:#POST
    """用于登陆12306平台网站的用户"""
    url='https://kyfw.12306.cn/passport/web/login'
    def __init__(self,username,pwd,cardname,cardid,mobile):
        self.username=username
        self.pwd=pwd
        self.cardname=cardname
        self.cardid=cardid
        self.mobile=mobile
#        post(self.obj)
        
    def __str__(self):
        return urllib.parse.urlencode({
                "username":self.username,
                "password":self.pwd,
                "appid":"otn",
                })
  
class Verification_code:
    """用于登陆12306平台网站的验证码登陆"""
    url='https://kyfw.12306.cn/passport/captcha/captcha-check'
    def __init__(self):
        self.pic_nums=self.imgtocode()
    
    def __str__(self):
        return urllib.parse.urlencode({
                "answer":self.pic_nums,
                "rand":"sjrand",
                "login_site":"E",
                })
    
    ##验证码验证
    def imgtocode(self):
        print('正在加载验证码...')
        r.urlretrieve('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand','./tempcode.png')
        #查看图片
        import os
        os.system('mspaint tempcode.png')
        no=input('请选择图片序号(例如12,是图片1图片2):')
        answerdict={"1":[39,43],"2":[111,41],"3":[182,40],"4":[254,42],
                "5":[41,114],"6":[112,111],"7":[183,105],"8":[254,104]}
        numsarr=[[nums for nums in answerdict[index]] for index in list(no)]
        answer=[]
        for nums in numsarr:
            answer.extend(nums)
        answer=str(answer).replace('[','').replace(']','')
        print('验证码数据是：',answer)
        return answer    
    
class OrderInfo:#POST
    """用于登陆12306平台网站购票选择的乘客信息"""
    url='https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo'
    def __init__(self,name,noid,mobile,token):
        self.name = name
        self.noid = noid
        self.mobile = mobile
        self.token = token
        
    def __str__(self):
        return urllib.parse.urlencode({
            "cancel_flag":2,
            "bed_level_order_num":"000000000000000000000000000000",
            "passengerTicketStr":"M,0,1,{},1,{},{},N".format(self.name,self.noid,self.mobile),
            "oldPassengerStr":"{},1,{},1_".format(self.name,self.noid),
            "tour_flag":"dc",
            "randCode":"",
            "whatsSelect":1,
            "_json_att":"",
            "REPEAT_SUBMIT_TOKEN":self.token,
            })
            
class Passenger:
    '检查乘客获取确定订单的一些token信息'
    url0='https://kyfw.12306.cn/otn/confirmPassenger/initDc'
#    url='https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
    def __init__(self):
        self.train_no=''
        self.leftTicketStr=''
        self.fromStationTelecode=''
        self.toStationTelecode=''
        self.train_location=''
        self.token = ''
        #获取train_no、leftTicketStr、fromStationTelecode、toStationTelecode、train_location
        self.confirmfirmPassenger()
    
    def confirmfirmPassenger(self):
        req7data=post(self.url0,urllib.parse.urlencode({
            "_json_att":""
            }))
        #获取
#        train_no,leftTicketStr,fromStationTelecode,toStationTelecode,train_location
        train_no_pat="'train_no':'(.*?)'"
        leftTicketStr_pat="'leftTicketStr':'(.*?)'"
        fromStationTelecode_pat="from_station_telecode':'(.*?)'"
        toStationTelecode_pat="'to_station_telecode':'(.*?)'"
        train_location_pat="'train_location':'(.*?)'"
        pattoken="var globalRepeatSubmitToken.*?'(.*?)'"
        patkey="'key_check_isChange':'(.*?)'"
        train_no_all=re.compile(train_no_pat).findall(req7data)
        if len(train_no_all)>0:
            self.train_no=train_no_all[0]
        leftTicketStr_all=re.compile(leftTicketStr_pat).findall(req7data)
        self.leftTicketStr=leftTicketStr_all[0]
        fromStationTelecode_all=re.compile(fromStationTelecode_pat).findall(req7data)
        self.fromStationTelecode=fromStationTelecode_all[0]
        toStationTelecode_all=re.compile(toStationTelecode_pat).findall(req7data)
        self.toStationTelecode=toStationTelecode_all[0]
        train_location_all=re.compile(train_location_pat).findall(req7data)
        self.train_location=train_location_all[0]
        
        tokenall=re.compile(pattoken).findall(req7data)
        self.token=tokenall[0]
        keyall=re.compile(patkey).findall(req7data)
        self.key=keyall[0]
        #还需要获取train_location
        pattrain_location="'tour_flag':'dc','train_location':'(.*?)'"
        train_locationall=re.compile(pattrain_location).findall(req7data)
        self.train_location=train_locationall[0]
        
class TickerControl:
    '余票查询、预定验证码验证、登陆、选择乘客、提交订单、选座确定订单、等待订单处理结果、确定支付'
    def __init__(self,loginuser:LoginUser):
        self.__网络设置__()
        self.loginuser = loginuser
        self.用户登陆()
#        self.获取乘客信息()
        
    def __网络设置__(self):
        #为了防止ssl出现问题，你可以加上下面一行代码
        ssl._create_default_https_context = ssl._create_unverified_context
        #建立cookie处理
        cjar=http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
        #添加用户代理
        opener.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')]
        urllib.request.install_opener(opener)
    
    def 用户登陆(self):
        def 验证码验证(vercode:Verification_code):
            return postobj(vercode).find('成功')!=-1
        while True:
            if 验证码验证(Verification_code()):
                break
        #用户名密码登陆
        for i in range(0,4):
            if postobj(self.loginuser).find('成功')!=-1:
                break
            if i==3:
                print('密码错误超过4此，此账号暂时不能用')
                sys.exit()
        #其他验证
        post('https://kyfw.12306.cn/otn/login/userLogin',urllib.parse.urlencode({
            "_json_att":"",
            }))
        data=post('https://kyfw.12306.cn/passport/web/auth/uamtk',urllib.parse.urlencode({
            "appid":"otn",
            }))
        tk=re.compile('"newapptk":"(.*?)"',re.S).findall(data)[0]
        
        post('https://kyfw.12306.cn/otn/uamauthclient',urllib.parse.urlencode({
            "tk":tk,
            }))
        #爬个人中心页面
        data=getnoparams('https://kyfw.12306.cn/otn/index/initMy12306','')
        loginname=re.compile('<a id="login_user" href="/otn/index/initMy12306" class="colorA" style="margin-left:-0.5px;"><span style="width:50px;">(.*?)</span>',re.S).findall(data)
        print("登陆完成"+len(str(loginname)))
    
    #######################
    def 订票(self,ticker:Ticker):
        self.ticker = ticker
        self.余票查询(ticker)
        self.提交订单请求()
        self.选择乘客确定()
        self.选座确定订单()
    #######################
    
    def 余票查询(self,ticker:Ticker):
        data=json.loads(getobj(ticker))['data']
        allcheci=data['result']
        checimap=data['map']
        ticker.showcheci(allcheci,checimap)
        self.thiscode=input("请输入要预定的车次：")
        
    def 提交订单请求(self):
        ticker=self.ticker
        #订票-第1次post-主要进行确认用户状态
        post('https://kyfw.12306.cn/otn/login/checkUser',urllib.parse.urlencode({
            "_json_att":""
            }))
        #自动得到当前时间并转为年-月-格式，因为后面请求数据需要用到当前时间作为返程时间backdate
        backdate=datetime.datetime.now()
        backdate=backdate.strftime("%Y-%m-%d")
        #订票-第2次post-主要进行“预订”提交
        post('https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest',urllib.parse.urlencode({
            "secretStr":ticker.traindata[self.thiscode],
            "train_date":ticker.date,
            "back_train_date":backdate,
            "tour_flag":"dc",
            "purpose_codes":ticker.student,
            "query_from_station_name":ticker.start1,
            "query_to_station_name":ticker.to1,
            }).replace("%25","%"))
        #订票-第3次post-主要获取Token、leftTicketStr、key_check_isChange、train_location
        passenger=Passenger()
        self.passenger = passenger
        
    def 选择乘客确定(self):
        #选择乘客
        token=self.passenger.token
        us=self.loginuser
        self.orderInfo=OrderInfo(us.cardname,us.cardid,us.mobile,token)
        #总请求1-点击提交后步骤1-确认订单(在此只定一等座，座位类型为M，如需选择多种类型座位，可以自行修改一下代码使用if判断一下即可)
        data=postobj(self.orderInfo)
        print("选择乘客确定：",data)
    
    def 选座确定订单(self):
        def 等待订单处理结果(token):
            time1=time.time()
            while True:
                #总请求4-确认步骤2-获取orderid
                time2=time.time()
                if((time2-time1)//60>5):
                    print("获取orderid超时，正在进行新一次抢购")
                    break
                data=get("https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime",urllib.parse.urlencode({
                        "random":str(int(time.time()*1000)),
                        "tourFlag":"dc",
                        "_json_att":"",
                        "REPEAT_SUBMIT_TOKEN":str(token)
                        }))
                try:
                    orderid=re.compile('"orderId":"(.*?)"').findall(data)[0]
                    break
                except Exception as err:
                    print("未获取到orderid，正在进行新一次的请求。",data)
                    continue
                
            #总请求5-确认步骤3-请求结果
            data=post('https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue',urllib.parse.urlencode({
                    "orderSequence_no":orderid,
                    "_json_att":"",
                    "REPEAT_SUBMIT_TOKEN":str(token)
                    }))
            print("等待订单处理结果",data)
            #总请求6-确认步骤4-支付接口页面
            data=post('https://kyfw.12306.cn/otn//payOrder/init',urllib.parse.urlencode({
                    "_json_att":"",
                    "REPEAT_SUBMIT_TOKEN":str(token)
                    }))
            print("订单已经完成提交，您可以登录后台进行支付了。",len(data)) 
        
        #总请求2-点击提交后步骤2-获取队列
        #将日期转为格林时间
        passenger=self.passenger
        ticker=self.ticker
        info=self.orderInfo
        token = info.token
        name=info.name
        noid=info.noid
        mobile=info.mobile
        
        #将leftstr2转成指定格式
        leftstr2=passenger.leftTicketStr.replace("%","%25")
        data=post('https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount',urllib.parse.urlencode({
            "train_date":str(self.__datetogm__(ticker.date))+"+00%3A00%3A00+GMT%2B0800",
            "train_no":passenger.train_no,
            "stationTrainCode":self.thiscode,
            "seatType":"M",
            "fromStationTelecode":passenger.fromStationTelecode,
            "toStationTelecode":passenger.toStationTelecode,
            "leftTicket":leftstr2,
            "purpose_codes":"00",
            "train_location":passenger.train_location,
            "_json_att":"",
            "REPEAT_SUBMIT_TOKEN":str(token)
            }))
        
        print("选座确定订单",data)
        #总请求3-确认步骤1-配置确认提交
        data=post('https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue',urllib.parse.urlencode({
            "passengerTicketStr":"M,0,1,"+str(name)+",1,"+str(noid)+","+str(mobile)+",N",
            "oldPassengerStr":str(name)+",1,"+str(noid)+",1_",
            "randCode":"",
            "purpose_codes":"00",
            "key_check_isChange":passenger.key,
            "leftTicketStr":passenger.leftTicketStr,
            "train_location":passenger.train_location,
            "choose_seats":"",
            "seatDetailType":"000",
            "whatsSelect":"1",
            "roomType":"00",
            "dwAll":"N",
            "_json_att":"",
            "REPEAT_SUBMIT_TOKEN":token,
            }))
        print("等待处理前：",data)
        等待订单处理结果(token)
        
    def __datetogm__(self,date):
        '将日期转为格林时间'
        #先将字符串转为常规时间格式
        thisdate=datetime.datetime.strptime(date,"%Y-%m-%d").date()#date需要的买票时间
        #再转为对应的格林时间
        gmt='%a+%b+%d+%Y'
        thisgmtdate=thisdate.strftime(gmt)
#        print(thisgmtdate)
        return thisgmtdate         



