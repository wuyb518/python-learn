#!/usr/bin/env python
# _*_coding:UTF-8 _*_

# from django.http import HttpResponse

# def hello(request):
#     return HttpResponse('Hello world!')


from django.shortcuts import render

def hello(request):
    context={}
    context['hello']='hello world!'
    return render(request,'hello.html',context)

def testtemplate(request):
    context={}
    context['name']='wuyb'
    context['friends']=['luna','lina','sven','zues']
    context['nav']=['home','template']
    return render(request,'testtemplate.html',context)

def inherit(request):
    return render(request,'subview.html')