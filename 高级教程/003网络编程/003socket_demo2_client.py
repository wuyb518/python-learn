#!/usr/bin/python
# _*_ coding:UTF-8 _*_
import socket
HOST='localhost'
PORT=21568
BUFSIZ=1024
ADDR=(HOST,PORT)

udpCliSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data=raw_input('>')
    if not data:
        break
    udpCliSock.sendto(data,ADDR)
    data,ADDR=udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break   
    print data
udpCliSock.close()