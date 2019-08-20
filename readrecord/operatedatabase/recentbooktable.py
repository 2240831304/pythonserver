# -*- coding: utf-8 -*

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from readrecord.models import recentbooklist


def saveReadData(data):

    # saveObject = recentbooklist()
    # result = recentbooklist.objects.values('bookName').get(bookName=data.bookName)

    try:
        saveObject = recentbooklist.objects.get(bookName=data.bookName, bookId=data.bookId)
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
    saveObject.state = 1;

    saveObject.save()
