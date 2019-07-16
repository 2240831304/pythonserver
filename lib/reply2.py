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
    def subscribe(self,content):
        msg = parse_message(content)

        cc = ConfigParser.ConfigParser()
        cc.read('./conf/auto_reply.conf')
        value = cc.get('subscribe', 'subscribe_content')
        reply = create_reply(value, msg)
        response = HttpResponse(reply.render(), content_type="application/xml")
        return response
#         ToUserName = xmlData.find('ToUserName').text
#         # 粉丝号
#         FromUserName = xmlData.find('FromUserName').text
#
#         now_time = int(time.time())
#         # 组装返回的消息体
#         content = '''你好，谢谢关注当当阅读器！'\
#
# '回复关键词“开学季”可领取三大锦囊哦 \ue312\ue312\ue312！'''
#
#         text = """
#                         <xml>
#                         <ToUserName><![CDATA[{0}]]></ToUserName>
#                         <FromUserName><![CDATA[{1}]]></FromUserName>
#                         <CreateTime>{2}</CreateTime>
#                         <MsgType><![CDATA[text]]></MsgType>
#                         <Content><![CDATA[content]]></Content>
#                         </xml>
#                         """.format(FromUserName, ToUserName, now_time,content)
#         return text

#关键字回复
class Keyword_Reply(object):
    '''
    根据捕获到的用户发送的消息关键字，去分析，返回相应的自动回复信息
    '''
    def deal(self,content,text):
        print('进入处理自动回复的函数')

        msg = parse_message(content)
        if msg.type == 'text':
            if text.find('碎') != -1 or text.find('保险') != -1:
                cc = ConfigParser.ConfigParser()
                cc.read('./conf/auto_reply.conf')
                title = cc.get('broken', 'broken_title')
                description = cc.get('broken', 'broken_description')
                picurl = cc.get('broken', 'broken_picurl')
                url = cc.get('broken', 'broken_url')
                tm = TextMsg()
                reply = tm.repay_data(content,title,description,picurl,url)
                response = HttpResponse(reply, content_type="application/xml")
                print('response:%s' % response)
                return response

            elif text.find('当当VIP') != -1 or\
                text.find('VIP') != -1 or\
                text.find('vip') != -1 or \
                text.find('当当vip') != -1 :
                cc = ConfigParser.ConfigParser()
                cc.read('./conf/auto_reply.conf')
                value = cc.get('vip', 'vip_content')
                print('自动回复--vip')
                reply = create_reply(value, msg)
                # print('完成处理关键字--vip')
                # return reply

            elif text.find('售后') != -1:
                # reply = create_reply('这是售后', msg)
                print('进入处理售后消息的函数')
                cc = ConfigParser.ConfigParser()
                cc.read('./conf/auto_reply.conf')
                title = cc.get('customer_service', 'customer_service_title')
                description = cc.get('customer_service', 'customer_service_description')
                picurl = cc.get('customer_service', 'customer_service_picurl')
                url = cc.get('customer_service', 'customer_service_url')
                tm = TextMsg()
                reply = tm.repay_data(content,title,description,picurl,url)
                # reply = create_reply(reply,msg)
                response = HttpResponse(reply,content_type="application/xml")
                print('response:%s'%response)
                return response
            elif text.find('热门书籍') != -1 :
                cc = ConfigParser.ConfigParser()
                cc.read('./conf/auto_reply.conf')
                value = cc.get('hot_books', 'hot_books_content')
                reply = create_reply(value, msg)

            # elif text.find('免费') != -1 or text.find('免费书') != -1 or text.find('免费电子书') != -1:
            #     reply = create_reply('这是免费书消息', msg)

            elif text.find('开不了机') != -1 or text.find('进水') != -1 or\
                text.find('坏了') != -1 or text.find('故障') != -1 or\
                text.find('问题') != -1 or text.find('闪屏') != -1:
                print('进入故障的处理函数')
                cc = ConfigParser.ConfigParser()
                cc.read('./conf/auto_reply.conf')
                title = cc.get('usual_problem', 'usual_problem_title')
                description = cc.get('usual_problem', 'usual_problem_description')
                picurl = cc.get('usual_problem', 'usual_problem_picurl')
                url = cc.get('usual_problem', 'usual_problem_url')
                tm = TextMsg()
                reply = tm.repay_data(content, title, description, picurl, url)
                # reply = create_reply(reply,msg)
                response = HttpResponse(reply, content_type="application/xml")
                print('response:%s' % response)
                return response

            elif text.find('书') != -1 or text.find('推荐') != -1 :
                cc = ConfigParser.ConfigParser()
                cc.read('./conf/auto_reply.conf')
                title = cc.get('book_list', 'book_list_title')
                description = cc.get('book_list', 'book_list_description')
                picurl = cc.get('book_list', 'book_list_picurl')
                url = cc.get('book_list', 'book_list_url')
                tm = TextMsg()
                reply = tm.repay_data(content, title, description, picurl, url)
                # reply = create_reply(reply,msg)
                response = HttpResponse(reply, content_type="application/xml")
                print('response:%s' % response)
                return response
            elif text.find('你好') != -1 or text.find('在吗') != -1 or text.find('嗨') != -1:
                cc = ConfigParser.ConfigParser()
                cc.read('./conf/auto_reply.conf')
                value = cc.get('hello', 'hello_content')
                reply = create_reply(value, msg)

            elif text.find('DDYDQ') != -1:
                cc = ConfigParser.ConfigParser()
                cc.read('./conf/auto_reply.conf')
                value = cc.get('DDYDQ', 'DDYDQ_content')
                reply = create_reply(value, msg)
            elif text.find('当当阅读器') != -1:
                cc = ConfigParser.ConfigParser()
                cc.read('./conf/auto_reply.conf')
                value = cc.get('obook', 'obook_content')
                reply = create_reply(value, msg)
            else:#识别不了的统一回复　收到消息后的回复
                cc = ConfigParser.ConfigParser()
                cc.read('./conf/auto_reply.conf')
                value = cc.get('others', 'others_content')
                reply = create_reply(value, msg)
            response = HttpResponse(reply.render(), content_type="application/xml")
            return response

