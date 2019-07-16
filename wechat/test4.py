# -*- coding: utf-8 -*-
# a=lambda x,y:x*y
# print(a(4,5))
# b=[x**2 for x in range(10)]
# print(b)
#
# c=((1,2),(3,4),(5,6))
# c1=dict(c)
# print(c1)
# for key,value in c1.items():
#     print(key,value)
# for item in c1.items():
#     print(item)
#
# d=['1','2','3']
# e=['4','5','6']
# f=zip(e,d)
# print(f)
# g=zip(*f)
# print(g)

# while True:
#     a=int(input('请输入第一个数字：'))
#     if a %2 ==0:
#         while True:
#             b=int(input('请输入第二个数字：'))
#             if b %3 ==0:
#
#                 print(a*b)
#                 break
#             else:
#                 print('请输入3的倍数')
#         break
#     else:
#         print('请输入2的倍数')
# x = 1
# while x <= 10:
#     print("x", x)
#     y = 1
#     while y <= 10:
#         print("y", y)
#         y = y + 1
#     x = x + 1
# import random
# print(random.random())

# from pymysql import *
# from django.http import HttpResponse, JsonResponse
# import json
# from django.shortcuts import render
#
# def search_book( serial):
#     conn = connect(host='192.168.4.181',
#                    user='root',
#                    password='mysql',
#                    database='kudie',
#                    port=3306,
#                    charset='utf8')
#     print(123)
#     # 2. 获取数据库的操作对象　ｃｕｒｓｏｒ
#     cur = conn.cursor()
#     sql = 'select bookid,booksname,url from obook where serial=%s and status=False'
#     ret = cur.execute(sql, serial)
#     # data = cur.fetchall()
#     # data = list(data)
#     # print(data)
#     # data = json.dumps(data)
#     # print(data)
#     #
#     # cur.close()
#     # conn.close()
#     # a = data.decode('raw_unicode_escape')
#     # print(a)
#     # a=eval(a)
#     # data = json.loads(data)
#     # return  JsonResponse({'data':data.decode('raw_unicode_escape')})
#     # return HttpResponse(data.decode('raw_unicode_escape'))
#     # return render(request,'test.xml',{'a':a})
#     # return render(request,'tel.xml',{'a':a},content_type="text/xml")
#     print(ret)
#
# if __name__ == '__main__':
#     search_book('2015wewrrq')

# def add(x,y):
#     print(x+y)
#
# add()
# import sys
#
# print sys.argv
# import json
#
#
# def writeDict(data):
#     with open("data.txt", "w") as f:
#         f.write(json.dumps(data, ensure_ascii=False))
#
#
# if __name__ == '__main__':
#     dict_1 = {"北京": "BJP", "北京北": "VAP", "北京南": "VNP", "北京东": "BOP", "北京西": "BXP"}
#
#     writeDict(dict_1)
# -*- coding: UTF-8 -*-

# i = int(raw_input('净利润:'))
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r = 0
# for idx in range(0, 6):
#     if i > arr[idx]:
#         r += (i - arr[idx]) * rat[idx]
#         print (i - arr[idx]) * rat[idx]
#         i = arr[idx]
# print r
# -*- coding: UTF-8 -*-

# for i in range(1, 85):
#     if 168 % i == 0:
#         j = 168 / i;
#         if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
#             m = (i + j) / 2
#             n = (i - j) / 2
#             x = n * n - 100
#             print(x)

# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
# import hashlib
#
# path = 'download' + '/' + '马克吐温1234' + '/' + 'CSDN' + '.epub'
# print(path)
# with open(path) as f:
#     news_data = f.read()
#     # print(book_data)
# print('****')
# md5str = news_data
# m1 = hashlib.md5()
# m1.update(md5str.decode('latin-1'))
# token = m1.hexdigest()
# print(token)
#
# import string
# l='明天,你好'
# m = l.translate(None, string.punctuation)
# print(m)
#
# print(l)

# import re
# from zhon.hanzi import punctuation
# line =  "测试。。去除标点。。"
# print re.sub(ur"[%s]+" %punctuation, "", line.decode("utf-8")) # 需要将str转换为unicode
# print re.sub(ur"[%s]+" %punctuation, "", line) #将不会发生替换

