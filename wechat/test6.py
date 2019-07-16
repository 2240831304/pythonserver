# -*- coding:utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# import urllib2
# import json
#
#
#
#
# WECHAT_APPID = "wx1fc6ff9824c795d3"
# WECHAT_APPSECRET = "7dcac95970536dc7cf3a44745965b3fa"
#
#
# def token():
#     url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
#     WECHAT_APPID, WECHAT_APPSECRET)
#     result = urllib2.urlopen(url).read()
#     access_token = json.loads(result).get('access_token')
#     print 'access_token===%s' % access_token
#     print(access_token)
#     return access_token
#
#
# def createMenu(access_token):
#     url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % access_token
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
#
#     # data = json.loads(data)
#     # data = urllib.urlencode(data)
#     req = urllib2.Request(url)
#     req.add_header('Content-Type', 'application/json')
#     req.add_header('encoding', 'utf-8')
#     response = urllib2.urlopen(req, json.dumps(data, ensure_ascii=False))
#     result = response.read()
#     print(result)
#
# f1 = token()
# createMenu(f1)


#import random

# string = '一个当当阅读'
# a = string.find('阅读器')
# print(a)
# '''
#      if Event =='subscribe':
#             rep = Reply_Msg()
#             rep.subscribe()
#             if EventKey:
#                 EventKey = EventKey.split('_')[1]
#                 print('处理过的EventKey:%s' % EventKey)
#                 obj = User2.objects.get(scene_id=EventKey)  # 设置唯一scene_id之后就不需要考虑了，直接解析到EventKey去表里查scend_id
#                 # print('serial_num:%s' % EventKey)
#                 # scene_id = obj.scene_id
#                 # print(scene_id + '***')
#                 # if EventKey.startswith('q'):  # 用户未关注，eventkey 是qrscene_9999；反之则是scene_id的值。
#                 #     print('----')
#                 #
#                 #     if str(EventKey) == str(scene_id):
#                 obj.bind = 1
#                 obj.weid = FromUserName
#                 obj.save()
#                 return HttpResponse('完成终端阅读器与当前微信号的绑定')
# '''
#
#
# """
# def autoreply(request):
#     print('2.将要获取post请求的回复信息')
#     webData = request.body
#     print(type(webData))
#     print(webData)
#     xmlData = ET.fromstring(webData)
#     print(type(xmlData))
#     print('xmlData:%s' % xmlData)
#     try:
#
#         ToUserName = xmlData.find('ToUserName').text
#         print('ToUserName:%s'%ToUserName)
#         # global  FromUserName
#         FromUserName = xmlData.find('FromUserName').text
#         print('FromUserName:%s'%FromUserName)
#         CreateTime = xmlData.find('CreateTime').text
#         print('CreateTime:%s'%CreateTime)
#         Event = xmlData.find('Event').text
#         print('Event: %s'%Event)
#         EventKey = xmlData.find('EventKey').text
#         print('EventKey:%s' % EventKey)
#         print(type(EventKey))
#         # Ticket = xmlData.find('Ticket').text
#         # print('Ticket:%s' %Ticket)
#         # MsgId = xmlData.find('MsgId').text
#         # print('MsgId:%s'%MsgId)
#
#
#         # toUser = FromUserName
#         # fromUser = ToUserName
#         # print(FromUserName)
#         # if msg_type == 'text':
#         #     content = "您好,欢迎来到Python大学习!希望我们可以一起进步!"
#         #     replyMsg = TextMsg(toUser, fromUser, content)
#         #     print "成功了!!!!!!!!!!!!!!!!!!!"
#         #     print replyMsg
#         #     return replyMsg.send()
#         #
#         # elif msg_type == 'image':
#         #     content = "图片已收到,谢谢"
#         #     replyMsg = TextMsg(toUser, fromUser, content)
#         #     return replyMsg.send()
#         # elif msg_type == 'voice':
#         #     content = "语音已收到,谢谢"
#         #     replyMsg = TextMsg(toUser, fromUser, content)
#         #     return replyMsg.send()
#         # elif msg_type == 'video':
#         #     content = "视频已收到,谢谢"
#         #     replyMsg = TextMsg(toUser, fromUser, content)
#         #     return replyMsg.send()
#         # elif msg_type == 'shortvideo':
#         #     content = "小视频已收到,谢谢"
#         #     replyMsg = TextMsg(toUser, fromUser, content)
#         #     return replyMsg.send()
#         # elif msg_type == 'location':
#         #     content = "位置已收到,谢谢"
#         #     replyMsg = TextMsg(toUser, fromUser, content)
#         #     return replyMsg.send()
#         # else:
#         #     msg_type == 'link'
#         #     content = "链接已收到,谢谢"
#         #     replyMsg = TextMsg(toUser, fromUser, content)
#         #     return replyMsg.send()
#
#
#     except Exception as e :
#         return '获取不到完整数据'
#     if Event == 'subscribe':
#         EventKey = EventKey.split('_')[1]
#         print('处理过的EventKey:%s' % EventKey)
#         obj = User2.objects.get(scene_id=EventKey)# 设置唯一scene_id之后就不需要考虑了，直接解析到EventKey去表里查scend_id
#         # print('serial_num:%s' % EventKey)
#         # scene_id = obj.scene_id
#         # print(scene_id + '***')
#         # if EventKey.startswith('q'):  # 用户未关注，eventkey 是qrscene_9999；反之则是scene_id的值。
#         #     print('----')
#         #
#         #     if str(EventKey) == str(scene_id):
#         obj.bind = 1
#         obj.weid = FromUserName
#         obj.save()
#         return HttpResponse('完成终端阅读器与当前微信号的绑定')
#
#     elif Event == 'SCAN':
#         obj = User2.objects.get(scene_id=EventKey)
#         obj.bind = 1
#         obj.weid = FromUserName
#         obj.save()
#         print('*****')
#         return HttpResponse('完成终端阅读器与当前微信号的绑定')
#
#
#     else:
#         pass
#
# """


