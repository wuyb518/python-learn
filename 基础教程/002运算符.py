#!/usr/bin/python
# _*_coding:UTF-8 _*_

# python算数运算符

# ** 幂-返回x的y次幂
print 2**3
print 2**3==8

# //取整除-返回上的整数部分

print 3.0/2,3.0//2
print 3.0/2==3.0//2

# 位运算

# & 位与
print 1&2,3&2,3&0
# | 位或
print 1|2,3|2,3|0
# ^异或
print 1^2,3^2,3^0
# ~按位取反:对于数据的每个二进制位取反即把0变为1,把1变为0
## <<左移
print 1<<2,2<<1,0<<1
# >>右移
print 2>>1,3>>1,0>>1

# 逻辑运算符
# and or not

# 成员运算符
# in
print 2 in (1,2),3 in (1,2)
# not in
print 2 not in(1,2),3 not in(1,2)

# 身份运算符
a=20
b=20

if(a is b):
    print '1-a 和 b 有相同的标识'
else:
    print '1-a 和 b 没有相同的标识'




