# -*- coding: utf-8 -*-

from xml.dom.minidom import Document
import readtimeprovide


def Handle_ReadDateList_Get(request):
    serialid = request.META.get('HTTP_SERIAL', '')
    resultCode = '0'
    returnXmlData = ''

    if serialid == '':
        resultCode = '1018'
        return resultCode,returnXmlData

    resultCode,dateList = readtimeprovide.getReadDateList(serialid)

    if dateList:
        doc = Document()
        root = doc.createElement('Response')
        doc.appendChild(root)
        dateListNode = doc.createElement('GetReadDateList')
        root.appendChild(dateListNode)

        for value in dateList:
            Add_Element_Date(doc,dateListNode,value)
    else:
        return resultCode,returnXmlData

    returnxmlData = doc.toxml('UTF-8')

    return resultCode,returnxmlData


def Add_Element_Date(doc,node,data):
    dateNode = doc.createElement('Date')
    dateText = doc.createTextNode(str(data['startTime']))
    dateNode.appendChild(dateText)

    node.appendChild(dateNode)