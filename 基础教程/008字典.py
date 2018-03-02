#!/usr/bin/python
# _*_ coding:UTF-8 _*_

dict1={'a':1,'b':2,'c':3}
print dict1
print str(dict1)
print dict1['a']
dict1['d']=4
print dict1
del dict1['d'] #删除自定中的某个键值对
print dict1
dict1.clear()
print dict1
del dict1


dict2={'a':1,'b':2,'c':3}
dict3=dict2.copy()
print dict3  #浅复制
print dict.fromkeys('abc',3)
print dict2.has_key('b')

for x in dict2.items():
    print x

print dict2.keys()
print dict2.values()
print dict2.pop(dict2['a'])
print dict2.popitem() #随机返回并删除一个键值对

  





