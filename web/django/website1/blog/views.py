# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import BlogPost,BlogPostForm
from datetime import datetime
import django.http
from django.template import RequestContext

# Create your views here.

def archive(request):
    context={}
    posts=BlogPost.objects.all().order_by('-timestamp')[:3]
    context['posts']=posts # context=Context({'posts':posts})
    return render(request,'archive.html',context,RequestContext(request))

add= lambda req: render(req,'add.html')

add_new=lambda req: render(req,'add_new.html',{'form':BlogPostForm()})

def add_post(request):
    if request.method=='POST':
        post=BlogPost(
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            timestamp=datetime.now())

        post.save()
        return django.http.HttpResponseRedirect('/blog/')
    else:
        return django.http.HttpResponseForbidden()


