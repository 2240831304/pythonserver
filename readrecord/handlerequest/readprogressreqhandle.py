# -*- coding: utf-8 -*-

import xml.sax
import xml.sax.handler
from readrecord.handlerequest import readprogressdataparse
from readrecord.operatedatabase import readprogresstable
import traceback

from readrecord.rabbitmq import readdataproducer
import json


def Handle_Readprogress_Post(request):
    print ("readrecord.handlerequest readprogressreqhandle Handle_Readprogress_Post!!")

    bodyData = request.body
    serial = request.META.get('HTTP_SERIAL', '')

    resultCode = '0'

    if (serial == '') or (bodyData == ''):
        return resultCode

    try:
        # 重写 ContextHandler
        Handler = readprogressdataparse.ReadProgressHandler()
        Handler.setSerial(serial)
        xml.sax.parseString(bodyData, Handler)
        tempData = Handler.getParseData()
        resultCode = readprogresstable.saveReadData(tempData)
        addQueueTask(tempData)
    except:
        print ("Handle_Readprogress_Post parse data,or save data to database Peanut error!!!")
        resultCode = '1028'
        traceback.print_exc()

    return resultCode


def addQueueTask(tasklist):
    producer = readdataproducer.ReadDataProducer()
    flag = producer.connect_mq()

    dict = {}
    if flag:
        for task in tasklist:
            dict["serial"] = task.serial
            dict["bookName"] = task.bookName
            dict["bookId"] = task.bookId
            dict["readDate"] = task.startTime
            dict["readTime"] = task.readTime
            dict["readWord"] = task.wordCount
            dict["endreadtime"] = task.endTime
            producer.addTask(json.dumps(dict))

    producer.quit()