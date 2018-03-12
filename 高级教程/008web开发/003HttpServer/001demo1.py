#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import os

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            current_filepath=os.path.realpath(__file__)
            print 'current_filepath:',current_filepath
            root_path='%s/%s' % (os.path.dirname(current_filepath),'001demo1_file')
            print 'root_path:',root_path
            file_path='%s/%s' % (root_path,self.path[1:])
            print file_path
            f=open(file_path,'r')
          
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(f.read())
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

def main():
    try:
        server=HTTPServer(('',80),MyHandler)
        print 'Welecome to the machine...'
        print 'Press ^C once or twice to quit'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

main()
