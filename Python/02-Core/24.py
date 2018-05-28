#!/usr/bin/env python

# functools
# functools 是 python2.5 引人的, 一些工具函数放在此包里
import functools

print(dir(functools))


# 常用的 functools 函数

print('-------------------partial---------------------')

# 1. partial: 偏函数
# 把一个函数的某些参数设置默认值，返回一个新的函数，调用这个新函数会更简单

def showarg(*args, **kwargs):
    print(args)
    print(kwargs)

p1 = functools.partial(showarg, 1, 2, 3)
p1()
p1(4, 5, 6)
p1(a='python', b='little')

p2 = functools.partial(showarg, a=3, b='linux')
p2()
p2(1, 2)
p2(a='python', b='little')

# wraps
# 使用装饰器时，有一些细节需要被注意
# 被装饰后的函数其实已经是另外一个函数了(例如: 函数名等函数属性会发生改变)
# 添加后由于函数名和函数的doc发生了改变，对测试结果有一些影响
# Python的functools包中提供了一个叫wraps的装饰器来消除这样的副作用

print('-------------------wraps---------------------')

def note(func):

    'note function'

    def wrapper():
        'wrapper function'
        print('note something')
        return func()

    return wrapper

@note
def xTest():
    'test function'
    print('I am test')

xTest()
print(xTest.__doc__)

print('-------------------wraps---------------------')

import functools

def note(func):
    'note function'
    @functools.wraps(func)
    def wrapper():
        'wrapper function'
        print('note something')
        return func()
    return wrapper

@note
def xTest():
    'xTest function'
    print('I am xTest')

xTest()
print(xTest.__doc__)
