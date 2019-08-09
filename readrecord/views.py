# -*- coding: utf-8 -*-
#from __future__ import unicode_literals


import sys

reload(sys)
sys.setdefaultencoding('utf-8')


from django.shortcuts import render
from readrecord.handlerequest import readprogressreqhandle
from readrecord.handlerequest import annotationreqhandle
from readrecord.handlerequest import recentbookhandle


# Create your views here.
from django.http import HttpResponse


def handle_readrecord_test(request):
    return render(request, 'readrecord/test.html')


def handle_readrecord_request(request):
    returnResult = {}
    handleResult = ''

    if request.method == 'GET':
        print ("readrord view handle_readrecord_request get!!!!!!")
    elif request.method == 'POST':
        print ("readrord view handle_readrecord_request post!!!!!!")
        requestAction = request.META.get('HTTP_ACTION', '')
        print ('readrord view handle_readrecord_request requestAction= %s' %requestAction)

        if requestAction == 'postReadProgressList':
            readprogressreqhandle.Handle_Readprogress_Post(request)
        elif requestAction == 'postAnnotationList':
            annotationreqhandle.Handle_Annotation_Post(request)
        elif requestAction == 'postRecentList':
            handleResult = recentbookhandle.Handle_Recentbook_Post(request)

    if handleResult == 'normal':
        returnResult['result-code'] = '23'
    elif handleResult == 'abnormal':
        returnResult['result-code'] = '1002'
    else:
        returnResult['result-code'] = '1003'

    return HttpResponse(returnResult)


