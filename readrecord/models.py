# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


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

