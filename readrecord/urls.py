
from django.conf.urls import url
# from django.conf.urls import  url,include

from readrecord import views

urlpatterns = [
    url(r'^readrecordapi.aspx', views.handle_readrecord_request),
    url(r'^readrecordtest', views.handle_readrecord_test),
]
