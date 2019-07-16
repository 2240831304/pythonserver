# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


from django.http.response import HttpResponse
from wechatpy import parse_message, create_reply
import ConfigParser
#关注后的自动回复信息
class Reply_Msg(object):
    #直接定义如何返回信息即可
    def subscribe(self,webData):
        print('进入到组织回复用户关注后的信息')
        cc = ConfigParser.ConfigParser()
        cc.read('/var/www/jiekou/conf/auto_reply.conf')
        value = cc.get('subscribe', 'content')
        tx = Text()
        reply = tx.repay_data(webData, value)

        response = HttpResponse(reply, content_type="application/xml")
        return response


#关键字回复
class Keyword_Reply(object):

    '''
    根据捕获到的用户发送的消息关键字，去分析，返回相应的自动回复信息
    '''
    def deal(self,webData,content):
        print('进入处理自动回复的函数')
        cc = ConfigParser.ConfigParser()
        cc.read('/var/www/jiekou/conf/auto_reply.conf')
        msg = parse_message(webData)
        if msg.type == 'text':
            # if content.find('碎') != -1 or content.find('保险') != -1:
            #
            #     title = cc.get('broken', 'title')
            #     description = cc.get('broken', 'description')
            #     picurl = cc.get('broken', 'picurl')
            #     url = cc.get('broken', 'url')
            #     tm = NewsMsg()
            #     reply = tm.repay_data(content,title,description,picurl,url)
            #     response = HttpResponse(reply, content_type="application/xml")
            #     print('response:%s' % response)
            #     return response
            #
            # elif content.find('当当VIP') != -1 or \
            #     content.find('VIP') != -1 or \
            #     content.find('vip') != -1 or \
            #     content.find('当当vip') != -1 :
            #
            #     value = cc.get('vip', 'content')
            #     print('自动回复--vip')
            #     tx = Text()
            #     reply = tx.repay_data(webData, value)
            #     # print('完成处理关键字--vip')
            #     # return reply
            #
            # elif content.find('售后') != -1:
            #     # reply = create_reply('这是售后', msg)
            #     print('进入处理售后消息的函数')
            #
            #     title = cc.get('customer_service', 'title')
            #     description = cc.get('customer_service', 'description')
            #     picurl = cc.get('customer_service', 'picurl')
            #     url = cc.get('customer_service', 'url')
            #     tm = NewsMsg()
            #     reply = tm.repay_data(content,title,description,picurl,url)
            #     # reply = create_reply(reply,msg)
            #     response = HttpResponse(reply,content_type="application/xml")
            #     print('response:%s'%response)
            #     return response
            # elif content.find('热门书籍') != -1 :
            #
            #     value = cc.get('hot_books', 'content')
            #     tx = Text()
            #     reply = tx.repay_data(webData, value)
            #
            # # elif text.find('免费') != -1 or text.find('免费书') != -1 or text.find('免费电子书') != -1:
            # #     reply = create_reply('这是免费书消息', msg)
            #
            # elif content.find('开不了机') != -1 or content.find('进水') != -1 or \
            #         content.find('坏了') != -1 or content.find('故障') != -1 or \
            #         content.find('问题') != -1 or content.find('闪屏') != -1:
            #     print('进入故障的处理函数')
            #
            #     title = cc.get('usual_problem', 'title')
            #     description = cc.get('usual_problem', 'description')
            #     picurl = cc.get('usual_problem', 'picurl')
            #     url = cc.get('usual_problem', 'url')
            #     tm = NewsMsg()
            #     reply = tm.repay_data(content, title, description, picurl, url)
            #     # reply = create_reply(reply,msg)
            #     response = HttpResponse(reply, content_type="application/xml")
            #     print('response:%s' % response)
            #     return response
            #
            # elif content.find('书') != -1 or content.find('推荐') != -1 :
            #
            #     title = cc.get('book_list', 'title')
            #     description = cc.get('book_list', 'description')
            #     picurl = cc.get('book_list', 'picurl')
            #     url = cc.get('book_list', 'url')
            #     tm = NewsMsg()
            #     reply = tm.repay_data(content, title, description, picurl, url)
            #     # reply = create_reply(reply,msg)
            #     response = HttpResponse(reply, content_type="application/xml")
            #     print('response:%s' % response)
            #     return response
            # elif content.find('你好') != -1 or content.find('在吗') != -1 or content.find('嗨') != -1:
            #
            #     value = cc.get('hello', 'content')
            #     tx = Text()
            #     reply = tx.repay_data(webData, value)
            #
            # elif content.find('DDYDQ') != -1:
            #
            #     value = cc.get('DDYDQ', 'content')
            #     tx = Text()
            #     reply = tx.repay_data(webData, value)
            # elif content.find('当当阅读器') != -1:
            #
            #     value = cc.get('obook', 'content')
            #     tx = Text()
            #     reply = tx.repay_data(webData, value)
            # else:#识别不了的统一回复　收到消息后的回复
            #
            #     value = cc.get('others', 'content')
            #     tx = Text()
            #     reply = tx.repay_data(webData, value)
            sections = cc.get('keyword','type')
            print(sections)
            sections = sections.split(',')
            print(sections)
            for s in sections:
                string = cc.get('keyword',s)
                print('string:%s'%string)
                if string.find(content) != -1:
                    type = cc.get(s,'type')
                    if type =='news':
                        print('处理news')
                        title = cc.get(s, 'title')
                        description = cc.get(s, 'description')
                        picurl = cc.get(s, 'picurl')
                        url = cc.get(s, 'url')
                        tm = NewsMsg()
                        reply = tm.repay_data(webData,title,description,picurl,url)
                        response = HttpResponse(reply,content_type="application/xml")
                        print('response:%s'%response)
                        return response

                    elif type =='text':
                        print('处理文本')
                        value = cc.get(s, 'content')
                        tx = Text()
                        reply = tx.repay_data(webData, value)
                        response = HttpResponse(reply, content_type="application/xml")
                        print('response:%s' % response)
                        return response
                    elif type == 'image':
                        media_id = cc.get(s,'media_id')
                        im = ImgMsg()
                        reply = im.repay_data(webData,media_id)
                        response = HttpResponse(reply,content_type="application/xml")
                        return response
                    else:
                        pass


            print('进入others处理函数')
            value = cc.get('others','content')
            tx = Text()
            reply = tx.repay_data(webData, value)

            response = HttpResponse(reply, content_type="application/xml")
            print('response:%s' % response)
            return response




