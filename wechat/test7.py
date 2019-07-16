# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from wechat.models import User,User2,User3
from pymysql import *
import os
import urllib2

from django.views.decorators.csrf import csrf_exempt


from lib.get_access_token1 import Get_Access_Token
from lib.auto_reply import Reply_Msg,Keyword_Reply,My_Custom_Service


def index(request,scene_id):
    print('进入获取临时二维码的处理函数')
    exa = Get_Access_Token()
    access_token=exa.get_access_token()
    url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s" % access_token
    params = {"expire_seconds": 604800,
              "action_name": "QR_SCENE",
              "action_info": {"scene": {"scene_id": scene_id}}
              }
    response = urllib2.urlopen(url, json.dumps(params))
    data = response.read()
    data_json = json.loads(data)
    """
    ticket	获取的二维码ticket，凭借此ticket可以在有效时间内换取二维码。
    expire_seconds	该二维码有效时间，以秒为单位。 最大不超过2592000（即30天）。
    url	二维码图片解析后的地址，开发者可根据该地址自行生成需要的二维码图片
    """
    ticket = data_json.get('ticket')
    print( 'src="https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s' % ticket)
    return '<img src="https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s">' % ticket


WECHAT_TOKEN = "guowenyuedu"

import hashlib
import json


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def get_parm(request):
    print('进入验证微信发来参数的函数。也是微信服务器绑定的入口。')
    """
       所有的消息都会先进入这个函数进行处理，函数包含两个功能，
       微信接入验证是GET方法，
       微信正常的收发消息是用POST方法。
       """
    if request.method == "GET":
        signature = request.GET.get('signature', None)
        print('signature: %s' %signature)
        timestamp = request.GET.get('timestamp', None)
        print('timestamp: %s' %timestamp)
        nonce = request.GET.get('nonce', None)
        print('nonce: %s' %nonce)
        echostr = request.GET.get('echostr', None)
        print('echostr: %s' %echostr)
        # 服务器配置中的token
        token = WECHAT_TOKEN
        # 把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist])
        hashstr = hashlib.sha1(hashstr).hexdigest()
        if hashstr == signature:
            print(hashstr)
            return HttpResponse(echostr)
        else:
            return HttpResponse("field")
    else:
        print('将要获取post请求的回复信息')
        othercontent = autoreply(request)
        return HttpResponse(othercontent)

    # 微信服务器推送消息是xml的，根据利用ElementTree来解析出的不同xml内容返回不同的回复信息，就实现了基本的自动回复功能了，也可以按照需求用其他的XML解析方法


import xml.etree.ElementTree as ET


def autoreply(request):
    print('2.将要获取post请求的回复信息')
    webData = request.body
    print(type(webData))
    print(webData)
    xmlData = ET.fromstring(webData)
    print(type(xmlData))
    print('xmlData:%s' % xmlData)
    try:

        ToUserName = xmlData.find('ToUserName').text
        print('ToUserName:%s'%ToUserName)
        FromUserName = xmlData.find('FromUserName').text
        print('FromUserName:%s'%FromUserName)
        CreateTime = xmlData.find('CreateTime').text
        print('CreateTime:%s'%CreateTime)
        Event = xmlData.find('Event').text
        print('Event: %s'%Event)
        EventKey = xmlData.find('EventKey').text
        print('EventKey:%s' % EventKey)
        print(type(EventKey))
        if Event == 'subscribe':
            if EventKey:
                print('这种情况是:扫描带参数二维码关注公众号,并绑定终端序列号的处理函数，用户扫码之前尚未关注公众号')
                EventKey = EventKey.split('_')[1]
                print('处理过的EventKey:%s' % EventKey)
                obj = User2.objects.get(scene_id=EventKey)  # 设置唯一scene_id之后就不需要考虑了，直接解析到EventKey去表里查scend_id
                obj.bind = 1
                obj.weid = FromUserName
                obj.save()
                print('完成绑定')

            rep = Reply_Msg()
            res = rep.subscribe(webData)
            return res
        elif Event == 'SCAN':
            print('这种情况是:扫描带参数的二维码去绑定终端序列,用户扫码之前已经关注了公众号')
            if EventKey:
                print('处理过的EventKey:%s' % EventKey)
                obj = User2.objects.get(scene_id=EventKey)  # 设置唯一scene_id之后就不需要考虑了，直接解析到EventKey去表里查scend_id
                obj.bind = 1
                obj.weid = FromUserName
                obj.save()
                return HttpResponse('完成终端阅读器与当前微信号的绑定')
        elif Event =='CLICK' and EventKey =='kugeshinidie':
            print('这种情况是:用户点击二级菜单　我的客服　后，返回指定的客服信息')
            mcs = My_Custom_Service()
            res = mcs.deal(webData)
            return res
        else:
            pass




    except Exception as e :
        print('本次请求的不是事件类型，会接着匹配下面的逻辑')

        print('这是自动回复消息的入口')
        MsgType = xmlData.find('MsgType').text
        if MsgType == 'text':
            Content = xmlData.find('Content').text
            print('Content:%s'%Content)
            krep = Keyword_Reply()
            reply = krep.deal(webData, Content)
            # print('reply:%s'%reply)
            return reply
        else:
            pass
        return '本次请求不是事件类型'


