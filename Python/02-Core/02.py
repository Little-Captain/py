#!/usr/bin/env python

import types
# 动态语言特性
# 在运行时可以改变其结构的语言

#  运行的过程中给对象绑定(添加)属性
class Person(object):

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

P = Person('小明', '24')
print(P.name)
print(P.age)

P.sex = 'male'
print(P.sex)

P1 = Person('小丽', '25')
# print(P1.sex)
# 异常
# 如果是给类绑定的属性就不会异常, 因为这是类属性
Person.sex = None
P1 = Person('小丽', '25')
# 优先访问实例属性, 再访问类属性
print(P1.sex)

# 运行的过程中给类绑定(添加)方法

class Person(object):

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def eat(self):
        print('eat food')

# 定义一个实例方法
def run(self, speed):
    print('%s在移动, 速度是 %d km/h'%(self.name, speed))

# 定义一个类方法
@classmethod
def testClass(cls):
    print('-----class method')
    cls.num = 100

# 定义一个静态方法
@staticmethod
def testStatic():
    print('----static method')

P = Person('老王', 24)
P.eat()
# P.run() 异常
# 给对象绑定实例方法
P.run = types.MethodType(run, P)
P.run(180)

# 给Person类绑定类方法
Person.testClass = testClass
Person.testClass()
print(Person.num)

# 给Person类绑定静态方法
Person.testStatic = testStatic
Person.testStatic()

# 运行工程中删除属性、方法
# 1. del 对象.属性名
# 2. delattr(对象, '属性名')

# 为了避免动态特性带来的坑, 可以使用 __slots__
