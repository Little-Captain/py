#!/usr/bin/env python

# __slots__

# 动态语言: 可以在运行的过程中, 修改代码
# 静态语言: 编译时已近确定好代码, 运行过程中不能修改

# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class Person(object):
    __slots__ = ('name', 'age')

P = Person()
P.name = '老王'
P.age = 20
# P.score = 100

# 使用__slots__要注意: __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class Test(Person):
    pass

t = Test()
t.score = 100
print(t.score)
