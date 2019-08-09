# -*- coding: utf-8 -*-

import xml.sax
import xml.sax.handler

from readrecord.handlerequest import recentbookdataparse


def Handle_Recentbook_Post(request):
    bodyData = request.body
    serial = request.META.get('HTTP_SERIAL', '')

    HandleResult = 'normal'

    try:
        # 重写 ContextHandler
        Handler = recentbookdataparse.RecentBookDataParse()
        Handler.setSerial(serial)
        xml.sax.parseString(bodyData, Handler)
    except:
        print ("Handle_Recentbook_Post parse data,or save data to database Peanut error!!!")
        HandleResult = 'abnormal'

    return HandleResult