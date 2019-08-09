# -*- coding: utf-8 -*

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from readrecord.models import annotation


def saveReadData(data):
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

    saveAnnotationData.save()
