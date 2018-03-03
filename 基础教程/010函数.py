#!/usr/bin/python
# _*_ coding:UTF-8 _*_

# 定义函数
def printme(str):
    '打印传入的字符串到设备上'
    print str
    return

# 调用函数
printme('haha')

# 可更改(mutable)与不可更改(immutable)对象

# 不可变类型:变量赋值a=5然后在赋值a=10,这里实际是新生成一个int值对象10,然后再让a指向它,而5被丢弃,不是改变a的值,相当于新生成了a

# 传递不可变对象实例
def changeInt(a):
    a=10

b=2
changeInt(b)
print b #结果是2
# 实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它。

#传递可变对象实例

def changeme(mylist):
    mylist.append([1,2,3])
    print '函数内取值',mylist
    return
mylist=[10,20,30]
changeme(mylist)
print '函数外取值:',mylist

# 参数
# 必备参数 关键字参数 默认参数 不定长参数

# 必备参数
# 必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

# 以下实例在函数 printme() 调用时使用参数名

# 缺省参数

# 调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：

# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：
def printinfo(arg1,*vartuple):
    '打印所有传入的参数'
    print '输出:'
    print arg1
    for x in vartuple:
        print x
    return

print(1)
printinfo(1,2,3,4,5)

# 匿名函数
sum=lambda a,b:a+b
print sum(10,20)

test=lambda a,b: a+b
print test(1,2)

test=printinfo
test('haha')








