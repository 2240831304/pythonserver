#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax
import xml.sax.handler
import time

class ReadProgressData:
    def __init__(self):
        self.serial = ''
        self.bookName = ""
        self.bookId = 0
        self.progress = 0
        self.readTime = 0
        self.readCount = 0
        self.startTime = 0
        self.endTime = 0
        self.wordCount = 0
        self.pageCount = 0
        self.dayminprogress = 0

    def clear(self):
        self.serial = ''
        self.bookName = ""
        self.bookId = 0
        self.progress = 0
        self.readTime = 0
        self.readCount = 0
        self.startTime = 0
        self.endTime = 0
        self.wordCount = 0
        self.pageCount = 0
        self.dayminprogress = 0



class ReadProgressHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.serial = ""
        self.dataObject = ReadProgressData()
        self.dataList = list()
        self.dataItem = ReadProgressData()
        self.comDate = ""
        self.totalCount = 0

    def startElement(self, tag, attributes):
        if tag == 'readProgress':
            self.dataObject.clear()
        self.CurrentData = tag

    def endElement(self, tag):
        self.CurrentData = ""
        if tag == "readProgress":
            if self.dataItem.bookName == "" and self.dataItem.bookId == 0:
                self.setBookInfo()

            dateTp = time.localtime(int(self.dataObject.endTime))
            curDateTp = time.strftime("%Y-%m-%d", dateTp)
            # print (curDateTp)
            timeArray = time.strptime(curDateTp, "%Y-%m-%d")

            if self.dataItem.bookName != self.dataObject.bookName or \
                    self.dataItem.bookId != self.dataObject.bookId or \
                    self.comDate != curDateTp:
                self.dataList.append(self.dataItem)
                self.dataItem = ReadProgressData()
                self.setBookInfo()


            if self.dataItem.progress < self.dataObject.progress:
                self.dataItem.progress = self.dataObject.progress
            elif self.dataItem.dayminprogress > self.dataObject.progress:
                self.dataItem.dayminprogress = self.dataObject.progress
            #self.dataItem.startTime = self.dataObject.startTime
            self.dataItem.startTime = int(time.mktime(timeArray))
            self.dataItem.endTime = self.dataObject.endTime
            self.dataItem.readTime += self.dataObject.readTime
            self.dataItem.readCount += self.dataObject.readCount
            self.dataItem.wordCount += self.dataObject.wordCount
            self.dataItem.pageCount += self.dataObject.pageCount

        if tag == "PostReadProgressListReq":
            self.dataList.append(self.dataItem)

    def setBookInfo(self):
        self.dataItem.bookName = self.dataObject.bookName
        self.dataItem.bookId = self.dataObject.bookId
        self.dataItem.serial = self.serial
        timeTemp = time.localtime(int(self.dataObject.endTime))
        self.comDate = time.strftime("%Y-%m-%d", timeTemp)
        self.dataItem.dayminprogress = self.dataObject.progress
        self.dataItem.progress = self.dataObject.progress


    '''
    def startElement(self, tag, attributes):
        if tag == 'readProgress':
            self.dataObject = ReadProgressData()
            self.dataObject.serial = self.serial
        self.CurrentData = tag

    def endElement(self, tag):
        if tag == "readProgress":
            self.dataList.append(self.dataObject)
        self.CurrentData = ""
    '''

    def characters(self, content):
        if self.CurrentData == "bookName":
            self.dataObject.bookName = content
        elif self.CurrentData == "bookId":
            self.dataObject.bookId = content
        elif self.CurrentData == "progress":
            self.dataObject.progress = int(content)
        elif self.CurrentData == "readTime":
            self.dataObject.readTime = int(content)
        elif self.CurrentData == "readCount":
            self.dataObject.readCount = int(content)
        elif self.CurrentData == "startTime":
            self.dataObject.startTime = content
        elif self.CurrentData == "endTime":
            self.dataObject.endTime = content
        elif self.CurrentData == "wordCount":
            self.dataObject.wordCount = int(content)
        elif self.CurrentData == "pageCount":
            self.dataObject.pageCount = int(content)
        elif self.CurrentData == "totalCount":
            self.totalCount = int(content)

    def setSerial(self, sn):
        self.serial = sn

    def getParseData(self):
        return self.dataList

    def getTotalCount(self):
        return self.totalCount