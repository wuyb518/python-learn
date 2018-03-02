#!/usr/bin/python
# _*_ coding:UTF-8 _*_
import math
import random

# int: 10
# long: 12312L
# float: 12.23
# complex: 3.14j

# python中的数学函数
print abs(-1),math.ceil(2.2),cmp(1,2),math.exp(2),math.fabs(-10),math.floor(2.2),round(1.234563,2),math.log(100,10),math.log10(100),max(1,2,3,4,5,3,4,9),min(1,2,5,3,5,6,5),math.modf(1.23),pow(2,3),math.sqrt(4)

# 随机数函数

# random.choice返回集合中的某个随机数
numbers=[1,2,3,4,5,6,7,8,9]
print random.choice(numbers),random.choice(numbers)
# random.randrange 返回增量区间中的某个随机数
print random.randrange(2,10,2) #可能返回 4,6,8
print random.randrange(1,5,3) #只可能返回4

