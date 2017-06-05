# coding=utf-8
from django.conf.urls import url
import views


urlpatterns=[
    url(r'^$', views.index),
    #传入三个参数：分类 页码　排序类型
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list),
    url(r'^(\d+)/$', views.detail),
]
