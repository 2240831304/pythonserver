# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import time
import urllib2
import json
import ConfigParser
import time
import fcntl


# WECHAT_APPID = "wx1fc6ff9824c795d3"
# WECHAT_APPSECRET = "7dcac95970536dc7cf3a44745965b3fa"

# access_token = {
#     # "access_token": "",
#     # "update_time": time.time(),
#     # "expires_in": 7200
#     "access_token": "",
#     # "access_token":"12_co30rnzLCsPO1-qF2V_nE7yEr6B__uNYIcdr8AhaaJQvCe5aah-bo94tGWACcXZlTmGfe-dmTdYhbB6cdRJ3UycuiLBcJ6Xh9PmplJTWdxUc6EdLjLE3uB9B771i2w8KsnT94S_4-Wqq8IdQKUCcAAAZJR",
#     "expires_in":7200,
#     "update_time": time.time(),

# }


class Get_Access_Token(object):
    def __init__(self):
        self.f = open('/var/www/jiekou/conf/access_token.conf')
        # self.f = open('./conf/access_token.conf')
        # print('未加锁')
        #对文件加锁处理
        fcntl.flock(self.f.fileno(), fcntl.LOCK_EX)  # 加锁
        # print('已加锁')
        cf = ConfigParser.ConfigParser()
        cf.read('/var/www/jiekou/conf/app_id.conf')
        # self.f = open('./conf/access_token.conf')
        self.app_id = cf.get('app', 'app_id')
        self.app_secret = cf.get('app', 'app_secret')

    def get_access_token(self):
        print('进入到获取普通access_token的处理函数')
        # access_token 不存在，或者已过期
        cc = ConfigParser.ConfigParser()
        cc.read('/var/www/jiekou/conf/access_token.conf')
        # self.f = open('./conf/access_token.conf')

        token_value = cc.get('token','token_access_token')
        create_time_value = cc.get('token','token_create_time')
        expires_in_value = cc.get('token','token_expires_in')
        if token_value == '' or \
                (time.time() - float(create_time_value) > int(expires_in_value)):
            # 去获取 access_token
            url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (
            self.app_id,self.app_secret)
            response = urllib2.urlopen(url)
            print(type(response))
            # 读取响应数据
            data = response.read()
            # 将响应数据转成字典
            data = json.loads(data)
            if "errcode" in data:
                raise Exception('get access_token failed')
            else:
                access_token = data.get("access_token")
                # print('现在的access_token:%s' % access_token.get('access_token'))
                update_time = time.time()
                # access_token["expires_in"] = data.get("expires_in")
                # print('当前字典内容是:%s' % access_token)

                # return access_token.get('access_token')

                cc.set('token','token_access_token',access_token)
                cc.set('token','token_create_time',update_time)
                cc.write(open("/var/www/jiekou/conf/access_token.conf", "w"))
                # self.f = open('./conf/access_token.conf')
                print('success')
                # time.sleep(10)
                #手动释放文件锁
                fcntl.flock(self.f, fcntl.LOCK_UN)
                print('已释放文件锁，其他进程可以对该文件加锁')
                # time.sleep(10)

                return  access_token
        else:
            # token_value = cc.get('token', 'token_access_token')
            print('还没过期')
            print('当前的token:%s'%cc.get('token','token_access_token'))
            return token_value


# gat = Get_Access_Token()
# token = gat.get_access_token()
# print(token)