class My_Custom_Service:
    def deal(self,content):
        msg = parse_message(content)
        reply = create_reply('客服电话：075586957006  （周一到周六 9：00-18:30）', msg)
        response = HttpResponse(reply.render(), content_type="application/xml")
        return response


from xml.etree import ElementTree as ET
import time


class Analysis:
    def __init__(self, xmlData):
        print("接收到的数据：" + xmlData)

    def jiexi(self, xmlText):
        xmlData = ET.fromstring(xmlText)
        msg_type = xmlData.find('MsgType').text
        if msg_type == 'text':
            text_msg = TextMsg(xmlData)
            return text_msg.repay_data(xmlData)


class TextMsg:
    def __init__(self):
        pass

    def repay_data(self, webData,title,description,picurl,url):
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

# def getResponseImageTextXml(self, FromUserName, ToUserName, sourceList):
#     """
#         source = [title, description, picurl, url]
#     """
#     itemXml = []
#     for source in sourceList:
#         # source = [title1, description1, picurl, url]
#         singleXml = """
#             <item>
#                 <Title><![CDATA[%s]]></Title>
#                 <Description><![CDATA[%s]]></Description>
#                 <PicUrl><![CDATA[%s]]></PicUrl>
#                 <Url><![CDATA[%s]]></Url>
#             </item>
#         """ % (source[0], source[1], source[2], source[3])
#         itemXml.append(singleXml)
#     reply = """
#         <xml>
#             <ToUserName><![CDATA[%s]]></ToUserName>
#             <FromUserName><![CDATA[%s]]></FromUserName>
#             <CreateTime>%s</CreateTime>
#             <MsgType><![CDATA[news]]></MsgType>
#             <ArticleCount>%d</ArticleCount>
#             <Articles>
#                 %s
#             </Articles>
#         </xml>
#     """ % (FromUserName, ToUserName, str(int(time.time())), len(sourceList), " ".join(itemXml))
#     response = make_response(reply)
#     response.content_type = 'application/xml'
#     return response