#!/usr/bin/env python

# 1. 私有属性添加getter和setter方法


class Money(object):

    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('error: Not Int')

a = Money()
print(a.getMoney())
a.setMoney(10)
print(a.getMoney())

# 2. 使用 property 升级 getter 和 setter 方法

class Money(object):

    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('error: Not Int')

    money = property(getMoney, setMoney)

a = Money()
print(a.money)
a.money = 100
print(a.money)
a.setMoney(200)
print(a.getMoney())

# 3. 使用 property 取代 getter和setter 方法
# @property成为属性函数，可以对属性赋值时做必要的检查，并保证代码的清晰短小
# a. 将方法转换为只读
# b. 重新实现一个属性的设置和读取方法,可做边界判定

class Money(object):

    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('error: Not Int')

a = Money()
print(a.money)
a.money = 100
print(a.money)
