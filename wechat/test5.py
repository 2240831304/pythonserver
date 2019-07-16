# coding:utf-8
#
# import time
# import urllib2
# import json
#
# WECHAT_APPID = "wx1fc6ff9824c795d3"
# WECHAT_APPSECRET = "7dcac95970536dc7cf3a44745965b3fa"
#
#
#
#
# access_token = {
#     # "access_token": "",
#     # "update_time": time.time(),
#     # "expires_in": 7200
#     # "access_token": "",
#     "access_token":"",
#     "expires_in":7200,
#     "update_time": time.time(),
#
# }
#
#
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
#             return access_token.get('access_token')
#     else:
#         return access_token.get('access_token')
#
#
#
#
# def index(scene_id):
#     access_token = get_access_token()
#     url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s" % access_token
#     params = {"expire_seconds": 604800,
#               "action_name": "QR_SCENE",
#               "action_info": {"scene": {"scene_id": scene_id}}
#               }
#     response = urllib2.urlopen(url, json.dumps(params))
#     data = response.read()
#     data_json = json.loads(data)
#     """
#     ticket	获取的二维码ticket，凭借此ticket可以在有效时间内换取二维码。
#     expire_seconds	该二维码有效时间，以秒为单位。 最大不超过2592000（即30天）。
#     url	二维码图片解析后的地址，开发者可根据该地址自行生成需要的二维码图片
#     """
#     ticket = data_json.get('ticket')
#     print data_json.get('expire_seconds')
#     print data_json.get('url')
#     print('src="https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s' % ticket)
#     return '<img src="https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s">' % ticket
#
#
# if __name__ == '__main__':
#     index(999)


# import random
# def make_scend_id():
#     while True:
#         randomNum = random.randint(0, 10 **2)  # 生成的随机整数n，其中0<=n<=100
#         print(type(randomNum))
#         print(randomNum)
#         # list0 = User2.objects.filter(scene_id=randomNum)
#         if randomNum == 36:
#             # uniqueNum = str(randomNum)
#             # scene_id = uniqueNum
#             return randomNum
#
# print(make_scend_id())

# import time, hashlib
#
#
# def create_id():
#     m = hashlib.md5()
#     m.update(bytes(str(time.clock()), encoding='utf-8'))
#     return m.hexdigest()
#
#
# if __name__ == '__main__':
#     print(type(create_id()))
#     print(create_id())
#     print(create_id())
#     print(create_id())

# import uuid
#
#
# def create_uid():
#
#     return str(uuid.uuid1())
#
#
# if __name__ == '__main__':
#     print(type(uuid.uuid1()))
#     print(type(create_uid()))
#
#     print(create_uid())

    # print(create_uid())
    # print(create_uid())

# https://api.weixin.qq.com/sns/userinfo?access_token=13_zXSgXedIGrnrtuiBEvOWKmy3xEzOAywc0cn_4xghB6tCjrpi_UWuJuKsrixOEpHzqNPjpoI_a-SJBbRo2aahymqGzE0HUQ3mSvNLsds5Tq2bf6uKHwutyL9Rkdyze6FKVqZjB3E3rhGgxhn4XHEcABADNK
# &o_Tvk1SsLOCt9tyvbb-5nC2pAdP4&lang=zh_CN
#
# 13_bL7QykWUA5olQwtH7OuNJClpOwrbOGJcOZ2iX_A7nrQE1PJVr5YAqGnaMxkoQio8N0zMMj5b80Yo7HfZ7D7M67R5h8jqAI4vTLspkAuvAUwXJpwx-ZKAM9G75IyPSKmTq4d3nkpZ8qi1vPMABEMfABA
# 13_bL7QykWUA5olQwtH7OuNJClpOwrbOGJcOZ2iX_A7nrQE1PJVr5YAqGnaMxkoQio8N0zMMj5b80Yo7HfZ7D7M67R5h8jqAI4vTLspkAuvAUwXJpwx-ZKAM9G75IyPSKmTq4d3nkpZABEMfABAWZH
# 13_zXSgXedIGrnrtuiBEvOWKmy3xEzOAywc0cn_4xghB6tCjrpi_UWuJuKsrixOEpHzqNPjpoI_a-SJBbRo2aahymqGzE0HUQ3mSvNLsds5Tq2bf6uKHwutyL9Rkdyze6FKVqZjB3E3rhGgxhn4XHEcABADNK

import sys
import ConfigParser
import time
cc = ConfigParser.ConfigParser()
# with open('../conf/auto_reply.conf','r',encoding = 'utf-8') as f :
# cc.read('../conf/test.conf')
cc.read('../conf/auto_reply.conf')
# value = cc.get('token', 'token_access_token')
value = cc.get('vip','content')
print('value:%s'%value)
print(type(value))
value1 = cc.get('subscribe','content')
print(type(value1))
print('value1:%s'%value1)
# value2 = cc.get('token','token_expires_in')
# print(type(value2))
# print('value2:%s'%value2)
print('***')
# cc.set('token','token_access_token','1931-09-18')
# time = time.time()
# print(type(time))
# print('time:%s'%time)
# # if time - float(value1) >float(value2):
# if time - float(value1) >int('10'):
#     cc.set('token','token_access_token','1931-09-29')
#     cc.set('token','token_create_time',time)
#
# cc.write(open("../conf/access_token.conf", "w"))
# with open('../conf/test.conf','w') as f:v
#     f.write('')
#
# cf = ConfigParser.ConfigParser()
# cf.read('../conf/test.conf')
# secs = cf.sections()
# print(secs)
# opts = cf.options('db')
# print(opts)
# ksv = cf.items('db')
# print(ksv)
# val = cf.get('db','today')
# print(val)
# val1 = cf.get('time','beijing')
# print(val1)
# cf.set('db','today','friday')
# cf.set('time','beijing','haidian')
# cf.write(open('../conf/test.conf','w'))