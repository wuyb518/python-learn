#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

def simple_wsgi_app(environ,start_response):
    status='200 OK'
    headers=[('Content-Type', 'text/plain')]
    start_response(status,headers)
    return ['Hello World!']


