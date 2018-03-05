#/usr/bin/python
# _*_ coding:UTF-8 _*_

import os
# 输出到屏幕
print 'print'

# 读取键盘输入
# str=raw_input('请输入:')
# print '输入内容为:',str

# raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：
# str2=raw_input('请输入:')
# print str2

# input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
# str3=input('请输入:')
# print str3

# 文件

fo=open('基础教程/012文件/test.txt','w+')
print '文件名:',fo.name
print '是否已关闭:',fo.closed
print '访问模式:',fo.mode
print '末尾是否强制加空格:',fo.softspace

fo.write('test write')

fo.flush()
fo.close()
fo=open('基础教程/012文件/test.txt','r+')
str=fo.read(50)
print str
print fo.tell()
fo.seek(0,0)
str=fo.read(4)
print str
fo.close()
os.rename('基础教程/012文件/test.txt','基础教程/012文件/test1.txt')
os.rename('基础教程/012文件/test1.txt','基础教程/012文件/test.txt')
os.remove('基础教程/012文件/test.txt')
if not os.chdir('基础教程/012文件/testdir'):
    os.mkdir('基础教程/012文件/testdir')
else:
    pass
# if os.chdir('基础教程/012文件/testdir'):
#     os.rmdir('基础教程/012文件/testdir')

