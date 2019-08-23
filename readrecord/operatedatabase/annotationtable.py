# -*- coding: utf-8 -*

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from readrecord.models import annotation
from django.db import transaction


def saveReadData(dataList):
    product_list_to_insert = list()
    resultCode = '0'

    for data in dataList:
        saveAnnotationData = annotation()
        saveAnnotationData.bookName = data.bookName
        saveAnnotationData.bookId = data.bookId
        saveAnnotationData.starthtmlPath = data.starthtmlPath
        saveAnnotationData.startparagraphId = data.startparagraphId
        saveAnnotationData.startelementId = data.startelementId
        saveAnnotationData.startcharId = data.startcharId
        saveAnnotationData.endhtmlPath = data.endhtmlPath
        saveAnnotationData.endparagraphId = data.endparagraphId
        saveAnnotationData.endelementId = data.endelementId
        saveAnnotationData.endcharId = data.endcharId
        saveAnnotationData.content = data.content
        saveAnnotationData.origContent = data.origContent
        saveAnnotationData.timestamp = data.timestamp
        saveAnnotationData.state = data.state
        saveAnnotationData.annotationId = data.annotationId
        saveAnnotationData.serial = data.serial

        product_list_to_insert.append(saveAnnotationData)

    # saveAnnotationData.save()
    # 用于事务保存
    savePoint = None

    try:
        savePoint = transaction.savepoint()  # 事务保存点
        annotation.objects.bulk_create(product_list_to_insert)
        # transaction.commit()
    except Exception as error:
        if savePoint:
            transaction.rollback(savePoint)
            print ('annotationtable saveReadData faile!!!!!')
            resultCode = '1028'

    return resultCode

