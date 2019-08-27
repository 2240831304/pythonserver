#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax
import xml.sax.handler

class RecentBookData:
    def __init__(self):
        self.serial = ''
        self.bookName = ''
        self.bookId = 0
        self.bookFormat = ''
        self.htmlPath = ''
        self.paragraphId = 0
        self.elementId = 0
        self.charId = 0
        self.pageId = 0
        self.content = ''


class RecentBookDataParse(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.curTag = ''
        self.serial = ''
        self.recentBookDataObj = None
        self.dataList = list()


    def startElement(self, tag, attributes):
        if tag == 'book':
            self.recentBookDataObj = RecentBookData()
            self.recentBookDataObj.serial = self.serial
        self.curTag = tag

    def endElement(self, tag):
        if tag == 'book':
            self.dataList.append(self.recentBookDataObj)
        self.curTag = ''

    def characters(self, data):
        if self.curTag == 'bookName':
            self.recentBookDataObj.bookName = data
        elif self.curTag == 'bookId':
            self.recentBookDataObj.bookId = data
        elif self.curTag == 'bookFormat':
            self.recentBookDataObj.bookFormat = data
        elif self.curTag == 'htmlPath':
            self.recentBookDataObj.htmlPath = data
        elif self.curTag == 'paragraphId':
            self.recentBookDataObj.paragraphId = data
        elif self.curTag == 'elementId':
            self.recentBookDataObj.elementId = data
        elif self.curTag == 'charId':
            self.recentBookDataObj.charId = data
        elif self.curTag == 'pageId':
            self.recentBookDataObj.pageId = data
        elif self.curTag == 'content':
            self.recentBookDataObj.content = data

    def setSerial(self, sn):
        self.serial = sn

    def getParseData(self):
        return self.dataList