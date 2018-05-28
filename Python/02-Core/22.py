#!/usr/bin/env python

# 内建函数
# 使用 dir(__builtins__) 查看

# 常用的内建函数介绍

# 1. range
# range(stop): 0 开始, 不包括 stop
# range(start, stop[, step])
# python2 中 range 返回列表，python3 中 range返回一个 range 对象(通过 list 函数转换)
a = range(5)
print(a)
print(list(a))

# 2. map
# 映射
# map(function, sequence[, sequence, ...]) -> map 对象
# sequence: 是一个或多个序列,取决于function需要几个参数
# 返回值是一个 map 对象(通过 list 函数转换)
print(map(lambda x: x*x, [1, 2, 3]))
print(map(lambda x, y: x+y, [1, 2, 3], [4, 5, 6]).__class__)


def f1(x, y):
    return (x, y)

l1 = [0, 1, 2, 3, 4, 5, 6]
l2 = ['Sun', 'M', 'T', 'W', 'T', 'F', 'S']
l3 = map(f1, l1, l2)
print(list(l3))

# filter
# 过滤
# filter(function or None, sequence) -> filter 对象
# function: 接受一个参数，返回布尔值 True 或 False
# sequence:序列可以是 str，tuple，list
# 返回值的类型为 filter 对象
print(filter(lambda x: x%2, [1, 2, 3, 4]))
print(filter(None, 'she').__class__)
print(list(filter(lambda x: x%2, [1, 2, 3, 4])))
print(tuple(filter(None, 'she')))

# reduce
# 整合
# reduce(function, sequence[, initial]) -> value
# function: 该函数有两个参数
# sequence: 序列可以是 str，tuple，list
# initial: 初始值
# 返回
# Python3 中 reduce 在 functools 中
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4]))
print(reduce(lambda x, y: x+y, [1, 2, 3, 4], 5))
print(reduce(lambda x, y: x+y, ['aa', 'bb', 'cc'], 'dd'))

# sorted
# sorted(iterable, /, *, key=None, reverse=False) -> list
# iterable: 可迭代对象
# reverse: 是否降序
print(sorted([1, 3, 2, 0, 6, 4]))
print(sorted([1, 3, 2, 0, 6, 4], reverse=True))
print(sorted(['dd', 'aa', 'cc', 'bb']))
print(sorted(['dd', 'aa', 'cc', 'bb'], reverse=True))
print(sorted('abc').__class__)
print(sorted((1, 2, 3)).__class__)
