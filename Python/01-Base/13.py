#!/usr/bin/env python

# 私有属性, 不通过对象直接访问, 但可以通过方法访问
# 私有方法, 不通过对象直接访问
# 私有属性、方法, 不会被子类继承, 也不能被访问
# 一般情况, 私有属性、方法都是不对外公开的, 往往用来做内部的事情
class Animal(object):

    def __init__(self, name='动物', color='白色'):
        self.__name = name
        self.color = color

    def __test(self):
        print(self.__name)
        print(self.color)

    def test(self):
        print(self.__name)
        print(self.color)


class Dog(Animal):

    def dogTest1(self):
        print(self.color)

    def dogTest2(self):
        self.test()


A = Animal()
print(A.color)
A.test()

print('------------------')

D = Dog(name='小花狗', color='黄色')
D.dogTest1()
D.dogTest2()