#!/usr/bin/python
# _*_coding:UTF-8 _*_
from socket import *
from time import ctime
HOST=''
PORT=21568
BUFSIZ=1024
ADDR=(HOST,PORT)

udpSerSock=socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

try:
    while True:
        data,addr=udpSerSock.recvfrom(BUFSIZ)
        udpSerSock.sendto('[%s] %s' %(ctime(),data),addr)
        print '...received from and returned to ',addr
finally:
    udpSerSock.close()

