#!/usr/bin/env python

# 当删除一个对象时，python解释器会默认调用 __del__() 方法
# del 是让对象的引用计数减1, 如果对象的引用计数为0, __del__() 方法就会被调用

import time

class Animal(object):

    def __init__(self, name):
        print('__init__ 方法被调用')
        self.__name = name


    def __del__(self):
        print('__del__ 方法被调用')
        print('%s对象马上就要被干掉了...'%self.__name)

dog = Animal('dog1')
del dog

cat = Animal('cat1')
cat2 = cat
cat3 = cat

print('del 1')
del cat
print('del 2')
del cat2
print('del 3')
del cat3
time.sleep(2)
