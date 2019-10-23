# -*- coding: utf-8 -*-

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jiekou.settings')
django.setup()


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



if __name__ == '__main__':
    getReadDateList('OS6BB11727B00997')

