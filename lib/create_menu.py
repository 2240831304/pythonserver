# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import json


# token = '13_I5Gqqlbr5Na8_XvPi5xbgbYniNUW8cEQRQhpwlk2ZNotKQ-OwElvIpqXXDd84g3xWxIv3-cYRlzBqG4KkSXyqOkHLdoK-diFDyPyZqdIGJkhwwNiAAvKPkUJPaoFL5wmPh7qyJLqXP7xuO8XOGFgABABTS'
def createMenu(access_token):
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % access_token
#     data = {
#      "button":[
#       {
#            "name":"书单",
#            "sub_button":[
#             {
#                "type":"view",
#                "name":"每周书单",
#                "url":"http://mp.weixin.qq.com/mp/homepage?__biz=MzU4ODUwNDU3Mw==&hid=3&sn=3ad33bfb9399e37d89858a02d7969e99&scene=18#wechat_redirect"
#             },
#             {
#                "type":"view",
#                "name":"福利下载",
#                "url":"http://mp.weixin.qq.com/mp/homepage?__biz=MzU4ODUwNDU3Mw==&hid=2&sn=8efa5222f2920cab34ad4342a84238f8&scene=18#wechat_redirect"
#             }]
#              },
# 	    {
#            "name":"产品",
#            "sub_button":[
#             {
#                "type":"view",
#                "name":"玩机技巧",
#                "url":"http://mp.weixin.qq.com/mp/homepage?__biz=MzU4ODUwNDU3Mw==&hid=4&sn=f711adbdfdfa08cac212af4fa4d68ea3&scene=18#wechat_redirect"
#             },
#             {
#                "type":"view",
#                "name":"产品评测",
#                "url":"http://mp.weixin.qq.com/mp/homepage?__biz=MzU4ODUwNDU3Mw==&hid=5&sn=b310b2c8e6231d2e6722565b70e1289d&scene=18#wechat_redirect"
#             },
# 			{
#                "type":"view",
#                "name":"产品视频",
#                "url":"https://v.qq.com/x/page/l070929x3w1.html"
#             },
# 			{
#                "type":"view",
#                "name":"官方网店",
#                 "url":"https://shop.m.jd.com/?shopId=1000100762"
#             },
# 		    {
#             "type":"view",
#            "name":"Send to Obook",
#             "url":"https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx1fc6ff9824c795d3&redirect_uri=http%3a%2f%2fqqq.ngrok.xiaomiqiu.cn%2fyanzheng&response_type=code&scope=snsapi_base&state=23#wechat_redirect"
#
# 		    }]
#                 },
#             {
#            "name":"服务",
#            "sub_button":[
#             {
#                "type":"view",
#                "name":"只换不修",
#                "url":"https://www.wjx.top/jq/26896448.aspx"
#             },
#             {
#                "type":"view",
#                "name":"碎屏换",
#                "url":"http://mp.weixin.qq.com/s?__biz=MzU4ODUwNDU3Mw==&mid=100000329&idx=1&sn=9c3f1b9e898362c62821f6ea30ea51e7&chksm=7dda8edb4aad07cd285bd41bf54347beadf3122c74c4824d9c6272ea4af69ad3f46b4b4dd7f2&scene=18#wechat_redirect"
#             },
# 			{
#                "type":"view",
#                "name":"常见问题",
#                "url":"http://mp.weixin.qq.com/s?__biz=MzU4ODUwNDU3Mw==&mid=100000064&idx=1&sn=1feea115c5810980b27a0b160f5c06ab&chksm=7dda8dd24aad04c418ad2792f81777f8064b262233cd67ac914ca49fe606be695d17827310f7&scene=18#wechat_redirect"
#             },
# 			{
#                "type":"click",
#                "name":"我的客服",
#                 "key":"kugeshinidie"
#             },
#                         {
#                 "type":"view",
#                 "name":"升级提示",
#                 "url":"http://mp.weixin.qq.com/s?__biz=MzU4ODUwNDU3Mw==&mid=2247484490&idx=2&sn=b6537a19776aace486c7d38fc0f9d48c&chksm=fdda88d8caad01ce8676f1713edf6a96ce8b7f7ae5f45a40a111334f5851606952be1ffc8cea&scene=18#wechat_redirect"
#               }]
# 	    }
#
# 	]
# }

    # data = json.loads(data)
    # data = urllib.urlencode(data)
    with open('./conf/menu.json','r') as f:
        data = f.read()

    print(data)
    print(type(data))
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    req.add_header('encoding', 'utf-8')
    response = urllib2.urlopen(req, data)
    result = response.read()
    result=result
    print(result)

# createMenu(token)