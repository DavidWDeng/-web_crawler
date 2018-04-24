# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from django.shortcuts import render_to_response
from . import models
# Create your views here.

# def index(request):
#     t = loader.get_template('index.html')
#     c = Context({})
#
#     return HttpResponse(t.render({}
# class person(object):
#     def __init__(self,name)
#         self.name=name


def index(req):
    articles = models.Article.objects.all()
    return render(req, 'blog/index.html', {'articles':articles})
    # return render_to_response('index.html',{'title':'hello','user':'David'})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request):
    return render(request,'blog/edit_page.html')

def edit_action(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    models.Article.objects.create(title=title,content=content)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})