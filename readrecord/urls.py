
from django.conf.urls import url
# from django.conf.urls import  url,include

from readrecord import views

urlpatterns = [
    url(r'^readprogress', views.handle_readrecord_request),
]
