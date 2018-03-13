#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.archive),
    url('^add$',views.add),
    url('^add_new$',views.add_new),
    url('^add_post$',views.add_post)

]