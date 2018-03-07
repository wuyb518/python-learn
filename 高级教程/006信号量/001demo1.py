#!/usr/bin/env python
# _*_coding:UTF-8 _*_

from threading import Thread,Lock,BoundedSemaphore
from time import ctime,sleep
from atexit import register
from random import randrange

lock=Lock()
MAX=5
candy_tray=BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print 'refill candy...',
    try:
        candy_tray.release()
    except ValueError:
        print 'full,skipping'
    else:
        print 'fill ok'
    lock.release()

def buy():
    lock.acquire()
    print 'buy candy...'
    if(candy_tray.acquire(False)):
        print ' buy ok'
    else:
        print 'empty, skipping'
    lock.release()

def producer(loops):
    for i in xrange(loops):
        refill()
        sleep(randrange(3))

def customer(loops):
    for i in xrange(loops):
        buy()
        sleep(randrange(3))

def main():
    print 'starting at',ctime
    nloops=randrange(5,10)
    print 'THE CANDY MACHINE(full with %d bars)!' % MAX
    Thread(target=customer,args=(randrange(nloops,nloops+MAX+2),)).start()
    Thread(target=producer,args=(nloops,)).start()

@register
def _atexit():
    print 'all done at',ctime

main()


