# -*- coding: utf-8 -*

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from readrecord.models import readprogress,booknamenumber
from django.db import transaction
import traceback
import time
import math


def saveReadData(dataList):
    product_list_to_insert = list()
    resultCode = '0'

    for data in dataList:
        saveReadProgressData = readprogress()

        try:
            reObject = booknamenumber.objects.get(bookname=data.bookName)
            saveReadProgressData.booknumber = reObject.booknumber
        except booknamenumber.DoesNotExist:
            t = time.time()
            number = int((t * 1000 * 1000) % 1000000)
            number = int(t) + number

            saveObject = booknamenumber()
            saveObject.bookname = data.bookName
            saveObject.booknumber = number
            saveObject.save()

            saveReadProgressData.booknumber = number

        saveReadProgressData.serial = data.serial
        saveReadProgressData.bookName = ''
        saveReadProgressData.bookId = data.bookId
        saveReadProgressData.progress = data.progress
        saveReadProgressData.readTime = data.readTime
        saveReadProgressData.readCount = data.readCount
        saveReadProgressData.startTime = data.startTime
        saveReadProgressData.endTime = data.endTime
        saveReadProgressData.wordCount = data.wordCount
        saveReadProgressData.pageCount = data.pageCount
        saveReadProgressData.dayminprogress = data.dayminprogress
        product_list_to_insert.append(saveReadProgressData)

    try:
        with transaction.atomic():
            readprogress.objects.bulk_create(product_list_to_insert)
    except Exception as error:
        print ('readprogresstable saveReadData faile!!!!!')
        resultCode = '1028'
        traceback.print_exc()

    return resultCode