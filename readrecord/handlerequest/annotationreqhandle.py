# -*- coding: utf-8 -*-

import xml.sax
import xml.sax.handler

from readrecord.handlerequest import annotationdataparse


def Handle_Annotation_Post(request):

    bodyData = request.body
    serial = request.META.get('HTTP_SERIAL', '')

    resultCode = '0'

    try:
        # 重写 ContextHandler
        Handler = annotationdataparse.AnnotationDataParse()
        Handler.setSerial(serial)
        xml.sax.parseString(bodyData, Handler)
    except:
        print ("Handle_Annotation_Post parse data,or save data to database Peanut error!!!")
        resultCode = '1028'

    return resultCode