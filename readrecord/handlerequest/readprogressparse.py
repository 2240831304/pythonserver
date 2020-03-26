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



class ReadProgressParse(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.serial = ""
        self.dataList = list()
        self.dataItem = None
        self.totalCount = 0

    def startElement(self, tag, attributes):
        if tag == 'readProgress':
            self.dataItem = ReadProgressData()
        self.CurrentData = tag


    def endElement(self, tag):
        self.CurrentData = ""
        if tag == "readProgress":
            self.setBookInfo()
            self.dataList.append(self.dataItem)


    def setBookInfo(self):
        self.dataItem.serial = self.serial

        dateTp = time.localtime(int(self.dataItem.endTime))
        curDateTp = time.strftime("%Y-%m-%d", dateTp)
        timeArray = time.strptime(curDateTp, "%Y-%m-%d")

        self.dataItem.startTime = int(time.mktime(timeArray))


    def characters(self, content):
        if self.CurrentData == "bookName":
            self.dataItem.bookName = content
        elif self.CurrentData == "bookId":
            self.dataItem.bookId = content
        elif self.CurrentData == "progress":
            self.dataItem.progress = int(content)
        elif self.CurrentData == "readTime":
            self.dataItem.readTime = int(content)
        elif self.CurrentData == "readCount":
            self.dataItem.readCount = int(content)
        elif self.CurrentData == "startTime":
            self.dataItem.startTime = content
        elif self.CurrentData == "endTime":
            self.dataItem.endTime = content
        elif self.CurrentData == "wordCount":
            self.dataItem.wordCount = int(content)
        elif self.CurrentData == "pageCount":
            self.dataItem.pageCount = int(content)
        elif self.CurrentData == "totalCount":
            self.totalCount = int(content)

    def setSerial(self, sn):
        self.serial = sn

    def getParseData(self):
        return self.dataList

    def getTotalCount(self):
        return self.totalCount