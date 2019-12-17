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
    serial = models.CharField(max_length=20, db_index=True)
    bookName = models.CharField(max_length=100)
    bookId = models.IntegerField()
    wordcount = models.IntegerField(default=0)
    timecount = models.IntegerField(default=0)
    maxprogress = models.IntegerField(default=0)
    pagecount = models.IntegerField(default=0)
    daycount = models.IntegerField(default=0)
    notecount = models.IntegerField(default=0)
    readdate = models.BigIntegerField(default=0,db_index=True)
    dayreadtime = models.IntegerField(default=0)
    dayreadword = models.IntegerField(default=0)
    dayprogress = models.IntegerField(default=0)
    state = models.BooleanField(default=False)


    class Meta:
        app_label = 'readrecord'
        db_table = 'bookreaddata'
        verbose_name = '每本书阅读数据'
        verbose_name_plural = verbose_name


class timeperioddata(models.Model):
    serial = models.CharField(max_length=20, db_index=True)
    todayword = models.IntegerField(default=0)
    todaytime = models.IntegerField(default=0)
    weekword = models.IntegerField(default=0)
    weektime = models.IntegerField(default=0)
    monthword = models.IntegerField(default=0)
    monthtime = models.IntegerField(default=0)
    yearword = models.BigIntegerField(default=0)
    yeartime = models.BigIntegerField(default=0)
    totleword = models.BigIntegerField(default=0)
    totletime = models.BigIntegerField(default=0)

    class Meta:
        app_label = 'readrecord'
        db_table = 'timeperioddata'
        verbose_name = '分时间段阅读数据'
        verbose_name_plural = verbose_name
