# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
# def wechat(request,data):
#     if data['bind'] ==1:
#         return render(request,'test1.html')
#     else:
#         return JsonResponse({'res':'指引绑定信息'})
data={'bind':1}

def deco(func):
    def wrapper(data):
        if data['bind'] == 1:
            func()
        else:
            return JsonResponse({'res': '指引绑定信息'})
    return wrapper

@deco
def upload_handle(request):
    if request.method == 'POST':
       file= request.FILES.get('files')
    # file = request.FILES['files']
    # if not file:
    #     return HttpResponse('default')
    save_path = '%s/booktest/%s' % (settings.MEDIA_ROOT, file.name)
    with open(save_path, 'wb') as f:
        # 遍历获取上传文件内容并写入新文件
        for content in file.chunks():
            f.write(content)

if __name__ == '__main__':

    upload_handle()