#!/usr/bin/python
# _*_ coding:UTF-8 _*_

list1=['physics','chemistry',1997,2000]
list2=[1,2,3,4,5]
list3=['a','b','c','d']

print 'list1[0]',list1[0]
print 'list2[1:5]', list2[1:5]

list=[]

list.append('first')
list.append('second')
print list

del list1

len(list2)
print [1,2,3]+[4,5]
print 3 in [1,2]
for x in [1,2,3]:print x

list4=['google','facebook','taobao']
print list4[1]
print list4[-1]
print list4[-2]
print list4[1:]



list1=[]
list1.append('a')
print list1.count(2)
list1.extend([1,2,3])
list1.index(2)
list1.insert(0,'begin')
print list1.pop()
list1.remove(list1[1])
print list1
list1.reverse()
print list1
list1.sort()
print list1




