#!/usr/bin/python
# _*_ coding:UTF-8 _*_
from SocketServer import (TCPServer,StreamRequestHandler)
from time import ctime
HOST=''
PORT=21569
ADDR=(HOST,PORT)

class MyRequestHandler(StreamRequestHandler):
    '我的请求帮助类'
    
    def handle(self):
        print '...connected from:',self.client_address
        self.wfile.write('[%s] %s' % (ctime(),self.wfile.readline()))

tcpServ=TCPServer(ADDR,MyRequestHandler)
print 'waiting from connection...'
tcpServ.serve_forever()

