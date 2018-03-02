#!/usr/bin/python
# _*_ coding:UTF-8 _*_

var1='Hello world'
var2='Python Runoob'

# 访问字符串中的值
print 'var1[0]',var1[0]
print 'var2[1:5]',var2[1:5]

# 字符串更新
var1='Hello World'
print '更新字符串:-',var1[:6]+'Runoob!'

# 字符串运算符

# + 字符串连接
print 'hello '+'world'
# * 字符串复制
print 'hello '*2
# [] 按索引获取字符
print 'hello'[1]
# [:] 截取字符串,前包含,后不包含
print 'hello'[2:4]
# in 被包含
print 'e' in 'hello'
# not in 不被包含
print 'a' not in 'hello'

# r/R 返回原始字符串
print r'aaa\naaa'
print '''aaa
aaaa'''
print 'aaa\naaa'

# 字符串內建函数
print 'hello'.capitalize() #首字符大写
print 'hello'.center(20) # 返回一个原字符串居中,并使用空格填充长度至width的新字符串
print 'hello'.count('ll',0,len('hello')) #子字符串在字符串中出现的次数

# string.decode(encoding="UTF-8",errors="strict")按指定编码格式解码string
# string.encode(encoding="UTF-8",errors="strict")按指定编码格式编码string
# string.endswith(str,beg=0,end=len(string))检查字符串是否以str结尾
# string.expandtabs(tabsize=8) 将字符串中的tab转换为空格,默认tab符号的空格数为8
# string.find(str,beg=0,end=len(string)) 检查str是否在find中存在,存在返回索引值,不存在返回-1
# string.format()格式化字符串
# string.index(str,beg=0,end=len(string)) 功能和find一样,但是不存在会抛出异常
# 还有好多函数,用到在学习吧






