#!/usr/bin/env python
# _*_ UTF-8 _*_

from wsgiref.simple_server import make_server
from simple_wsgi_app import simple_wsgi_app

httpd=make_server('',8000,simple_wsgi_app)
print 'Started app serving on port 8000'
httpd.serve_forever()
