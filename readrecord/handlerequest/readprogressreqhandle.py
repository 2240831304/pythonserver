# -*- coding: utf-8 -*-

import xml.sax
import xml.sax.handler
from readrecord.handlerequest import readprogressdataparse
from readrecord.operatedatabase import readprogresstable
import traceback


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
    except:
        print ("Handle_Readprogress_Post parse data,or save data to database Peanut error!!!")
        resultCode = '1028'
        traceback.print_exc()

    return resultCode
