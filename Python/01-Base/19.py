#!/usr/bin/env python

# __new__至少要有一个参数cls
# __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，
# 可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
# __init__有一个参数self，就是这个__new__返回的实例，
# __init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
# __new__ 方法: 创建对象
# __init__ 方法: 初始化对象
class A(object):

    def __init__(self):
        print('__init__')

    def __new__(cls):
        print('__new__')
        return super().__new__(cls)

A()