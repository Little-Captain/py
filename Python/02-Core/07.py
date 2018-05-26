#!/usr/bin/env python

# 装饰器

def foo():
    print('foo')

print(foo)
print(foo())


def foo():
    print('foo')

foo = lambda x: x + 1
foo(1)


############### 基础平台提供的功能如下 ###############

def w1(func):

    def inner():
        # 验证
        func()

    return inner


@w1
def f1():
    print('f1')


@w1
def f2():
    print('f2')


@w1
def f3():
    print('f3')


@w1
def f4():
    print('f4')

# python解释器会从上到下解释代码
# 1. def w1(func): ==> 将w1函数加载到内存
# 2. @w1

# @w1: 执行w1函数 ，并将 @w1 下面的函数作为w1函数的参数
# 即：@w1 <=> w1(f1)
# w1 的返回值: 将执行完的 w1 函数返回值赋值给 @w1 下面的函数的函数名 f1
# 即将 w1 的返回值再重新赋值给 f1
