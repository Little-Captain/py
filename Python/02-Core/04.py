#!/usr/bin/env python

# 生成器: 在 Python 中, 一边循环, 一边计算的机制, 称为生成器(generator)

# 创建生成器方法1: 将列表生成式的[]改成()
L = [x*2 for x in range(5)]
print(L)

G = (x*2 for x in range(5))
print(G)

# 使用 next() 函数获得生成器的下一个返回值
# print(next(G))
# print(next(G))
# print(next(G))
for x in G:
    print(x)

# 生成器保存的是算法，每次调用 next(G) ，就计算出 G 的下一个元素的值，
# 直到计算到最后一个元素，没有更多的元素时，抛出 StopIteration 的异常
# 一般会使用 for 循环, 生成器是可迭代对象

# 创建生成器方法2: 使用函数实现. 用在推算算法比较复杂的时候
# def fib(times):
#     n = 0
#     a,b = 0,1
#     while n < times:
#         print(b)
#         a,b = b,a+b
#         n += 1
#     return 'done'
# print(fib(5))

print('-----------------------------------------')

def fib(times):
    n = 0
    a,b = 0,1
    while n < times:
        yield b
        a,b = b,a+b
        n += 1
    return 'done'

F = fib(5)

for x in F:
    print(x)

# 用 for 循环调用 generator 时，发现拿不到 generator 的 return 语句的返回值。
# 如果想要拿到返回值，必须捕获 StopIteration 错误，返回值包含在 StopIteration 的 value 中

print('-----------------------------------------')

g = fib(5)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print(e.value)
        break

print('---------------------')

def gen():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1

f = gen()
# for x in f:
#     print(x)

# 使用 __next__()
print(f.__next__())
print(f.__next__())

# 使用 send()
f = gen()
print(f.__next__())
print(f.send('haha'))

# 生成器是这样的函数, 它记住上一次返回时在函数体中的位置
# 对生成器函数的第二次（或第 n 次）调用跳转至该函数中间，而上次调用的所有局部变量都保持不变
# 生成器不仅“记住”了它的数据状态；生成器还“记住”了它在流控制构造中的位置
# 生成器的特点:
# 1. 节约内存
# 2. 迭代到下一次的调用时，所使用的参数都是第一次所保留下的，
# 即是说，在整个所有函数调用的参数都是第一次调用时保留的，而不是新创建的
