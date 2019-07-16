from django.conf.urls import url
# from django.conf.urls import  url,include


from wechat import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^hello$', views.index)  # new
    url(r'^wechat$',views.get_parm),
    # url(r'^entrance/(?P<serial>.*)$', views.wechat),
    url(r'^api/Rssforeink.ashx', views.wechat),

    url(r'^yanzheng$', views.SendToObook),
    url(r'^yanzheng/MP_verify_dtx7hOzMlkJNtt00.txt$', views.text),
    url(r'^upload$',views.upload_handle),
    url(r'^download_news$',views.download_news),
    url(r'^download_books/(?P<openid>.*)/(?P<filename>.*)$', views.download_books),
    # url(r'^download_books$', views.download_books),
    url(r'^select/(?P<serial>.*)$',views.select),
    # url(r'^save/(?P<user>.*)/(?P<booksname>.*)$',views.save),
    # url(r'^send_to_obook$',views.send_to_obook),
    url(r'^search$', views.search_book),
    # url(r'^check$',views.check),
    # url(r'^templates/(?P<template>.*)/(?P<FromUserName>.*)$',views.templates)
    url(r'^templates/(?P<template>.*)$', views.templates),
    url(r'^zhongduan$',views.zhongduan),
    url(r'^tuishu$',views.tuishu),
    url(r'^delete$',views.delete),
    url(r'^cancel$', views.cancel),
    url(r'^deal$', views.deal),
    url(r'^obookapi$',views.check),
    url(r'^shebei$',views.shebei)

]

#http://q.obook.com.cn/api/Rssforeink.ashx?seriNum=obj000000345678