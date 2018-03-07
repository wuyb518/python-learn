#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

import thread
from time import sleep, ctime


# 1.单线程版本
# def loop0():
#     print 'start loop 0 at: %s' % ctime()
#     sleep(4)
#     print 'end loop 0 at: %s' % ctime()

# def loop1():
#     print 'start loop 1 at: %s' % ctime()
#     sleep(2)
#     print 'end loop 1 at: %s' % ctime()

# def main():
#     print 'start at: %s' % ctime()
#     loop0()
#     loop1()
#     print 'all done at: %s' % ctime()

# main()

# 2.多线程未同步版本
# def loop0():
#     print 'start loop 0 at: %s' % ctime()
#     sleep(4)
#     print 'end loop 0 at: %s' % ctime()

# def loop1():
#     print 'start loop 1 at: %s' % ctime()
#     sleep(2)
#     print 'end loop 1 at: %s' % ctime()

# def main():
#     print 'start at: %s' % ctime()
#     thread.start_new_thread(loop0,())
#     thread.start_new_thread(loop1,())
#     sleep(6)
#     print 'all done at: %s' % ctime()

# main()

# 3.多线程同步版本

def loop(nloop,sec,lock):
    print 'start loop %d at: %s ' % (nloop, ctime())
    sleep(sec)
    print 'end loop %d at: %s ' % (nloop, ctime())
    lock.release()

def main():
    print 'start at: %s ' % ctime()
    loops=[2,4]
    locks=[]

    nloops=range(len(loops))

    for  i in nloops:
        lock=thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    
    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked():pass

    print 'all done at: %s ' % ctime()

main()


