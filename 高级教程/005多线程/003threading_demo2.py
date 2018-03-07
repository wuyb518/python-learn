#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

import threading
from time import sleep,ctime

loops=[2,3,4]

class ThreadFunc(object):
    def __init__(self,func,args,name=''):
        self.func=func
        self.args=args
        self.name=name
    
    def __call__(self):
        self.func(*self.args)

def loop(nloop,nsec):
    print 'start loop %d at %s' %(nloop,ctime())
    sleep(nsec)
    print 'end loop %d at %s' %(nloop,ctime())

def main():
    threads=[]
    nloops=range(len(loops))

    print 'start at %s' % ctime()

    for i in nloops:
        t=threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()

    print 'all done at %s' % ctime()

main()