# x = [1, 2, 3]
#
# y = [4, 5, 6]
#
# z = [7, 8, 9]
#
# xyz = zip(x, y, z)
#
# print(type(xyz))
# print(xyz)
# import urllib
# WECHAT_APPID = "wx1fc6ff9824c795d3"
# WECHAT_APPSECRET = "7dcac95970536dc7cf3a44745965b3fa"
# # WECHAT_APPID = "wxfb86c393c98cbc31"
# # WECHAT_APPSECRET = "7e348419472320d17b9fe148c62ac951"
# url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (
# WECHAT_APPID, WECHAT_APPSECRET)
# response = urllib.urlopen(url).read()
#
# print(response)

# import datetime
# import random
# for i in range (0,10):
#     nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")#生成当前时间
#     print(str(nowTime))
#     randomNum=random.randint(0,100)#生成的随机整数n，其中0<=n<=100
#     if randomNum<=10:
#         randomNum=str(0)+str(randomNum)
#     uniqueNum=str(nowTime)+str(randomNum)
#     print uniqueNum

# o47Fa0mp9SRTf3eiKmqWm69BjG_8
# o_Tvk1beiykoZ2Xqp6ltXZiMo5lQ
# B4nYjnoHhuWrPVi2pYLuPjnCaU0

# data = '<?xml version="1.0" encoding="utf-8"?>
# <string xmlns="http://XXX.org/">8888</string>'
# import xml.etree.ElementTree as ET
# root = ET.fromstring(data)
# node = root.find('EventKey')
# node1 = root.find('Event')
# node2 = root.find('Ticket')
# node3 = root.find('FromUserName')
# node =node.text
# node = int(node)
# print(node)
# print(node.text)
# print(node1.text)
# print(node2.text)
# print(node3.text)
# str = 'qrscene_9999'
# str2 ='789'
# print(int(str))
# print(int(str2))
# if int(str2):
#     print('***')

# import datetime
#
# time_stamp = datetime.datetime.now()
# print(time_stamp)
# -*- coding: utf-8 -*-

# import datetime
# import random
# #用时间生成一个唯一随机数
#
# nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")#生成当前时间
# randomNum = random.randint(0, 1000) #生成的随机整数n，其中0<=n<=100
# if randomNum < 10:
#     randomNum = str(00)+str(randomNum)
# elif randomNum >= 10 and randomNum < 100:
#     randomNum = str(0) + str(randomNum)
# else:
#     randomNum=randomNum
#
# uniqueNum = str(nowTime)+str(randomNum)
# print(uniqueNum)

#
# str = 'qrscene_9999'
# a = str.split('_')[1]
# print(a)

# import random
#
# while True :
#     a = random.randint(1,10**10)
#     print(a)
#     if a<100:
#         break

# from urllib2 import urlopen
# doc = urlopen("http://hqx3fr.natappfree.cc/entrance/nmsl").read()
# print doc

import time
import urllib2
import json
#
import requests
WECHAT_APPID = "wx1fc6ff9824c795d3"
WECHAT_APPSECRET = "7dcac95970536dc7cf3a44745965b3fa"
access_token = '13_0THlYjRTQ22w1b3bkrUMpWkyduHmUOt3uV-ZgexC-3bpEny6rwhxyaNxHbczPo2e_OdCTjpCqaT_obiG7RDBEIsN75T1X-p2NbyLdr7VIVmeSwoHp7yE9wq7euc9cWJ-tgUwBZDUNJhtT1UQUSXcADAHFK'
from urllib import quote

