#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

from simple_wsgi_middleware import ts_simple_wsgi_middleware
from wsgiref.simple_server import make_server

httpd=make_server('',8000,ts_simple_wsgi_middleware)
print 'Started app serving on port 8000'
httpd.serve_forever()