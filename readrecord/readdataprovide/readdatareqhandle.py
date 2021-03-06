# -*- coding: utf-8 -*-

from xml.dom.minidom import Document
import readtimeprovide
import readbookprovide


# get read book days,every day read books
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
        dateListNode = doc.createElement('GetReadDateBookList')
        root.appendChild(dateListNode)

        for value in dateList:
            Add_Element_Date(doc,dateListNode,value)
    else:
        return resultCode,returnXmlData

    returnxmlData = doc.toxml('UTF-8')

    return resultCode,returnxmlData


def Add_Element_Date(doc,node,data):
    dateNode = doc.createElement('Date')
    node.appendChild(dateNode)

    bookNameNode = doc.createElement('BookName')
    bookNameText = doc.createTextNode(str(data['bookName']))
    bookNameNode.appendChild(bookNameText)

    bookIdNode = doc.createElement('BookId')
    bookIdText = doc.createTextNode(str(data['bookId']))
    bookIdNode.appendChild(bookIdText)

    readDateNode = doc.createElement('ReadDate')
    readDateText = doc.createTextNode(str(data['startTime']))
    readDateNode.appendChild(readDateText)

    dateNode.appendChild(bookNameNode)
    dateNode.appendChild(bookIdNode)
    dateNode.appendChild(readDateNode)




# get today,week,month,year,totle read times,words
def Handle_ReadWordTime_Get(request):
    serialid = request.META.get('HTTP_SERIAL', '')
    resultCode = '0'
    returnXmlData = ''

    if serialid == '':
        resultCode = '1018'
        return resultCode,returnXmlData

    doc = Document()
    root = doc.createElement('Response')
    doc.appendChild(root)
    stateNode = doc.createElement('GetReadWordTimeReq')
    root.appendChild(stateNode)

    resultCode,dateList = readtimeprovide.getTodayReadWordTime(serialid)
    Add_Today(doc,stateNode,dateList)

    resultCode, dateList = readtimeprovide.getWeekReadWordTime(serialid)
    Add_Week(doc, stateNode, dateList)

    resultCode, dateList = readtimeprovide.getMonthReadWordTime(serialid)
    Add_Month(doc, stateNode, dateList)

    resultCode, dateList = readtimeprovide.getYearReadWordTime(serialid)
    Add_Year(doc, stateNode, dateList)

    resultCode, dateList = readtimeprovide.getTotleReadWordTime(serialid)
    Add_Totle(doc, stateNode, dateList)

    returnxmlData = doc.toxml('UTF-8')

    return resultCode,returnxmlData


def Add_Today(doc,node,data):
    readWordsNode = doc.createElement('ReadWords')
    if data['wordCount'] == None :
        readWordsText = doc.createTextNode(str(0))
    else:
        readWordsText = doc.createTextNode(str(data['wordCount']))
    readWordsNode.appendChild(readWordsText)

    readTimesNode = doc.createElement('ReadTimes')
    if data['timeCount'] == None:
        readTimesText = doc.createTextNode(str(0))
    else:
        readTimesText = doc.createTextNode(str(data['timeCount']))
    readTimesNode.appendChild(readTimesText)

    todayNode = doc.createElement('Today')
    node.appendChild(todayNode)
    todayNode.appendChild(readWordsNode)
    todayNode.appendChild(readTimesNode)


def Add_Week(doc, node, data):
    readWordsNode = doc.createElement('ReadWords')
    if data['wordCount'] == None :
        readWordsText = doc.createTextNode(str(0))
    else:
        readWordsText = doc.createTextNode(str(data['wordCount']))
    readWordsNode.appendChild(readWordsText)

    readTimesNode = doc.createElement('ReadTimes')
    if data['timeCount'] == None:
        readTimesText = doc.createTextNode(str(0))
    else:
        readTimesText = doc.createTextNode(str(data['timeCount']))
    readTimesNode.appendChild(readTimesText)

    weekNode = doc.createElement('Week')
    node.appendChild(weekNode)
    weekNode.appendChild(readWordsNode)
    weekNode.appendChild(readTimesNode)