class My_Custom_Service(object):
    def deal(self,webData):
        print('进入到组织用户点击　我的客服　后的回复信息的处理函数')
        cc = ConfigParser.ConfigParser()
        cc.read('/var/www/jiekou/conf/auto_reply.conf')
        value = cc.get('my_customer_service', 'content')
        tx = Text()
        reply = tx.repay_data(webData,value)

        response = HttpResponse(reply, content_type="application/xml")
        return response

class Wwnd(object):
    def deal(self,webData):
        print('这种情况是:用户点击二级菜单　我问你答　后，返回指定的图片信息')
        cc = ConfigParser.ConfigParser()
        cc.read('/var/www/jiekou/conf/auto_reply.conf')
        media_id = cc.get('wwnd', 'media_id')
        im = ImgMsg()
        reply = im.repay_data(webData, media_id)

        response = HttpResponse(reply, content_type="application/xml")
        return response


from xml.etree import ElementTree as ET
import time

class NewsMsg(object):
    def __init__(self):
        pass

    def repay_data(self, webData,title,description,picurl,url):
        print('进入到处理自动回复信息－－回复图文消息类型的函数')
        xmlData = ET.fromstring(webData)
        # 接受消息的公众号
        ToUserName = xmlData.find('ToUserName').text
        # 粉丝号
        FromUserName = xmlData.find('FromUserName').text

        now_time = int(time.time())
        # 组装返回的消息体
        text = """<xml>
 <ToUserName>{}</ToUserName>
 <FromUserName><![CDATA[{}]]></FromUserName>
 <CreateTime>{}</CreateTime>
 <MsgType>news</MsgType>
 <ArticleCount>1</ArticleCount>
 <Articles>
 <item>
 <Title><![CDATA[{}]]></Title>
 <Description><![CDATA[{}]]></Description>
 <PicUrl><![CDATA[{}]]></PicUrl>
 <Url><![CDATA[{}]]></Url>
 </item>
 </Articles>
 </xml> 
                 """.format(FromUserName,ToUserName, now_time,title,description,picurl,url)
        return text

class Text(object):
    def __init__(self):
        pass

    def repay_data(self,webData,value):
        print('进入到处理自动回复信息－－回复文本消息类型的函数')
        xmlData = ET.fromstring(webData)
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text
        now_time = int(time.time())
        text = """
        <xml>
        <ToUserName>{}</ToUserName>
        <FromUserName>{}</FromUserName>
        <CreateTime>{}</CreateTime>
        <MsgType>text</MsgType>
        <Content>{}</Content>
        </xml>
        """.format(FromUserName,ToUserName,now_time,value)
        return text

class ImgMsg(object):
    def __init__(self):
        pass
    def repay_data(self,webData,media_id):
        print('进入到处理自动回复信息－－回复文本消息类型的函数')
        xmlData = ET.fromstring(webData)
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text
        now_time = int(time.time())
        text = """
                <xml>
                <ToUserName>{}</ToUserName>
                <FromUserName>{}</FromUserName>
                <CreateTime>{}</CreateTime>
                <MsgType>image</MsgType>
                <Image>
                <MediaId>{}</MediaId>
                </Image>
                </xml>
                """.format(FromUserName, ToUserName, now_time, media_id)
        return text
