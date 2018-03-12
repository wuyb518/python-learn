#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

import cgi

reshtml='''Content-Type text/html\n
<html>
    <head>
        <title>Friend CGI Demo(dynamic screen)</title>
    </head>
    <body>
        <h3>Friends list for:<i>%s</i></h3>
        Your name is <b>%s<b><br />
        You have <b>%s</b> friends
    </body>
</html>
'''

form=cgi.FieldStorage()
who=form['persion'].value
howmany=form['howmany'].value
print reshtml % (who,who,howmany)
