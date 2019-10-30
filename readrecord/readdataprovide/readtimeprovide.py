# -*- coding: utf-8 -*-

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jiekou.settings')
django.setup()
from django.db.models import Sum
import datetime
import time


from readrecord.models import readprogress


def getReadDateList(serialID):
    resultCode = '0'

    try:
        list = readprogress.objects.values("startTime","bookName","bookId").distinct().filter(serial=serialID)
        # print (list)
    except:
        print ('getReadDateList faile of select data from table!!!!!')
        resultCode = '1028'

    return resultCode,list


#totle read time,word count
def getTotleReadWordTime(serialID):
    resultCode = '0'

    try:
        list = readprogress.objects.filter(serial=serialID)\
            .aggregate(timeCount=Sum('readTime'),wordCount=Sum('wordCount'))
        print ("totle:",list)
    except:
        print ('getTotleReadWordTime faile of select data from table!!!!!')
        resultCode = '1028'

    return resultCode,list


#today read time count,word count
def getTodayReadWordTime(serialID):
    resultCode = '0'

    timeNow = datetime.datetime.now()
    timeStr = timeNow.strftime('%Y-%m-%d')
    timeArray = time.strptime(timeStr, "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray))

    try:
        list = readprogress.objects.filter(serial=serialID,startTime=timeStamp)\
            .aggregate(timeCount=Sum('readTime'),wordCount=Sum('wordCount'))
        print ("today:",list,"timeStamp:",timeStamp)
    except:
        print ('getTotleReadWordTime faile of select data from table!!!!!')
        resultCode = '1028'

    return resultCode,list


#this week read time count,word count
def getWeekReadWordTime(serialID):
    resultCode = '0'

    today = datetime.date.today()
    thisWeek = today - datetime.timedelta(days=today.weekday())
    print (thisWeek)
    timeNow = datetime.datetime.now()
    timeNow = timeNow.replace(year=thisWeek.year,month=thisWeek.month,day=thisWeek.day)
    timeStr = timeNow.strftime('%Y-%m-%d')
    timeArray = time.strptime(timeStr, "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray))

    try:
        list = readprogress.objects.filter(serial=serialID,startTime__gte=timeStamp)\
            .aggregate(timeCount=Sum('readTime'),wordCount=Sum('wordCount'))
        print ("week:", list, "timeStamp:", timeStamp)
    except:
        print ('getTotleReadWordTime faile of select data from table!!!!!')
        resultCode = '1028'

    return resultCode,list


#this month read time count,word count
def getMonthReadWordTime(serialID):
    resultCode = '0'

    timeNow = datetime.datetime.now()
    timeNow = timeNow.replace(day=1)
    timeStr = timeNow.strftime('%Y-%m-%d')
    timeArray = time.strptime(timeStr, "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray))

    try:
        list = readprogress.objects.filter(serial=serialID,startTime__gte=timeStamp)\
            .aggregate(timeCount=Sum('readTime'),wordCount=Sum('wordCount'))
        print ("month:", list, "timeStamp:", timeStamp)
    except:
        print ('getTotleReadWordTime faile of select data from table!!!!!')
        resultCode = '1028'

    return resultCode,list


#this year read time count,word count
def getYearReadWordTime(serialID):
    resultCode = '0'

    timeNow = datetime.datetime.now()
    timeNow = timeNow.replace(month=1,day=1)
    timeStr = timeNow.strftime('%Y-%m-%d')
    timeArray = time.strptime(timeStr, "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray))

    try:
        list = readprogress.objects.filter(serial=serialID,startTime__gte=timeStamp)\
            .aggregate(timeCount=Sum('readTime'),wordCount=Sum('wordCount'))
        print ("year:", list, "timeStamp:", timeStamp)
    except:
        print ('getTotleReadWordTime faile of select data from table!!!!!')
        resultCode = '1028'

    return resultCode,list



if __name__ == '__main__':
    # getReadDateList('234234231234455')
    getTotleReadWordTime('234234231234455')
    getTodayReadWordTime('234234231234455')
    getWeekReadWordTime('234234231234455')
    getMonthReadWordTime('234234231234455')
    getYearReadWordTime('234234231234455')

