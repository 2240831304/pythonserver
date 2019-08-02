#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax
import xml.sax.handler

from readrecord.operatedatabase import readprogresstable


class ReadProgressHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.serial = ""
        self.bookName = ""
        self.bookId = 0
        self.progress = 0
        self.readTime = 0
        self.readCount = 0
        self.startTime = 0
        self.endTime = 0
        self.wordCount = 0
        self.pageCount = 0

    def startElement(self, tag, attributes):
        self.CurrentData = tag

    def endElement(self, tag):
        if tag == "readProgress":
            readprogresstable.saveReadData(self)
            self.serial = ""
            self.bookName = ""
            self.bookId = 0
            self.progress = 0
            self.readTime = 0
            self.readCount = 0
            self.startTime = 0
            self.endTime = 0
            self.wordCount = 0
            self.pageCount = 0

        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "bookName":
            self.bookName = content
        elif self.CurrentData == "bookId":
            self.bookId = content
        elif self.CurrentData == "progress":
            self.progress = content
        elif self.CurrentData == "readTime":
            self.readTime = content
        elif self.CurrentData == "readCount":
            self.readCount = content
        elif self.CurrentData == "startTime":
            self.startTime = content
        elif self.CurrentData == "endTime":
            self.endTime = content
        elif self.CurrentData == "wordCount":
            self.wordCount = content
        elif self.CurrentData == "pageCount":
            self.pageCount = content

    def setSerial(self, sn):
        self.serial = sn
