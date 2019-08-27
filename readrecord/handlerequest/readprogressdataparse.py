#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax
import xml.sax.handler

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

class ReadProgressHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.serial = ""
        self.dataObject = None
        self.dataList = list()

    def startElement(self, tag, attributes):
        if tag == 'readProgress':
            self.dataObject = ReadProgressData()
            self.dataObject.serial = self.serial
        self.CurrentData = tag

    def endElement(self, tag):
        if tag == "readProgress":
            self.dataList.append(self.dataObject)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "bookName":
            self.dataObject.bookName = content
        elif self.CurrentData == "bookId":
            self.dataObject.bookId = content
        elif self.CurrentData == "progress":
            self.dataObject.progress = content
        elif self.CurrentData == "readTime":
            self.dataObject.readTime = content
        elif self.CurrentData == "readCount":
            self.dataObject.readCount = content
        elif self.CurrentData == "startTime":
            self.dataObject.startTime = content
        elif self.CurrentData == "endTime":
            self.dataObject.endTime = content
        elif self.CurrentData == "wordCount":
            self.dataObject.wordCount = content
        elif self.CurrentData == "pageCount":
            self.dataObject.pageCount = content

    def setSerial(self, sn):
        self.serial = sn

    def getParseData(self):
        return self.dataList