def SendToObook(request):
    print('用户点击二级菜单Send to Obook,网页跳转授权后，code参数在这里接收')
    # print('此时的session[openid]:%s' % request.session.get('openid'))
    FromUserName = get_ACCESS_TOKEN(request)

    nickname = make_nickname(request,FromUserName)
    print('FromUserName:%s'%FromUserName)
    list = []
    objs = User2.objects.filter(weid=FromUserName)
    for obj in objs:
        if obj.bind == '1':
            list.append(obj)
    print(len(list))
    if len(list) >0:
        return render(request,'test0.html',{'FromUserName':FromUserName,'value':nickname})
    else:
        return render(request,'test2.html')


#　weid与终端绑定的视图
import random
def wechat(request):
    print('进入weid与终端绑定的处理函数')
    # 先得到一个唯一的scene_id
    # User.objects.select_for_update().get()
    #如果按需求取唯一id的话，是需要加锁的。如果两个用户同时访问，都去生成当时表中不存在的值的话，逻辑上是存在相同的概率的，不过概率很小。
    scene_id = make_scend_id(request)
    serial_num = request.GET.get('seriNum')
    list = User2.objects.filter(serial=serial_num)

    if len(list) >0:
        for l in list:
            if l.bind == '1':
                index(request,scene_id )
                return HttpResponse('公众号二维码已返回')
            else:
                l.scene_id = scene_id
                index(request, scene_id)
                return HttpResponse('公众号二维码已返回，扫码完成绑定。')

    else:
        User2.objects.create(serial=serial_num, bind=0, scene_id=scene_id)
        index(request,scene_id)
        return HttpResponse('公众号二维码已返回，扫码完成绑定')


#  本地文件上传之后 bookid怎么算
def upload_handle(request):
    print('进入本地文件上传的处理函数')
    FromUserName=request.GET.get('FromUserName')
    # if request.method == 'POST':
    file = request.FILES.get('files')
    if not file:
        list = User.objects.filter(username=FromUserName)

        data = '没有选择文件，请选择想要上传的文件'
        value = get_nickname(request,FromUserName)
        return render(request, 'test1.html', {'value':value,'FromUserName': FromUserName, 'list': list, 'data': data})
    booksname = file.name
    list = User.objects.filter(username=FromUserName, booksname=booksname)
    if len(list) != 0:
        # return HttpResponse('该图书已被推送,请选择其它书籍。')
        list = User.objects.filter(username=FromUserName)

        data = '该图书已被上传,请选择其它书籍。'
        value = get_nickname(request, FromUserName)
        return render(request, 'test1.html', {'value':value,'FromUserName': FromUserName, 'list': list, 'data': data})
    else:
        save_path = '%s/booktest/%s' % (settings.MEDIA_ROOT,FromUserName)
        save_path=save_path.decode()
        print(save_path)
        if not os.path.exists(save_path):
            # print('1111111111111')
            os.makedirs(save_path)
            # print('***********************')
            save_path = save_path + '/' +'%s'%file
            # if os.path.exists(save_path):
            #     data = '该文件已上传，请选择其他文件'
            #     return render(request, 'test6.html', {'data': data})
            # else:
            with open(save_path, 'w+') as f:
            # 遍历获取上传文件内容并写入新文件
                for content in file.chunks():
                    f.write(content)
            with open(save_path, 'r+') as f:
                book_data = f.read()

            md5str = book_data
            m1 = hashlib.md5()
            m1.update(md5str.encode('utf-8'))
            token = m1.hexdigest()
            print('FromUserName:%s' % FromUserName)
            bookid = make_book_id(request)
            url = 'http://qqq.ngrok.xiaomiqiu.cn/download_books/%s/%s'%(FromUserName,booksname)
            User.objects.create(bookid=bookid,username=FromUserName, booksname=booksname, url=url,status=False, md5=token)
            list = User.objects.filter(username=FromUserName)

            data = '文件上传成功'
            value = get_nickname(request,FromUserName)
            return render(request, 'test1.html',{'value': value, 'FromUserName': FromUserName, 'list': list, 'data': data})

            # return HttpResponse('文件上传完成,可以使用阅读器下载后阅读。')
        else:
            save_path = save_path + '/' + '%s' % file
            if os.path.exists(save_path):
                data = '该文件已上传，请选择其他文件'
                value = get_nickname(request, FromUserName)
                return render(request, 'test1.html', {'value':value,'FromUserName':FromUserName,'list':list,'data': data})
            else:
                with open(save_path, 'w+') as f:
                # 遍历获取上传文件内容并写入新文件
                    for content in file.chunks():
                        f.write(content)

                with open(save_path,'r+') as f:
                    book_data = f.read()

                # print(book_data)
                md5str=book_data
                m1 = hashlib.md5()
                m1.update(md5str.encode('utf-8'))
                token = m1.hexdigest()
                print('FromUserName:%s'%FromUserName)
                bookid = make_book_id(request)
                # serial = User2.objects.get(weid=FromUserName).serial
                url = 'http://qqq.ngrok.xiaomiqiu.cn/download_books/%s/%s' % (FromUserName, booksname)
                User.objects.create(bookid=bookid, username=FromUserName, booksname=booksname, url=url, status=False,
                                    md5=token)
                list = User.objects.filter(username=FromUserName)

                data = '文件上传成功'
                value = get_nickname(request, FromUserName)
                return render(request, 'test1.html', {'value':value,'FromUserName':FromUserName,'list':list,'data': data})


