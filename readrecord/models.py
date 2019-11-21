# -*- coding: utf-8 -*-

from django.db import models


# create table to store read data of progress

class readprogress(models.Model):
    serial = models.CharField(max_length=20, db_index=True)
    bookName = models.CharField(max_length=60, db_index=True)
    bookId = models.BigIntegerField()
    progress = models.IntegerField()
    readTime = models.IntegerField()
    readCount = models.IntegerField()
    startTime = models.BigIntegerField()
    endTime = models.BigIntegerField()
    wordCount = models.IntegerField()
    pageCount = models.IntegerField()

    class Meta:
        app_label = 'readrecord'
        db_table = 'readprogress'
        verbose_name = '阅读进度'
        verbose_name_plural = verbose_name


class annotation(models.Model):
    serial = models.CharField(max_length=20, db_index=True)
    bookName = models.CharField(max_length=60, db_index=True)
    bookId = models.IntegerField()
    starthtmlPath = models.CharField(max_length=40)
    startparagraphId = models.IntegerField()
    startelementId = models.IntegerField()
    startcharId = models.IntegerField()
    endhtmlPath = models.CharField(max_length=40)
    endparagraphId = models.IntegerField()
    endelementId = models.IntegerField()
    endcharId = models.IntegerField()
    content = models.TextField()
    origContent = models.TextField()
    timestamp = models.IntegerField()
    state = models.IntegerField()
    annotationId = models.IntegerField()

    class Meta:
        app_label = 'readrecord'
        db_table = 'annotation'
        verbose_name = '书摘批注'
        verbose_name_plural = verbose_name


class recentbooklist(models.Model):
    serial = models.CharField(max_length=20, db_index=True)
    bookName = models.CharField(max_length=100)
    bookId = models.IntegerField()
    bookFormat = models.CharField(max_length=15)
    htmlPath = models.CharField(max_length=50)
    paragraphId = models.IntegerField()
    elementId = models.IntegerField()
    charId = models.IntegerField()
    pageId = models.IntegerField()
    content = models.TextField()
    timestamp = models.IntegerField(default=0)
    state = models.BooleanField(default=False)

    class Meta:
        app_label = 'readrecord'
        db_table = 'recentbooklist'
        verbose_name = '最近阅读的图书'
        verbose_name_plural = verbose_name


class bookreaddata(models.Model):
    serial = models.CharField(max_length=15, db_index=True)
    bookName = models.CharField(max_length=100)
    bookId = models.IntegerField()
    wordcount = models.IntegerField()
    timecount = models.IntegerField()
    maxprogress = models.IntegerField()
    pagecount = models.IntegerField()
    daycount = models.IntegerField()
    notecount = models.IntegerField()


    class Meta:
        app_label = 'readrecord'
        db_table = 'bookreaddata'
        verbose_name = '每本书阅读数据'
        verbose_name_plural = verbose_name