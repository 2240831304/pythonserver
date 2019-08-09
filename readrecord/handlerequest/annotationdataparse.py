#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax
import xml.sax.handler

from readrecord.operatedatabase import annotationtable


class AnnotationDataParse(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.curTag = ''
        self.position = ''
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

    def startElement(self, tag, attributes):
        if tag == 'startPosition':
            self.position = tag
        elif tag == 'endPosition':
            self.position = tag
        else:
            self.curTag = tag

    def endElement(self, tag):
        if tag == 'annotation':
            annotationtable.saveReadData(self)
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
        elif tag == 'startPosition':
            self.position = ''
        elif tag == 'endPosition':
            self.position = ''
        self.curTag = ''

    def characters(self, text):
        if self.position == 'startPosition':
            if self.curTag == 'htmlPath':
                self.starthtmlPath = text
            elif self.curTag == 'paragraphId':
                self.startparagraphId = text
            elif self.curTag == 'elementId':
                self.startelementId = text
            elif self.curTag == 'charId':
                self.startcharId = text
        elif self.position == 'endPosition':
            if self.curTag == 'htmlPath':
                self.endhtmlPath = text
            elif self.curTag == 'paragraphId':
                self.endparagraphId = text
            elif self.curTag == 'elementId':
                self.endelementId = text
            elif self.curTag == 'charId':
                self.endcharId = text
        else:
            if self.curTag == 'bookName':
                self.bookName = text
            elif self.curTag == 'bookId':
                self.bookId = text
            elif self.curTag == 'content':
                self.content = text
            elif self.curTag == 'origContent':
                self.origContent = text
            elif self.curTag == 'timestamp':
                self.timestamp = text
            elif self.curTag == 'state':
                self.state = text
            elif self.curTag == 'annotationId':
                self.annotationId = text
            elif self.curTag == 'serial':
                self.serial = text

    def setSerial(self, sn):
        self.serial = sn
