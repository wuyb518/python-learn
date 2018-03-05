#!/usr/bin/python
# _*_ coding:UTF-8 _*_

# 类
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t=Test()
t.prt()

class Employee:
    '所有员工的基类'
    empCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def __del__(self):
        class_name=self.__class__.__name__
        print class_name,'销毁'
    
    def displayCount(self):
        print 'Total Employee %d' % Employee.empCount
    
    def displayEmployee(self):
        print 'Name:',self.name,"Salary:",self.salary
    

emp1=Employee('Zara',2000)
emp2=Employee('Manni',5000)
emp1.displayEmployee()
emp2.displayEmployee()
print 'Total employee %d' % Employee.empCount

print hasattr(emp1,'name')
print getattr(emp1,'name')
setattr(emp1,'name','wuyb')
delattr(emp1,'name')

print "Employee.__doc__:",Employee.__doc__ #类说明
print 'Employee.__name__:',Employee.__name__ #类名
print 'Employee.__module__:',Employee.__module__ #类所在模块
print 'Employee.__bases__:',Employee.__bases__ # 所有基类
print "Employee.__dict__:",Employee.__dict__

del emp2

# 继承
class Parent:
    parentAttr=100
    def __init__(self):
        print '调用父类构造函数'
    
    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self,attr):
        Parent.parentAttr=attr
    
    def getAttr(self):
        print '父类属性：',Parent.parentAttr
    def myMethod(self):
        print '父类方法'

class Child(Parent): #继承父类
    def __init__(self):
        print '调用子类构造函数'
        Parent.__init__(self)
    
    def childMethod(self):
        print '调用子类方法'
    
    def myMethod(self):
        print '子类方法重写父类方法'

c=Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.myMethod()

# 多继承
class A:
    pass
class B:
    pass
class C(A,B):
    pass

print C.__bases__


class Vector:
    def __init__(self,x,y):
        self.x,self.y=x,y
    
    def __str__(self):
        return 'Vector (%d, %d)' %(self.x,self.y)
    
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

v1=Vector(2,3)
v2=Vector(4,5)
v3=v1+v2
print v3

class JustCounter:
    __secretCount=0 #类的私有变量
    # publicCount=0 #类的公有变量

    def count(self):
        self.__secretCount+=1
   

counter=JustCounter()
counter.count()
counter.count()

#print counter.publicCount
print JustCounter._JustCounter__secretCount
print counter._JustCounter__secretCount



