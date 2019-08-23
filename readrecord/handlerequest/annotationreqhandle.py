# -*- coding: utf-8 -*-

import xml.sax
import xml.sax.handler

from readrecord.handlerequest import annotationdataparse
from readrecord.operatedatabase import annotationtable


def Handle_Annotation_Post(request):
    resultCode = '0'

    bodyData = request.body
    serial = request.META.get('HTTP_SERIAL', '')

    if (serial == '') or (bodyData == ''):
        return resultCode

    try:
        # 重写 ContextHandler
        Handler = annotationdataparse.AnnotationDataParse()
        Handler.setSerial(serial)
        xml.sax.parseString(bodyData, Handler)

        listTemp = Handler.getParseData()
        print (listTemp)
        annotationtable.saveReadData(listTemp)

    except:
        print ("Handle_Annotation_Post parse data,or save data to database Peanut error!!!")
        resultCode = '1028'

    return resultCode