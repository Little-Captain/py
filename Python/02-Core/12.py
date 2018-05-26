#!/usr/bin/env python

# 作用域
# globals local nonlocal

A = 100
B = 111


def xTest():

    a = 11
    b = 12
    print(locals())

xTest()
print(globals())

# LEGB 规则
# Python 使用 LEGB 的顺序来查找一个符号对应的对象
# locals -> enclosing function -> globals -> builtins
# locals: 当前所在命名空间（如函数、模块），函数的参数也属于命名空间内的变量
# enclosing: 外部嵌套函数的命名空间（闭包中常见）


def fun1():

    a = 10

    def fun2():

        # a 位于外部嵌套函数的命名空间
        print(a)

# globals: 全局变量，函数定义所在模块的命名空间
a = 1


def fun():

    global a
    a = 2

fun()
print(a)

# builtins: 内建模块的命名空间
# Python 在启动的时候会自动为我们载入很多内建的函数、类
# 可以使用 dir(__builtin__) 来查看
# 在Python中，有一个内建模块，该模块中有一些常用函数;在Python启动后，
# 且没有执行程序员所写的任何代码前，Python会首先加载该内建函数到内存