def get_code():
    appid = WECHAT_APPID
    redirect_url ='http://qqq.ngrok.xiaomiqiu.cn/yanzheng'
    #redirect_url ='http%3a%2f%2fqqq.tcp.xiaomiqiu.cn%2fyanzheng'
    redirect_url = quote(redirect_url)
    print(redirect_url)
    # scope = snsapi_base
    url =  'https://api.weixin.qq.com/sns/oauth2/access_token?appid=wx1fc6ff9824c795d3&secret=7dcac95970536dc7cf3a44745965b3fa&code=0713gJTt1WPe5d02KGTt1EMYTt13gJTV&grant_type=authorization_code'
    #http://open.weixin.qq.com/connect/oauth2/authorize?appid=wx1fc6ff9824c795d3&redirect_uri=http%3a%2f%2fqqq.ngrok.xiaomiqiu.cn%2fyanzheng&response_type=code&scope=snsapi_base&state=23#wechat_redirect
    #http://open.weixin.qq.com/connect/oauth2/authorize?appid=wx1fc6ff9824c795d3&redirect_uri=http%3a%2f%2fmwvguj.natappfree.cc%2fyanzheng&response_type=code&scope=snsapi_base&state=23#wechat_redirect
    # url = "
    # " % (
    # WECHAT_APPID, redirect_url)
    # response = requests.get(url).text
    # print(response)
    response = urllib2.urlopen(url)
    print(response)
    print(type(response))
    code = response.read()
    print(code)
#     return code
# code = '081KF9qk1EyIAm0jOcpk1i71qk1KF9qp'
# 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=wx1fc6ff9824c795d3&secret=7dcac95970536dc7cf3a44745965b3fa&code=061g9Mmg22JPgB0p1qqg2gHPmg2g9Mm6&grant_type=authorization_code'
# get_code()
# access_token = {
#     # "access_token": "",
#     # "update_time": time.time(),
#     # "expires_in": 7200
#     "access_token": "",
#     # "access_token":"12_co30rnzLCsPO1-qF2V_nE7yEr6B__uNYIcdr8AhaaJQvCe5aah-bo94tGWACcXZlTmGfe-dmTdYhbB6cdRJ3UycuiLBcJ6Xh9PmplJTWdxUc6EdLjLE3uB9B771i2w8KsnT94S_4-Wqq8IdQKUCcAAAZJR",
#     "expires_in":7200,
#     "update_time": time.time(),

# }

# def get_access_token():
#
#     # access_token 不存在，或者已过期
#     if not access_token.get('access_token') or \
#             (time.time() - access_token.get('update_time') > access_token.get('expires_in')):
#         # 去获取 access_token
#         url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (WECHAT_APPID, WECHAT_APPSECRET)
#         response = urllib2.urlopen(url)
#         print(type(response))
#         # 读取响应数据
#         data = response.read()
#         # 将响应数据转成字典
#         data = json.loads(data)
#         if "errcode" in data:
#             raise Exception('get access_token failed')
#         else:
#             access_token["access_token"] = data.get("access_token")
#             access_token["update_time"] = time.time()
#             access_token["expires_in"] = data.get("expires_in")
#             print(access_token.get('access_token'))
#             return access_token.get('access_token')
#
#     else:
#         print(access_token.get('access_token'))
#         return access_token.get('access_token')
#
# a  = get_access_token()
# print(a)


# str1 = '{"access_token":"12_eh-RmW3oHFZzj-JaF8xVkBdsZ63Pkjz6xsAYHcMZKky5JKp0aPSuipW_I5nbvm4G3ELW3fcwMM4uh7Hy5ccswqprB3kddAaCrshY72Ej-S8","expires_in":7200,"refresh_token":"12_9a2HBYAmlxbB-zj0e4_iSSgZIjBSMg45fQlY6MbXGBLrkhsJfAFuYN2IRewEioFay6SitqE-cnwOD8_nSW4TyUzDygJgj5nxudaNKz30sdE","openid":"o_Tvk1cVxPUe9oGe-Iex8CYgiXxA","scope":"snsapi_base"}'
# str1 = str1.split(',')
# list1 = list(str1)
# print(len(list1))
# dict1 = {}
# for i in list1:
#     i.split()
# print(list1)

# a = 'qrscene_72061'
# b = a.split('_')[1]
# print(b)
# str = 'abcd'
# if str.startswith('a'):
#     print('hhh')
# print('---')

#http://qqq.ngrok.xiaomiqiu.cn/download_books/o_Tvk1fLh_NOziFidqh3Q3Vckvqk/_7ServiceRecAckFromServer.txt

def get_weip():
    url = 'https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=%s'%access_token
    response =urllib2.urlopen(url)
    print(response)
    response = response.read()

    return response


ip = get_weip()
print('ip:%s'%ip)