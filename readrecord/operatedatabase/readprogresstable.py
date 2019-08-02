# -*- coding: utf-8 -*

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from readrecord.models import readprogress


def saveReadData(data):

    saveReadProgressData = readprogress()

    saveReadProgressData.serial = data.serial
    saveReadProgressData.bookName = data.bookName
    saveReadProgressData.bookId = data.bookId
    saveReadProgressData.progress = data.progress
    saveReadProgressData.readTime = data.readTime
    saveReadProgressData.readCount = data.readCount
    saveReadProgressData.startTime = data.startTime
    saveReadProgressData.endTime = data.endTime
    saveReadProgressData.wordCount = data.wordCount
    saveReadProgressData.pageCount = data.pageCount

    saveReadProgressData.save()