#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

import threading
from time import sleep,ctime

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args

    def run(self):
        self.func(*self.args)


def loop(nloop,nsec):
    print 'start loop %d at %s' %(nloop,ctime())
    sleep(nsec)
    print 'end loop %d at %s' %(nloop,ctime())

loops=[2,3,4]
def main():
    threads=[]
    nloops=range(len(loops))

    print 'start at %s' % ctime()

    for i in nloops:
        t=MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()

    print 'all done at %s' % ctime()

main()