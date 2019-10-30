# -*- coding: utf-8 -*-

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jiekou.settings')
django.setup()
from django.db.models import Sum,Max

from readrecord.models import readprogress,recentbooklist


def getBookReadDataList(serialID):
    list = recentbooklist.objects.values("bookName", "bookId").distinct().filter(serial=serialID)
    resultValue = []

    if list.exists():
        for value in list:
            bookIndfo = readprogress.objects.filter(serial=serialID,bookName=value['bookName'],bookId=value['bookId'])\
            .aggregate(progressMax=Max('progress'),timeCount=Sum('readTime'),wordCount=Sum('wordCount'))
            bookIndfo["bookName"] = value['bookName']
            bookIndfo["bookId"] = value["bookId"]
            resultValue.append(bookIndfo)
    else:
        return list

    # print (resultValue)
    return resultValue




if __name__ == '__main__':
    getBookReadDataList('234234231234455')