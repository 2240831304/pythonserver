# -*- coding: utf-8 -*-

import xml.sax
import xml.sax.handler
from xml.dom.minidom import Document

from readrecord.handlerequest import annotationdataparse
from readrecord.operatedatabase import annotationtable
from readrecord.models import annotation
import urlparse


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
        resultCode = annotationtable.saveReadData(listTemp)

    except:
        print ("Handle_Annotation_Post parse data,or save data to database Peanut error!!!")
        resultCode = '1028'

    return resultCode


def Hand_Annotation_Get(request):
    serialid = request.META.get('HTTP_SERIAL', '')
    resultCode = '0'
    returnXmlData = ''

    if serialid == '':
        resultCode = '1018'
        return resultCode,returnXmlData

    urlParse = urlparse.urlparse(request.get_full_path())
    keylist = urlparse.parse_qs(urlParse.query.decode("string_escape"))

    bookname = keylist['bookName'][0]
    bookname = bookname.decode("string_escape")
    bookid = int(keylist['bookId'][0])

    try:
        dataList = annotation.objects.filter(serial=serialid,bookName=bookname,bookId=bookid)
    except:
        print ("Hand_Annotation_Get select database of table annotation faile!!!!!")
        resultCode = '1028'
        return resultCode,returnXmlData

    if dataList:
        doc = Document()
        root = doc.createElement('Response')
        doc.appendChild(root)
        getAnnotationListReqNode = doc.createElement('GetAnnotationListReq')
        root.appendChild(getAnnotationListReqNode)

        for value in dataList:
            Add_Element(doc,getAnnotationListReqNode,value)
    else:
        return resultCode,returnXmlData

    # print (doc.toxml('UTF-8'))
    returnxmlData = doc.toxml('UTF-8')

    return resultCode,returnxmlData



def Add_Element(doc,node,data):
    annotationNode = doc.createElement('annotation')
    node.appendChild(annotationNode)

    booknameNode = doc.createElement('bookName')
    booknameNode.appendChild(doc.createTextNode(data.bookName))
    annotationNode.appendChild(booknameNode)

    bookidNode = doc.createElement('bookId')
    bookidNode.appendChild(doc.createTextNode(str(data.bookId)))
    annotationNode.appendChild(bookidNode)

    startPositionNode = doc.createElement('startPosition')
    annotationNode.appendChild(startPositionNode)

    starthtmlPathNode = doc.createElement('starthtmlPath')
    starthtmlPathNode.appendChild(doc.createTextNode(data.starthtmlPath))
    startPositionNode.appendChild(starthtmlPathNode)

    startparagraphIdNode = doc.createElement('startparagraphId')
    startparagraphIdNode.appendChild(doc.createTextNode(str(data.startparagraphId)))
    startPositionNode.appendChild(startparagraphIdNode)

    startelementIdNode = doc.createElement('startelementId')
    startelementIdNode.appendChild(doc.createTextNode(str(data.startelementId)))
    startPositionNode.appendChild(startelementIdNode)

    startcharIdNode = doc.createElement('startcharId')
    startcharIdNode.appendChild(doc.createTextNode(str(data.startcharId)))
    startPositionNode.appendChild(startcharIdNode)


    endPositionNode = doc.createElement('endPosition')
    annotationNode.appendChild(endPositionNode)

    endhtmlPathNode = doc.createElement('endhtmlPath')
    endhtmlPathNode.appendChild(doc.createTextNode(data.endhtmlPath))
    endPositionNode.appendChild(endhtmlPathNode)

    endparagraphIdNode = doc.createElement('endparagraphId')
    endparagraphIdNode.appendChild(doc.createTextNode(str(data.endparagraphId)))
    endPositionNode.appendChild(endparagraphIdNode)

    endelementIdNode = doc.createElement('endelementId')
    endelementIdNode.appendChild(doc.createTextNode(str(data.endelementId)))
    endPositionNode.appendChild(endelementIdNode)

    endcharIdNode = doc.createElement('endcharId')
    endcharIdNode.appendChild(doc.createTextNode(str(data.endcharId)))
    endPositionNode.appendChild(endcharIdNode)


    contentNode = doc.createElement('content')
    contentNode.appendChild(doc.createTextNode(data.content))
    annotationNode.appendChild(contentNode)

    origContentNode = doc.createElement('origContent')
    origContentNode.appendChild(doc.createTextNode(data.origContent))
    annotationNode.appendChild(origContentNode)

    timestampNode = doc.createElement('timestamp')
    timestampNode.appendChild(doc.createTextNode(str(data.timestamp)))
    annotationNode.appendChild(timestampNode)

    stateNode = doc.createElement('state')
    stateNode.appendChild(doc.createTextNode(str(data.state)))
    annotationNode.appendChild(stateNode)

    annotationIdNode = doc.createElement('annotationId')
    annotationIdNode.appendChild(doc.createTextNode(str(data.annotationId)))
    annotationNode.appendChild(annotationIdNode)
