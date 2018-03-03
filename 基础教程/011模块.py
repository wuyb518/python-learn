#!/usr/bin/python
# _*_ coding:UTF-8 _*_

# 模块

# Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。

# 模块让你能够有逻辑地组织你的 Python 代码段。

# 把相关的代码分配到一个模块里能让你的代码更好用，更易懂。

# 模块能定义函数，类和变量，模块里也能包含可执行的代码。

# 模块搜索路径

# 当你导入一个模块，Python 解析器对模块位置的搜索顺序是：

# 1、当前目录
# 2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
# 3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
# 模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

# PYTHONPATH 变量
# 作为环境变量，PYTHONPATH 由装在一个列表里的许多目录组成。PYTHONPATH 的语法和 shell 变量 PATH 的一样。

# 在 Windows 系统，典型的 PYTHONPATH 如下：

# set PYTHONPATH=c:\python27\lib;
# 在 UNIX 系统，典型的 PYTHONPATH 如下：

# set PYTHONPATH=/usr/local/lib/python

#命名空间和作用域名

# 变量是拥有匹配对象的名字（标识符）。命名空间是一个包含了变量名称们（键）和它们各自相应的对象们（值）的字典。

# 一个 Python 表达式可以访问局部命名空间和全局命名空间里的变量。如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量。

# 每个函数都有自己的命名空间。类的方法的作用域规则和通常函数的一样。

# Python 会智能地猜测一个变量是局部的还是全局的，它假设任何在函数内赋值的变量都是局部的。

# 因此，如果要给函数内的全局变量赋值，必须使用 global 语句。

# global VarName 的表达式会告诉 Python， VarName 是一个全局变量，这样 Python 就不会在局部命名空间里寻找这个变量了。

# 例如，我们在全局命名空间里定义一个变量 Money。我们再在函数内给变量 Money 赋值，然后 Python 会假定 Money 是一个局部变量。然而，我们并没有在访问前声明一个局部变量 Money，结果就是会出现一个 UnboundLocalError 的错误。取消 global 语句的注释就能解决这个问题。

# dir()函数
# dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。

# 返回的列表容纳了在一个模块里定义的所有模块，变量和函数。如下一个简单的实例：

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 导入内置math模块
import math
content=dir(math)
print content

# 在这里，特殊字符串变量__name__指向模块的名字，__file__指向该模块的导入文件名。

