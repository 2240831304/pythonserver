# -*- coding: utf-8 -*-
#from __future__ import unicode_literals


import sys

reload(sys)
sys.setdefaultencoding('utf-8')


from django.shortcuts import render
from readrecord.handlerequest import readprogressreqhandle


# Create your views here.
from django.http import HttpResponse


def handle_readrecord_request(request):

    if request.method == 'GET':
        print ("readrord view handle_readrecord_request get!!!!!!")
    elif request.method == 'POST':
        print ("readrord view handle_readrecord_request post!!!!!!")
        requestAction = request.META.get('HTTP_ACTION', '')
        print ('readrord view handle_readrecord_request requestAction= %s' %requestAction)

        if requestAction == 'postReadProgressList':
            readprogressreqhandle.Handle_Readprogress_Post(request)

    return HttpResponse("wsisjwisjwisw")
    # return render(request, 'readrecord/test.html')