#考虑参数怎么传过来，我定义还是微信提供？？？要怎么获取
import pypub
def download_news(request, url, newsname):
    print('进入新闻页下载的处理函数')
    FromUserName=get_ACCESS_TOKEN(request)

    my_first_epub = pypub.Epub(newsname.decode())
    # my_first_epub = pypub.Epub('%s' % user)

    my_first_chapter = pypub.create_chapter_from_url(url)

    my_first_epub.add_chapter(my_first_chapter)

    my_first_epub.create_epub('download/' + FromUserName )
    list = User.objects.filter(username=FromUserName, newsname=newsname)
    print(list)
    # list = []
    if len(list) != 0:
        data = '该新闻已被保存,请选择其它新闻。'
        return render(request, 'test6.html', {'data': data})
    else:
        path = 'download'+'/'+FromUserName+'/'+newsname+'.epub'
        print(path)
        with open(path) as f:
            news_data = f.read()
        md5str = news_data
        #m = hashlib.md5(str(time.clock()).encode('utf-8'))
        #m.hexdigest()
        m1 = hashlib.md5()
        m1.update(md5str.decode('latin-1'))
        token = m1.hexdigest()
        User.objects.create(username=FromUserName, newsname=newsname,status=False,md5=token)
        data = '该新闻页保存成功'
        return render(request, 'test6.html', {'data': data})

#查询该序列号绑定的weid关联的
def select(request,serial):
    print('进入用户已保存的图书的处理函数')
    conn = connect(host='192.168.4.118',
                   user='root',
                   password='mysql',
                   database='kudie',
                   port=3306,
                   charset='utf8')
    # 2. 获取数据库的操作对象　ｃｕｒｓｏｒ
    cur = conn.cursor()
    # 3. sql
    sql = 'select booksname from wechat where username = %s '
    # user = '荷兰'
    list = User2.objects.filter(serial=serial)
    if len(list)>0:
        for obj in list:
            FromUserName=obj.weid
            # 4. 执行ｓｑｌ语句 如果是查询会返回总行数
            user = FromUserName
            ret = cur.execute(sql, user)
            if ret == 0:
                data = '该用户暂时没有已保存的图书'
                return render(request, 'test6.html', {'data': data})
            data = cur.fetchall()
            print(data)
            # data = list(data)
            data = json.dumps(data)
            cur.close()
            conn.close()
            data = data.decode("unicode-escape")
            data = eval(data)
            return render(request, 'tel2.xml', {'data': data}, content_type="text/xml")
    else:
        return HttpResponse('该序列号尚未绑定微信用户，请及时绑定相关微信用户。')





