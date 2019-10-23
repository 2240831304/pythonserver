# -*- coding: utf-8 -*-
#from __future__ import unicode_literals


import sys

reload(sys)
sys.setdefaultencoding('utf-8')


from django.shortcuts import render
from readrecord.handlerequest import readprogressreqhandle
from readrecord.handlerequest import annotationreqhandle
from readrecord.handlerequest import recentbookhandle
from readrecord.readdataprovide import readdatareqhandle


# Create your views here.
from django.http import HttpResponse


def handle_readrecord_test(request):
    return render(request, 'readrecord/test.html')


def handle_readrecord_request(request):
    resultCode = '0'
    returnXmlData = ''

    if request.method == 'GET':
        print ("readrord view handle_readrecord_request get!!!!!!")
        requestAction = request.META.get('HTTP_ACTION', '')
        print ('readrord view handle_readrecord_request requestAction= %s' % requestAction)
        if requestAction == 'getRecentList':
            resultCode,returnXmlData = recentbookhandle.Hand_Recentbook_Get(request)
        elif requestAction == 'getAllReadBookList':
            resultCode, returnXmlData = recentbookhandle.Hand_Allbooklist_Get(request)
        elif requestAction == 'getAnnotationList':
            resultCode, returnXmlData = annotationreqhandle.Hand_Annotation_Get(request)
        elif requestAction == 'getReadDateBookList':
            resultCode, returnXmlData = readdatareqhandle.Handle_ReadDateList_Get(request)

        response = HttpResponse()
        response.setdefault('result-code',resultCode)
        response.content_type = 'application/xml'
        response.content = returnXmlData

        return response

    elif request.method == 'POST':
        print ("readrord view handle_readrecord_request post!!!!!!")
        requestAction = request.META.get('HTTP_ACTION', '')
        print ('readrord view handle_readrecord_request requestAction= %s' %requestAction)

        if requestAction == 'postReadProgressList':
            resultCode = readprogressreqhandle.Handle_Readprogress_Post(request)
        elif requestAction == 'postAnnotationList':
            resultCode = annotationreqhandle.Handle_Annotation_Post(request)
        elif requestAction == 'postRecentList':
            resultCode = recentbookhandle.Handle_Recentbook_Post(request)

        response = HttpResponse()
        response.setdefault('result-code',resultCode)
        return response
