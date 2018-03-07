#!/usr/bin/env python
# _*_coding:UTF-8 _*_

import threading
from atexit import register
from re import compile
from time import ctime
from urllib2 import urlopen

REGEX=compile(b'#([\d,]+) in Books ')
AMZN='http://amazon.com/dp/'
ISBNs={
    '0132269937':'Core Python Programming',
    '0132356139':'Python Web Development with Django',
    '0137143419':'Python Foundamentals'
}

def getRanking(isbn):
    url='%s%s' %(AMZN,isbn)
    print url
    page=urlopen(url,timeout=100)
    data=page.read()
    return REGEX.findall(data)[0]

def showRanking(isbn):
    print '- %r ranked %s' %(ISBNs[isbn],getRanking(isbn))

def main():
    print 'At',ctime,'onAmazon...'
    for isbn in ISBNs:
        threading.Thread(target=showRanking,args=(isbn,)).start()

@register
def _atexit():
    print 'all done at',ctime()

main()