#下载接口如何实现,拿到序列号可以转化成微信用户标识，但是返回来的只是图书名，如何让终端阅读器下载？

def download_books(request,openid,filename):
    print('进入下载图书视图')
    FromUserName=openid
    """获取文件数据　通过返回值返回　如果没有数据Ｎｏｎｅ"""
    if  os.path.exists('%s/booktest/%s/%s' % (settings.MEDIA_ROOT, FromUserName,filename)):
        file = open('%s/booktest/%s/%s' % (settings.MEDIA_ROOT, FromUserName,filename), "rb")
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename= %s' %filename
        return response
    elif os.path.exists('download'+'/'+FromUserName+'/'+filename+'.epub'):
        file = open('download'+'/'+FromUserName+'/'+filename+'.epub', "rb")
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename= %s' % filename
        return response
    else:
        return HttpResponse('文件不存在')

# url  /send_to_obook
# def send_to_obook(request, bookid, booksname,serial, url, status=False):
#     # list = []
#     list = User1.objects.filter(bookid=bookid, booksname=booksname, serial=serial, url=url)
#     print(list)
#     if len(list) != 0:
#         return HttpResponse('该图书已上传')
#     else:
#         conn = connect(host='192.168.4.118',
#                        user='root',
#                        password='mysql',
#                        database='kudie',
#                        port=3306,
#                        charset='utf8')
#         # 2. 获取数据库的操作对象　ｃｕｒｓｏｒ
#         cur = conn.cursor()
#         # 3. sql
#         sql = ' insert into obook(bookid,booksname,serial,url,status) values(%s,%s,%s,%s,%s);'
#         ret = cur.execute(sql, (bookid, booksname, serial, url, status))
#
#         print(ret)
#
#         # 5. 关闭游标对象和连接对象
#         conn.commit()
#         cur.close()
#         conn.close()
#         return HttpResponse('完成推送图书信息的存储')


# url http://search/?serial=终端序列号  获取推送书籍
def search_book(request,serial):
    print('进入用户查询已推送的图书的处理函数')
    obj = User3.objects.filter(serial=serial)
    if len(obj) ==0:
        return HttpResponse('暂且没有推送到该序列号上的图书')
    else:
        for o in obj:
            o.url=User.objects.get(bookid=o.bookid).url
            o.bookname=User.objects.get(bookid=o.bookid).booksname
        return render(request,'tel.xml',{'obj':obj},content_type="text/xml")



#设置授权域名时可以获取到该文件文本

def text(request):
    print('进入用户跳转页面时，网页授权域名的验证的处理函数')
    with open('./MP_verify_dtx7hOzMlkJNtt00.txt') as f:
        data = f.read()
    return HttpResponse(data)



import ConfigParser
# import requests
# from urllib import quote
# def get_code(request):
#     # print('当前字典内容是:%s' % access_token)
#
#     print('进入网页授权时，首先获取code')
#     # appid = WECHAT_APPID
#     redirect_url ='https://www.ngrok.xiaomiqiu.cn/yanzheng'
#     redirect_url = quote(redirect_url)
#     cf = ConfigParser.ConfigParser()
#     cf.read('../conf/app_id.conf')
#     WECHAT_APPID = cf.get('app', 'app_id')
#     url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=snsapi_base&state=23#wechat_redirect" % (
#     WECHAT_APPID, redirect_url)
#     response = requests.get(url).text
#     print(response)



def get_ACCESS_TOKEN(request):
    # print('当前字典内容是:%s' % access_token)

    print('进入网页授权时，拿到code后，获取用户的openid')
    print('----------------')
    if request.method == 'GET':
        code = request.GET.get('code')
        print(code)
        cf = ConfigParser.ConfigParser()
        cf.read('./conf/app_id.conf')
        WECHAT_APPID= cf.get('app', 'app_id')
        WECHAT_APPSECRET = cf.get('app', 'app_secret')
        url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code'%(
            WECHAT_APPID,WECHAT_APPSECRET,code
        )
        response = urllib2.urlopen(url)
        print(response)
        response =response.read()
        print(response)
        print(type(response))
        response = response.split('"')
        print('**************')
        openid = response[-6]
        return openid



