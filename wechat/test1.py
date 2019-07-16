#coding:utf-8
# list = [[1789,'今天',3],[47854,'明天',6]]
# for l in list:
#     print(l[1])
#
# import pypub
# my_first_epub = pypub.Epub('我的第一个EPUB ')
# my_first_chapter = pypub.create_chapter_from_url(' https://en.wikipedia.org/wiki/EPUB ')
# my_first_epub.add_chapter(my_first_chapter)
# my_first_epub.create_epub('我的epub ')
# from wechat.models import User,User1
# from django.core import serializers
# from django.core import serializers
# data = serializers.serialize("json", User.objects.all())
#
# print(data)
# import os,django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jiekou.settings")# project_name 项目名称
# django.setup()
# from django.core import serializers
# from wechat.models import *
from django.db.models import F,Q
# from django.http import HttpResponse
# import json
# def special():
#     # Q(nid__gt=10)
#     a = User1.objects.all()  #获取id大于3的数据
#     print(a)   #得到queryset对象
#
#     b = serializers.serialize("json",a)     #将queryset对象转换成json类型
#     b = b.decode('raw_unicode_escape')
#     print(b)                                #得到json类型
#
#     c = json.loads(b)                       #将json类型还原成Python数据类型
#     print(c)
#     return HttpResponse(b)
#
#
# if __name__ == '__main__':
#     special()

# import logging
# logging.debug('debug 信息')
# logging.warning('只有这个会输出。。。')
# logging.info('info 信息')

# import logging
# # logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
# #                     level=logging.DEBUG)
# # logging.debug('debug 信息')
# # logging.info('info 信息')
# # logging.warning('warning 信息')
# # logging.error('error 信息')
# # logging.critical('critial 信息')
#
# logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
#                     filename='new.log',
#                     filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
#                     #a是追加模式，默认如果不写的话，就是追加模式
#                     format=
#                     '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
#                     #日志格式
#                     )
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import logging
from logging import handlers

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

    def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)
if __name__ == '__main__':
    log = Logger('all.log',level='debug')
    log.logger.debug('debug')
    log.logger.info('info')
    log.logger.warning('警告')
    log.logger.error('报错')
    log.logger.critical('严重')
    Logger('error.log', level='error').logger.error('error')