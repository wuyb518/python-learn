#!/usr/bin/python
# _*_coding:UTF-8 _*_
import ftplib
import os
import socket
HOST='ftp.mozilla.org'
DIRN='pub/mozilla.org/webtools'
FILE='bugzilla-LATEST.tar.gz'

def main():
    try:
        f=ftplib.FTP(HOST)
    except (socket.error,socket.gaierror) as e:
        print 'ERROR:cannot reach "%s"' % HOST
        return
    print '*** Connected to host "%s"' % HOST

    try:
        f.login()
    except ftplib.error_perm:
        print  'ERROR: can\'t login anonymously'
        f.quit()
        return
    
    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print  'ERROR: can\'t CD to "%s"' % DIRN
        f.quit()
        return
    print 'Changed to "%s" folder' % DIRN
    
    try:
        f.retrbinary('RETR %s' % FILE,open(FILE,'wb'.write))
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % FILE
        os.unlink(FILE)
    else:
        print '***Downloaded "%s" to CWD***' %FILE
    

main()