def templates(request,template):
    print("进入处理模板的视图")
    # openid = request.session.get('openid')
    # print('此时的session[openid]:%s' % request.session.get('openid'))
    # print(template)
    # print(type(template))
    FromUserName = request.GET.get('FromUserName')
    print('FromUserName:%s'%FromUserName)

    if template == 'test1.html':
        list = User.objects.filter(username=FromUserName)
        value = get_nickname(request,FromUserName)
        return render(request, 'test1.html', {'value':value,'FromUserName': FromUserName, 'list': list})
    elif template == 'books.html':
        #直接在这里处理FromUserName对应的数据库书籍
        list = User.objects.filter().all()
        print(len(list))
        # return render(request,'test9.html',{'list':list})
        value = get_nickname(request,FromUserName)

        return render(request, 'books.html', {'value':value,'list': list,'FromUserName':FromUserName})
    elif template == 'bind.html':
        list = User2.objects.filter(weid=FromUserName,bind=1)
        value = get_nickname(request,FromUserName)

        return render(request,'bind.html',{'value':value,'list': list,'FromUserName':FromUserName})

    elif template == 'detail.html':
        bookid = request.GET.get('bookid')
        # FromUserName = request.GET.get('FromUserName')
        obj = User.objects.get(bookid=bookid)
        value = get_nickname(request,FromUserName)
        return render(request, 'detail.html', {'value':value,'obj': obj, 'FromUserName': FromUserName})
    else:
        bookid = request.GET.get('bookid')
        obj = User.objects.get(bookid=bookid)
        value = get_nickname(request,FromUserName)

        return render(request, 'test10.html', {'value':value,'obj':obj,'openid':FromUserName})


#获取普通的access_token，开头有获取
# def token(request):
#     url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
#     WECHAT_APPID, WECHAT_APPSECRET)
#     result = urllib2.urlopen(url).read()
#     access_token = json.loads(result).get('access_token')
#     print 'access_token===%s' % access_token
#     # print(access_token)
#     return access_token

#创建自定义菜单
# def createMenu(request,access_token):
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
#     result=result
#     print(result)


def make_scend_id(request):
    print('进入获取唯一场景值的处理函数')
    while True:
        randomNum = random.randint(0, 10 ** 10)  # 生成的随机整数n，其中0<=n<=100
        randomNum=str(randomNum)
        list0 = User2.objects.filter(scene_id=randomNum)
        if len(list0) == 0:
            scene_id = randomNum
            return scene_id


def make_book_id(request):
    print('进入获取唯一bookid的处理函数')
    while True:
        randomNum1 = random.randint(0,10*4)
        randomNum2 = random.randint(0,10*4)
        randomstr=str(randomNum1)+str(randomNum2)
        idlist=User.objects.filter(bookid=randomstr)
        if len(idlist) ==0:
            bookid = randomstr
            return bookid
#显示该微信绑定的终端列表
def zhongduan(request):
    print('进入显示终端序列号的视图')
    bookid = request.GET.get('bookid')
    print('bookid:%s'%bookid)
    openid = request.GET.get('openid')
    print('openid:%s'%openid)
    list = User2.objects.filter(weid=openid,bind=1)
    obj = User.objects.get(bookid=bookid)

    if len(list) ==0:
        data = '请先绑定终端，之后才可以使用该功能'
        return render(request, 'test8.html', {'data': data})
    else:
        return render(request,'show_serial.html',{'list':list,'obj':obj})

#处理推书.  需要另外建一张推书表，与之前的上传图书表区分。拿到的书名直接写入表中，就是准备推书的书单，终端不定时请求，返回图书下载地址。
def tuishu(request):
    print('进入处理推送图书功能的函数')
    bookid = request.GET.get('bookid')
    serial=request.GET.get('serial')
    if len(User3.objects.filter(bookid=bookid,serial=serial)) != 0:
        data = '该书籍已被推送，请选择其他书籍'
        return render(request, 'test8.html', {'data': data})
    else:
        User3.objects.create(bookid=bookid,serial=serial)
        data = '该图书已完成推送'
        return render(request, 'test8.html', {'data': data})

import oss2
def delete(request):
    print('进入删除个人书库的书籍')
    print('data:%s'%request.body)
    bookid = request.POST.get('bookid')
    print('bookid:%s'%bookid)
    openid = request.POST.get('openid')

    cf = ConfigParser.ConfigParser()
    cf.read('./conf/oss.conf')
    Bucket = cf.get('oss', 'Bucket')
    EndPoint = cf.get('oss', 'EndPoint')
    id = cf.get('oss', 'id')
    secret = cf.get('oss', 'secret')
    # cf.write(open("./conf/oss.conf", "w"))
    bucket = oss2.Bucket(oss2.Auth(id, secret), EndPoint, Bucket)
    bookname = User.objects.get(bookid=bookid).booksname

    key = (openid + '_' + bookname)
    key = key.encode('utf-8')

    bucket.delete_object(key)

    User.objects.get(username=openid, bookid=bookid).delete()
    return JsonResponse({'res':1})


