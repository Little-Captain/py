#!/usr/bin/env python

# 确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，
# 这个类称为单例类，单例模式是一种对象创建型模式。

class Singleton(object):

    # 类属性
    __instance = None
    # 控制__init__方法只执行一次
    __first_init = False

    def __init__(self, age, name):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton.__first_init = True

    # 类对象 cls
    def __new__(cls, age, name):

        if not cls.__instance:
            cls.__instance = super().__new__(cls)

        return cls.__instance

a = Singleton(18, 'dongGe')
print(a.age)
b = Singleton(8, 'dongGe')
print(a.age)
print(b.age)

print(id(a))
print(id(b))

a.age = 19
print(b.age)
