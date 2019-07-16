# -*- coding: UTF-8 -*-
from django.db import models

class User(models.Model):
    bookid = models.CharField('图书编号',max_length=50,default=1)
    username = models.CharField('用户名',max_length=30)
    newsname = models.CharField('新闻标题',max_length=50,null = True,blank=True)
    booksname = models.CharField('上传图书名',max_length=50,null= True,blank=True)
    # status = models.CharField('图书状态',max_length=10,blank=True)
    url = models.CharField(max_length=300,verbose_name='图书下载地址',default=1)
    md5 = models.CharField('图书md值',max_length=128,blank=True)
    class Meta:
        db_table = 'wechat'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


# class User1(models.Model):
#     # id = models.AutoField(primary_key=True, verbose_name='编号')
#     bookid = models.CharField(max_length=50,verbose_name='书籍id')
#     booksname = models.CharField(max_length=50,verbose_name='书名')
#     serial = models.CharField(max_length=50,verbose_name='终端序列号')
#     url = models.CharField(max_length=100,verbose_name='图书下载地址')
#     status = models.CharField(max_length=10,default=False,verbose_name='图书下载状态')
#     # weid = models.CharField(max_length=50,verbose_name='用户openid')
#     # bind = models.CharField(max_length=10,verbose_name='绑定状态',default=0)
#     class Meta:
#         db_table = 'obook'
#         verbose_name = '国文'
#         verbose_name_plural = verbose_name


class User2(models.Model):
    serial = models.CharField(max_length=50, verbose_name='终端序列号')
    weid = models.CharField(max_length=50, verbose_name='用户openid',null=True,blank=True)
    bind = models.CharField(max_length=10, verbose_name='绑定状态', default=0)
    scene_id = models.CharField(max_length=32,verbose_name='scend_id')

    class Meta:
        db_table = 'tobind'
        verbose_name = '绑定'
        verbose_name_plural = verbose_name

class User3(models.Model):
    # weid = models.CharField(max_length=50, verbose_name='用户openid', null=True, blank=True)
    # bookid = models.CharField(max_length=50, verbose_name='图书编号')
    bookid = models.CharField(max_length=50,verbose_name='推送书籍编号',default=1)
    serial = models.CharField(max_length=50, verbose_name='终端序列号',default=0)
    # url = models.CharField(max_length=100,verbose_name='图书下载地址')

    class Meta:
        db_table = 'booksend'
        verbose_name = '推送书籍'
        verbose_name_plural = verbose_name

class User4(models.Model):
    serial = models.CharField(max_length=50, verbose_name='终端序列号')
    weid = models.CharField(max_length=50, verbose_name='用户openid', blank=True)

    class Meta:
        db_table = 'sewe'
        verbose_name = '简单绑定'
        verbose_name_plural = verbose_name