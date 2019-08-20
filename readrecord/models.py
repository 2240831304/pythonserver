# -*- coding: utf-8 -*-

from django.db import models


# create table to store read data of progress

class readprogress(models.Model):
    serial = models.CharField(max_length=20)
    bookName = models.CharField(max_length=60)
    bookId = models.BigIntegerField()
    progress = models.IntegerField()
    readTime = models.IntegerField()
    readCount = models.IntegerField()
    startTime = models.BigIntegerField()
    endTime = models.BigIntegerField()
    wordCount = models.BigIntegerField()
    pageCount = models.IntegerField()

    class Meta:
        app_label = 'readrecord'
        db_table = 'readprogress'
        verbose_name = '阅读进度'
        verbose_name_plural = verbose_name


class annotation(models.Model):
    serial = models.CharField(max_length=20)
    bookName = models.CharField(max_length=60)
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
    serial = models.CharField(max_length=20)
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
