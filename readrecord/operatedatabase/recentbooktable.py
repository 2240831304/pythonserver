# -*- coding: utf-8 -*

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from readrecord.models import recentbooklist
from django.db import transaction
import traceback


def saveReadData(dataList,serialid):

    recentbooklist.objects.filter(serial=serialid).update(state=0)
    product_list_to_insert = list()
    resultCode = '0'
    # return resultCode

    # saveObject = recentbooklist()
    # result = recentbooklist.objects.values('bookName').get(bookName=data.bookName)

    for data in dataList:
        try:
            saveObject = recentbooklist.objects.get(serial=serialid, bookName=data.bookName, bookId=data.bookId)
        except recentbooklist.DoesNotExist:
            saveObject = recentbooklist()

        saveObject.bookName = data.bookName
        saveObject.bookId = data.bookId
        saveObject.bookFormat = data.bookFormat
        saveObject.htmlPath = data.htmlPath
        saveObject.paragraphId = data.paragraphId
        saveObject.elementId = data.elementId
        saveObject.charId = data.charId
        saveObject.pageId = data.pageId
        saveObject.content = data.content
        saveObject.serial = data.serial
        saveObject.state = True

        product_list_to_insert.append(saveObject)

    try:
        with transaction.atomic():
            for object in product_list_to_insert:
                object.save()
    except Exception as error:
        print ('recentbooktable saveReadData faile!!!!!')
        resultCode = '1028'
        traceback.print_exc()

    return resultCode