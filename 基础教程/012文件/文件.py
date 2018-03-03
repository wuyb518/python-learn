#/usr/bin/python
# _*_ coding:UTF-8 _*_

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

fo=open('./test.txt','r+')
print '文件名:',fo.name
print '是否已关闭:',fo.closed
print '访问模式:',fo.mode
print '末尾是否强制加空格:',fo.softspace

fo.write('test write')

fo.flush()
fo.close()
