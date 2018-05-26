#!/usr/bin/env python

from collections import Iterable
from collections import Iterator

# 迭代器是访问集合元素的一种方式
# 迭代器是一个可以记住遍历的位置的对象
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束
# 迭代器只能往前不会后退

# 可迭代对象

# 可直接用于 for 循环的数据类型有:
# 1. 集合数据类型: list, tuple, dict, set, str
# 2. generator: 生成器, 带有 yield 的 generator function
# 可直接用于 for 循环的对象称为可迭代对象(Iterable)

# 判断是否可以迭代
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print('------------------------------------------')

# 迭代器
# 可以被 next() 函数调用并不断返回下一个值的对象称为迭代器: Iterator
# 判断是否是迭代器
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance(100, Iterator))

print('------------------------------------------')

# iter() 函数
# 生成器都是 Iterator 对象
# list 、 dict 、 str 虽然是 Iterable ，却不是 Iterator
# 把 list 、 dict 、 str 等 Iterable 变成 Iterator 可以使用 iter() 函数
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

# 总结
# 1. 凡是可作用于 for 循环的对象都是 Iterable 类型
# 2. 凡是可作用于 next() 函数的对象都是 Iterator 类型
# 3. Iterable 可以通过使用 iter() 函数转换为 Iterator