def Add_Month(doc, node, data):
    readWordsNode = doc.createElement('ReadWords')
    if data['wordCount'] == None :
        readWordsText = doc.createTextNode(str(0))
    else:
        readWordsText = doc.createTextNode(str(data['wordCount']))
    readWordsNode.appendChild(readWordsText)

    readTimesNode = doc.createElement('ReadTimes')
    if data['timeCount'] == None:
        readTimesText = doc.createTextNode(str(0))
    else:
        readTimesText = doc.createTextNode(str(data['timeCount']))
    readTimesNode.appendChild(readTimesText)

    monthNode = doc.createElement('Month')
    node.appendChild(monthNode)
    monthNode.appendChild(readWordsNode)
    monthNode.appendChild(readTimesNode)

def Add_Year(doc, node, data):
    readWordsNode = doc.createElement('ReadWords')
    if data['wordCount'] == None :
        readWordsText = doc.createTextNode(str(0))
    else:
        readWordsText = doc.createTextNode(str(data['wordCount']))
    readWordsNode.appendChild(readWordsText)

    readTimesNode = doc.createElement('ReadTimes')
    if data['timeCount'] == None:
        readTimesText = doc.createTextNode(str(0))
    else:
        readTimesText = doc.createTextNode(str(data['timeCount']))
    readTimesNode.appendChild(readTimesText)

    yearNode = doc.createElement('Year')
    node.appendChild(yearNode)
    yearNode.appendChild(readWordsNode)
    yearNode.appendChild(readTimesNode)

def Add_Totle(doc, node, data):
    readWordsNode = doc.createElement('ReadWords')
    if data['wordCount'] == None :
        readWordsText = doc.createTextNode(str(0))
    else:
        readWordsText = doc.createTextNode(str(data['wordCount']))
    readWordsNode.appendChild(readWordsText)

    readTimesNode = doc.createElement('ReadTimes')
    if data['timeCount'] == None:
        readTimesText = doc.createTextNode(str(0))
    else:
        readTimesText = doc.createTextNode(str(data['timeCount']))
    readTimesNode.appendChild(readTimesText)

    totleNode = doc.createElement('Totle')
    node.appendChild(totleNode)
    totleNode.appendChild(readWordsNode)
    totleNode.appendChild(readTimesNode)



def Hand_EveryBookData_Get(request):
    serialid = request.META.get('HTTP_SERIAL', '')
    resultCode = '0'
    returnXmlData = ''

    if serialid == '':
        resultCode = '1018'
        return resultCode,returnXmlData

    bookList = readbookprovide.getBookReadDataList(serialid)

    if bookList:
        doc = Document()
        root = doc.createElement('Response')
        doc.appendChild(root)
        bookListNode = doc.createElement('GetBookDataList')
        root.appendChild(bookListNode)

        for value in bookList:
            AddBookInfo(doc,bookListNode,value)
    else:
        return resultCode, returnXmlData

    returnXmlData = doc.toxml('UTF-8')
    return resultCode, returnXmlData


def AddBookInfo(doc, node, data):
    bookNameNode = doc.createElement("BookName")
    bookNameText = doc.createTextNode(str(data['bookName']))
    bookNameNode.appendChild(bookNameText)

    bookIdNode = doc.createElement("BookId")
    bookIdText = doc.createTextNode(str(data['bookId']))
    bookIdNode.appendChild(bookIdText)

    readTimeNode = doc.createElement("ReadTime")
    readTimeText = doc.createTextNode(str(data['timeCount']))
    readTimeNode.appendChild(readTimeText)

    readWordNode = doc.createElement("ReadWord")
    readWordText = doc.createTextNode(str(data['wordCount']))
    readWordNode.appendChild(readWordText)

    readProgressNode = doc.createElement("ReadProgress")
    readProgressText = doc.createTextNode(str(data['progressMax']))
    readProgressNode.appendChild(readProgressText)

    bookNode = doc.createElement("Book")
    bookNode.appendChild(bookNameNode)
    bookNode.appendChild(bookIdNode)
    bookNode.appendChild(readTimeNode)
    bookNode.appendChild(readWordNode)
    bookNode.appendChild(readProgressNode)

    node.appendChild(bookNode)