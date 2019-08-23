#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax
import xml.sax.handler

class AnnotationData:
    def __init__(self):
        self.serial = ''
        self.bookName = ''
        self.bookId = 0
        self.starthtmlPath = ''
        self.startparagraphId = 0
        self.startelementId = 0
        self.startcharId = 0
        self.endhtmlPath = ''
        self.endparagraphId = 0
        self.endelementId = 0
        self.endcharId = 0
        self.content = ''
        self.origContent = ''
        self.timestamp = 0
        self.state = -1
        self.annotationId = 0


class AnnotationDataParse(xml.sax.handler.ContentHandler):

    def __init__(self):
        self.curTag = ''
        self.position = ''
        self.serial = ''
        self.antationData = None
        self.dataList = list()


    def startElement(self, tag, attributes):
        if tag == 'startPosition':
            self.position = tag
        elif tag == 'endPosition':
            self.position = tag
        elif tag == 'annotation':
            self.antationData = AnnotationData()
            self.antationData.serial = self.serial
        else:
            self.curTag = tag

    def endElement(self, tag):
        if tag == 'annotation':
            self.dataList.append(self.antationData)
        elif tag == 'startPosition':
            self.position = ''
        elif tag == 'endPosition':
            self.position = ''
        self.curTag = ''

    def characters(self, text):
        if self.position == 'startPosition':
            if self.curTag == 'htmlPath':
                self.antationData.starthtmlPath = text
            elif self.curTag == 'paragraphId':
                self.antationData.startparagraphId = text
            elif self.curTag == 'elementId':
                self.antationData.startelementId = text
            elif self.curTag == 'charId':
                self.antationData.startcharId = text
        elif self.position == 'endPosition':
            if self.curTag == 'htmlPath':
                self.antationData.endhtmlPath = text
            elif self.curTag == 'paragraphId':
                self.antationData.endparagraphId = text
            elif self.curTag == 'elementId':
                self.antationData.endelementId = text
            elif self.curTag == 'charId':
                self.antationData.endcharId = text
        else:
            if self.curTag == 'bookName':
                self.antationData.bookName = text
            elif self.curTag == 'bookId':
                self.antationData.bookId = text
            elif self.curTag == 'content':
                self.antationData.content = text
            elif self.curTag == 'origContent':
                self.antationData.origContent = text
            elif self.curTag == 'timestamp':
                self.antationData.timestamp = text
            elif self.curTag == 'state':
                self.antationData.state = text
            elif self.curTag == 'annotationId':
                self.antationData.annotationId = text

    def setSerial(self, sn):
        self.serial = sn


    def getParseData(self):
        return self.dataList
