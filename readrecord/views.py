# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse


def handle_readrecord_request(request):
    print ("sjjjjjjjjjjjjjj")
    #return HttpResponse("wsisjwisjwisw")
    return render(request, 'readrecord/test.html')


