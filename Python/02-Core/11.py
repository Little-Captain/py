#!/usr/bin/env python

# 循环导入

# a.py
#
# from b import b
#
# print '---------this is module a.py----------'
# def a():
#     print("hello, a")
#     b()
#
# a()

# b.py
#
# from a import a
#
# print '----------this is module b.py----------'
# def b():
#     print("hello, b")
#
# def c():
#     a()
# c()

# 如何避免循环导入
# 1. 程序设计上分层，降低耦合
# 2. 导入语句放在后面需要导入时再导入，例如放在函数体内导入