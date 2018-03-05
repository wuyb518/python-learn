#!/usr/bin/python
# _*_ coding:UTF-8 _*_

import re
# match
m=re.match('foo','foo')
print dir(m)
print m.group()

m=re.match('foo','bar')
if m is not None:print m.group()

m=re.match('foo','food is on the table')
if m is not None:print m.group()

# search
m=re.match('foo','seafood')
if m is not None:
    print m.group()
else:
    print 'match 失败'

m=re.search('foo','seafood')
if m is not None:
    print m.group()
else:
    print 'searh 失败'

bt='bat|bet|bit'
m=re.match(bt,'bat')
if m is not None:
    print m.group()
else:
    print 'match 失败'

# findall 和 finditer
print re.findall('car','car')
print re.findall('car','scary')
print re.findall('car','carry the barcari to the car')

s='This and That'
print re.findall(r'(th\w+) and (th\w+)',s,re.I)
print re.finditer(r'(thi\w+) and (th\w+)',s,re.I).next().groups()
print re.finditer(r'(thi\w+) and (th\w+)',s,re.I).next().group(0)
print re.finditer(r'(thi\w+) and (th\w+)',s,re.I).next().group(1)
print re.finditer(r'(thi\w+) and (th\w+)',s,re.I).next().group(2)
print [g.groups() for g in re.finditer(r'(th\w+) and (th\w+)',s,re.I)]

# sub 和 subn
print re.sub('X','Mr. Smith','attn: X\n\nDear X, \n')
print re.sub('[ae]','X','abcdef')
result =re.subn('[ae]','X','abcdef')
print result
print result[0]
print result[1]
pt=r'(\d{1,2})/(\d{1,2})/(\d{1,2}|\d{4})'
print re.sub(pt,r'\2/\1/\3','2/20/91')  #wow 调整了分组顺序

#split
print re.split(':','sdf:sdfss:gg')

DATA=(
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA'
)
for datam in DATA:
    print re.split(', |(?= (?:\d{5}|[A-X]{2})) ',datam)

# 扩展符号
print re.findall(r'(?i)yes','Yes? yes. YES')
print re.findall(r'(?im)yes','''yes
sdfsdf
sdfsdf yes
YES''')

# 更多正则相关用到的时候再查文档吧