@csrf_exempt
def cancel(request):
    print('进入取消绑定的视图函数')
    data = request.body
    print('data:%s'%data)
    FromUserName = request.POST.get('FromUserName')
    print('FromUserName:%s'%FromUserName)
    serial = request.POST.get('serial')
    User2.objects.get(serial=serial).delete()
    return JsonResponse({'res':1})



"""
nickname改变该如何处理？之前写入文件的值就无效了。
考虑到拿nickname的接口每天有请求上限，用户每次点菜单的时候写入文件，之后再用直接读文件。
"""
import fcntl
def make_nickname(request,FromUserName):
    f = open('./conf/nk.conf')
    fcntl.flock(f.fileno(), fcntl.LOCK_EX)
    cf = ConfigParser.ConfigParser()
    cf.read('./conf/nk.conf')
    gat = Get_Access_Token()
    token = gat.get_access_token()
    url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN' % (token, FromUserName)
    response = urllib2.urlopen(url)
    data = response.read()
    print('data:%s'%data)
    nickname = data.split('"')[9]
    print('nickname:%s'%nickname)
    if FromUserName in cf.sections():
        cf.set(FromUserName,'nickname',nickname)
        cf.write(open("./conf/nk.conf", "w"))
    else:
        cf.add_section(FromUserName)
        cf.set(FromUserName, 'nickname',nickname )
        cf.write(open("./conf/nk.conf", "w"))
    fcntl.flock(f, fcntl.LOCK_UN)
    return nickname

def get_nickname(request,FromUserName):
    cf = ConfigParser.ConfigParser()
    cf.read('./conf/nk.conf')
    value = cf.get(FromUserName, 'nickname')
    return value

import urllib

@csrf_exempt
def deal(request):
    print('进入到ajax的视图')
    FromUserName = request.POST.get('FromUserName')
    FromUserName = FromUserName.encode("utf-8")

    filename = request.POST.get('filename')
    filename = filename.encode("utf-8")

    FileName=urllib.quote(filename)

    fileString = request.POST.get('fileString')
    # print(type(fileString))
    fileString = fileString.encode("utf-8")

    bookid = make_book_id(request)

    cf = ConfigParser.ConfigParser()
    cf.read('./conf/oss.conf')
    Bucket = cf.get('oss','Bucket')
    EndPoint = cf.get('oss','EndPoint')
    id = cf.get('oss','id')
    secret = cf.get('oss','secret')
    # cf.write(open("./conf/oss.conf", "w"))
    bucket = oss2.Bucket(oss2.Auth(id, secret), EndPoint, Bucket)
    print('bucket:%s' % bucket)
    encode_md5,md5_val = calculate_data_md5(request,fileString)
    print(encode_md5,md5_val)
    bucket.put_object(FromUserName+'_'+filename, fileString, headers={'Content-MD5': encode_md5})

    url ='https://%s.%s/%s_%s'%(Bucket,EndPoint,FromUserName,FileName)
    #也就是说,会存在用户名，文件名相同的行
    li = User.objects.filter(username=FromUserName,booksname=filename,md5=md5_val)
    print(len(li))
    if len(li)>0:
        #如果存在同一用户与同一文件的数据，就删掉，之后在表中加一条新的数据。因为oss存储是：如果同一用户上传同名文件，则覆盖，因此表中的之前文件的数据就没有存在的意义，创建新文件的数据即可。也就避免了用户名与文件名都相同的数据。
        User.objects.filter(username=FromUserName, booksname=filename).delete()
        User.objects.create(bookid=bookid, username=FromUserName, booksname=filename, url=url, md5=md5_val)
        return JsonResponse({'res':1})
    else:
        User.objects.create(bookid=bookid, username=FromUserName, booksname=filename, url=url, md5=md5_val)
        return JsonResponse({'res': 1})

import base64
def calculate_data_md5(request,data):
    """计算数据的MD5
    :param data: 数据
    :return MD5值
    """
    md5 = hashlib.md5()
    md5.update(data)
    return base64.b64encode(md5.digest()),md5.hexdigest()