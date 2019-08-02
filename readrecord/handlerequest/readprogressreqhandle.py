# -*- coding: utf-8 -*-

import xml.sax
import xml.sax.handler
from readrecord.handlerequest import readprogressdataparse

def Handle_Readprogress_Post(request):
    print ("readrecord.handlerequest readprogressreqhandle Handle_Readprogress_Post!!")

    bodyData = request.body
    serial = request.META.get('HTTP_SERIAL', '')

    # 重写 ContextHandler
    Handler = readprogressdataparse.ReadProgressHandler()
    Handler.setSerial(serial)
    xml.sax.parseString(bodyData, Handler)
