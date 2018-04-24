#!/usr/bin/env python 
# -*- coding: utf-8 -*-
""" 
@author:wei.deng 
@file: urls.py.py 
@time: 2018/01/03 
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page,name='article_page'),
    url(r'^edit/$', views.edit_page,name='edit_page'),
    url(r'^edit/action$', views.edit_action,name='edit_action'),
]
