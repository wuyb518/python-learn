#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

import threading
from time import sleep,ctime

def loop(nloop,nsec):
    print 'start loop %d at %s' %(nloop,ctime())
    sleep(nsec)
    print 'end loop %d at %s' %(nloop,ctime())

def main():
    loops=[2,3,4]
    nloops=range(len(loops))
    threads=[]

    print 'start'

    for i in nloops:
        thread=threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(thread)

    for i in nloops:
        threads[i].start()
    
    for i in nloops:
        threads[i].join()

    print 'all done at %s' % ctime()

main()