# import ConfigParser
# cp = ConfigParser.ConfigParser()
# cp.read('../conf/work.cfg')
# section = cp.sections()
# # print(section)
# # print(cp.options('test7'))
# # a = cp.items('test7')
# # print(a)
# # print(type(a))
# for s in section:
#     print(s)
#     print(cp.options(s))
#     ci = cp.items(s)
#     print(ci)
#     print(type(ci))
#     for c in ci:
#         print(c[0])
#         print(c[1])

import urllib2

# token = '13_DVEgOg19LJk8cLkmc-WcMzfRfNPYgWFH5xb8IfePYeAI0nIklmyQzS4O_8U7cyattJkMw4kp4lhbVNhflFC-wbOGZvKWqoemvC3MwXEh2VWc4DVCtZotUX9s3sA_hCWCYHKcOQEbOakY0TZ0NTYjABARXC'
# # openid = 'o_Tvk1cVxPUe9oGe-Iex8CYgiXxA'
# openid = 'o_Tvk1fLh_NOziFidqh3Q3Vckvqk'
# url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN'%(token,openid)
#
# response = urllib2.urlopen(url)
# print(response)
# print(type(response))
# data = response.read()
# print(data)
# print(type(data))
# string = data
# # string = '{"subscribe":1,"openid":"o_Tvk1cVxPUe9oGe-Iex8CYgiXxA","nickname":"卢传","sex":1,"language":"zh_CN","city":"焦作","province":"河南","country":"中国","headimgurl":"http:\/\/thirdwx.qlogo.cn\/mmopen\/BRe3yTTZvpzkaNAXlYmgEPl5CcsE8zRSaugO9Hia64dM68Y4BZsiaIsy1mHBSVWo6IBlryJks3T5OmeYjKs7mpXJYQlVdBkb6W\/132","subscribe_time":1533111484,"remark":"","groupid":0,"tagid_list":[],"subscribe_scene":"ADD_SCENE_SEARCH","qr_scene":0,"qr_scene_str":""}'
# list = string.split('"')
# print(list)
# print(list[9])
# print(type(list[9]))
token = '15_Z_wAbpa9r6Rh5-PP8Lmm4qH7XXHhrOJ3RFzWUHw3axNPWgybZ0Fe-DVzbVVCmjvmxL29VR7qvDRzqqLfIBONnj-u37Wh-NZ_PXNJdJr7E28vja155JR8FbVfSkiwYxCLdV3LZ5Ld34pNZU5cBUVbACATMN'
url = 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=%s&type=jsapi'% token
response = urllib2.urlopen(url)
print(response)
print(type(response))
data = response.read()
print(data)
data = data.split('"')[9]
print(data)
print(type(data))