#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

from time import ctime
from simple_wsgi_app import simple_wsgi_app

def ts_simple_wsgi_middleware(environ,start_response):
    return ('[%s] %s' % (ctime(), x) for x in simple_wsgi_app(environ,start_response))

    
