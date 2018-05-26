#!/usr/bin/env python


def xtest1():
    print('--- in test1 func ---')

xtest1()

ret = xtest1
print(id(ret))
print(id(xtest1))

# 闭包


def func(number):
    # 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，
    # 那么将这个函数以及用到的一些变量称之为闭包
    def test_in(number_in):
        print('in test_in 函数, number_in is %d'%number_in)
        return number + number_in

    return test_in

ret = func(20)
print(ret(100))
print(ret(200))

# 内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包


def counter(start=0):

    count = [start]

    def incr():
        count[0] += 1
        return count[0]

    return incr

c1 = counter(5)
print(c1())
print(c1())
c1 = counter(100)
print(c1())
print(c1())

print('-----------------------------------')

def counter1(start=0):

    def incr():
        nonlocal start
        start += 1
        return start
    return incr

c1 = counter1(5)
print(c1())
print(c1())

c2 = counter1(50)
print(c2())
print(c2())

print(c1())
print(c1())

print(c2())
print(c2())


def line_conf(a, b):

    def line(x):
        return a * x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5))
print(line2(5))

# 闭包的思考
# 1. 闭包优化了变量，原来需要类对象完成的工作，闭包也可以完成
# 2. 由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
