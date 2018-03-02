#!/usr/bin/python
# _*_ coding:UTF-8 _*_

# if else
flag=False
name='wuyb'
if flag:
    print 'True'
else:
    print 'False'


if name=='wuyubo':
    print 'wuyubo'
elif name=='wuyb':
    print 'wuyb'
else:
    print 'other'

if name=='wuyb' and flag:
    print True

# while循环
numbers=[1,2,4,5,6,7,8]
# 偶数
even=[]
# 奇数
odd=[]

while len(numbers)>0:
    number=numbers.pop()
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)
else:
    print '循环结束'
    pass
print 'even:',even
print 'odd:',odd

# for循环
numbers2=[13,4,5,6,7]
for number in numbers2:
    print number

# break,continue,pass(pass是空语句,单纯为了保持程序结构的完整性)

if 2==2:
    pass


