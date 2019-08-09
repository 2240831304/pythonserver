#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax
import xml.sax.handler

from readrecord.operatedatabase import recentbooktable


class RecentBookDataParse(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.curTag = ''
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

    def startElement(self, tag, attributes):
        self.curTag = tag

    def endElement(self, tag):
        if tag == 'book':
            recentbooktable.saveReadData(self)
            self.bookName = ''
            self.bookId = 0
            self.bookFormat = ''
            self.htmlPath = ''
            self.paragraphId = 0
            self.elementId = 0
            self.charId = 0
            self.pageId = 0
            self.content = ''
        self.curTag = ''

    def characters(self, data):
        if self.curTag == 'bookName':
            self.bookName = data
        elif self.curTag == 'bookId':
            self.bookId = data
        elif self.curTag == 'bookFormat':
            self.bookFormat = data
        elif self.curTag == 'htmlPath':
            self.htmlPath = data
        elif self.curTag == 'paragraphId':
            self.paragraphId = data
        elif self.curTag == 'elementId':
            self.elementId = data
        elif self.curTag == 'charId':
            self.charId = data
        elif self.curTag == 'pageId':
            self.pageId = data
        elif self.curTag == 'content':
            self.content = data

    def setSerial(self, sn):
        self.serial = sn
