# -*- coding: utf-8 -*-

import xml.sax
import xml.sax.handler
from xml.dom.minidom import Document

from readrecord.handlerequest import recentbookdataparse
from readrecord.models import recentbooklist

XML_Header = '<?xml version="1.0" encoding="utf-8"?>'


def Handle_Recentbook_Post(request):
    bodyData = request.body
    serialid = request.META.get('HTTP_SERIAL', '')

    resultCode = '0'

    try:
        recentbooklist.objects.filter(serial=serialid).update(state=0)

        # 重写 ContextHandler
        Handler = recentbookdataparse.RecentBookDataParse()
        Handler.setSerial(serialid)
        xml.sax.parseString(bodyData, Handler)
    except:
        print ("Handle_Recentbook_Post parse data,or save data to database Peanut error!!!")
        resultCode = '1028'

    return resultCode



def Hand_Recentbook_Get(request):
    serialid = request.META.get('HTTP_SERIAL', '')
    resultCode = '0'
    returnXmlData = ''

    try:
        dataList = recentbooklist.objects.filter(serial=serialid,state=1)
    except:
        print ("Hand_Recentbook_Get select database of table recentbooklist faile!!!!!")
        resultCode = '1028'
        return resultCode,returnXmlData

    if dataList:
        doc = Document()
        root = doc.createElement('Response')
        doc.appendChild(root)
        getRecentListReq = doc.createElement('GetRecentListReq')
        root.appendChild(getRecentListReq)

        for value in dataList:
            Add_Element(doc,getRecentListReq,value)
    else:
        return resultCode,returnXmlData

    # print (doc.toxml('UTF-8'))
    returnxmlData = doc.toxml('UTF-8')

    return resultCode,returnxmlData


def Add_Element(doc,node,data):
    book = doc.createElement('book')
    node.appendChild(book)

    bookName = doc.createElement('bookName')
    bookNameText = doc.createTextNode(data.bookName)
    bookName.appendChild(bookNameText)

    bookId = doc.createElement('bookId')
    bookIdText = doc.createTextNode(str(data.bookId))
    bookId.appendChild(bookIdText)

    book.appendChild(bookName)
    book.appendChild(bookId)