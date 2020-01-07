# -*- coding: utf-8 -*-

import os
import django
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jiekou.settings')
django.setup()

from django.db.models import Sum,Max

from readrecord.models import readprogress,recentbooklist,bookreaddata


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


def getReadDataList(serialID):
    list = bookreaddata.objects.values("bookName","bookId","wordcount","timecount","maxprogress","readdate",
                                       "dayreadtime","dayreadword","dayreadprogress","daymaxprogress","dayminprogress")\
        .filter(serial=serialID,state=1)

    # print (list)
    return list

def updateState(serialID):
    bookreaddata.objects.filter(serial=serialID,state=1).update(state=False)



def getAllReadProgress(serialid,minRecord,maxRecord):
    list = bookreaddata.objects.values("bookName", "bookId", "wordcount", "timecount", "maxprogress", "readdate")\
        .filter(serial=serialid,record__gt=minRecord,record__lt=maxRecord)

    return list


def getLoseReadProgress(serialid,minTime,minRecord,maxRecord):
    list = bookreaddata.objects.values("bookName", "bookId", "wordcount", "timecount", "maxprogress", "readdate")\
        .filter(serial=serialid,record__gt=minRecord,record__lt=maxRecord,readdate__lt=minTime)

    return list


def getMaxRecord(serialID):
    try:
        recordInfo = bookreaddata.objects.filter(serial=serialID).aggregate(maxRecord=Max('record'))
        return recordInfo['maxRecord']
    except:
        return 1


if __name__ == '__main__':
    getBookReadDataList('234234231234455')
    getReadDataList('OF6IC31811B00030')