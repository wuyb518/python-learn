#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

import StringIO
import sys
from simple_wsgi_app import simple_wsgi_app as wsgi_app

def run_wsgi_app(app,environ):
    body=StringIO.StringIO()

    def start_response(status,headers):
        body.write('Status: %s\r\n' % status)
        for header in headers:
            body.write('%s: %s\r\n' % header)
        return body.write
    iterable=app(environ,start_response)
    try:
        if not body.getvalue():
            raise RuntimeError('start_response() not called by app!')
        body.write('\r\n%s\r\n' % '\r\n'.join( line for line in iterable))
    finally:
        if hasattr(iterable,'close') and callable(iterable.close):
            interable.close()
    
    sys.stdout.write(body.getvalue())
    sys.stdout.flush()


