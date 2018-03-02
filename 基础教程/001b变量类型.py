#!/usr/bin/python
# _*_ coding:UTF-8 _*_

print "你好,世界"

# 多个变量赋值
a=b=c=1
print a,b,c

# 标准数据类型
# Numbers String List Tuple Dictionary

# python中的数字
var1=1
var2=2
del var1,var2 # 删除变量,释放资源

# python中的字符串
s="a1a2...an"
print s

str="Hello World"
print str
print str[0]
print str[2:5] # 输出字符串[2,5]之间的字符
print str[2:]  # 输入字符串[2,最后]之间的字符
print str*2
print str+"TEST"

# python中的列表(数组)
list=['runoob',766,2.34,'john',50.6]
tinylist=[123,'haha']
print list
print list[0]
print list[1:3]
print list[2:]
print tinylist*2
print list+tinylist

# python中的元组,元组不能按索引赋值
tuple=('runoob',766,2.34,'john',50.6)
tinytuple=(123,'haha')
print tuple
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tinytuple*2
print tuple+tinytuple

# python中的字典
dict={}
dict['one']='This is one'
dict['three']=3
dict['three']='san'
tinydict={'one':1,'two':2,'three':3}
print dict['one']
print dict['three']
print tinydict
print tinydict.keys()
print tinydict.values()

print int('1')
print long('123L')
print float('123.456')
# print str(12)
print repr('1+2')
print eval('1+2')
# print tuple('(1,2,3)')
# print list((1,2,3))
# print dict('{1:1,2:2,3:5}')
# print set({})
# print chr(96)
# print unichr(97)
# print ord('a')
# print hex(16)
# print oct(8)




