# -*- coding: utf-8 -*-

import urllib2


class ReadRequest:

    def getEveryBookReadData(self):
        request = urllib2.Request('http://127.0.0.1:8000/readrecord/readrecordapi.aspx/')
        request.add_header('action', 'getBookDataList')
        request.add_header('serial', '234234231234455')
        response = urllib2.urlopen(request)

        print response.read()


    def getPeriodReadWordTime(self):
        request = urllib2.Request('http://127.0.0.1:8000/readrecord/readrecordapi.aspx/')
        request.add_header('action', 'getPeriodReadWordTime')
        request.add_header('serial', '234234231234455')
        response = urllib2.urlopen(request)

        print response.read()

    def getReadDateBookList(self):
        request = urllib2.Request('http://127.0.0.1:8000/readrecord/readrecordapi.aspx/')
        request.add_header('action', 'getReadDateBookList')
        request.add_header('serial', '234234231234455')
        response = urllib2.urlopen(request)

        print response.read()


if __name__ == '__main__':
    testObject = ReadRequest()

    # testObject.getEveryBookReadData()
    # testObject.getPeriodReadWordTime()
    testObject.getReadDateBookList()