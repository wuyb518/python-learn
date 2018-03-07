#!/usr/bin/env python
# _*_coding:UTF-8 _*_

import threading
from time import sleep,ctime

def fib(x):
    sleep(0.005)
    if(x<2):return 1
    return (fib(x-2) +fib(x-1))
def fac(x):
    sleep(0.1)
    if(x<2):return 1
    return (x * fac(x-1))
def sum(x):
    sleep(0.1)
    if(x<2):return 1
    return x+sum(x-1)

n=20
funcs=[fib,fac,sum]

def main():
    nloops=range(len(funcs))
    threads=[]

    for i in nloops:
        thread=threading.Thread(target=funcs[i],args=(n,),name=funcs[i].__name__)
        threads.append(thread)

    for i in nloops:
        threads[i].start()
        print '%s start at %s' %(threads[i].name,ctime())

    for i in nloops:
        threads[i].join()
        print '%s end at %s' %(threads[i].name,ctime())

main()

    
