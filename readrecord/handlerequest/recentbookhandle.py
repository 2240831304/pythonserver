# -*- coding: utf-8 -*-

import xml.sax
import xml.sax.handler

from readrecord.handlerequest import recentbookdataparse


def Handle_Recentbook_Post(request):
    bodyData = request.body
    serial = request.META.get('HTTP_SERIAL', '')

    # 重写 ContextHandler
    Handler = recentbookdataparse.RecentBookDataParse()
    Handler.setSerial(serial)
    xml.sax.parseString(bodyData, Handler)
