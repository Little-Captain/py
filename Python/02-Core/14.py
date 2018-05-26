#!/usr/bin/env python

# 1. 浅拷贝
# 浅拷贝是对于一个对象的顶层拷贝
# 通俗的将就是：拷贝了引用，并没有拷贝内容

a = [11, 22, 33]
print(id(a))

b = a
print(id(b))

a. append(44)
print(a)
print(b)

a = {'name': 'xiaowang'}
print(id(a))

b = a
print(id(b))

a['id'] = 100
print(a)
print(b)

print('----------------------------------------')

# 深拷贝
# 深拷贝是对于一个对象所有层次的拷贝(递归)
import copy

a = [11, 22, 33]
print(id(a))

b = copy.deepcopy(a)
print(id(b))

a.append(44)
print(a)
print(b)

print('----------------------------------------')

a = [11, 22, 33]
b = [44, 55, 66]
c = (a, b)
# 深拷贝, 递归
d = copy.deepcopy(c)
a.append(77)
print(a)
print(b)
print(c)
print(d)

# 浅层拷贝, 对可变与不可变类型的拷贝, 行为不同, 不递归
e = copy.copy(c)
a.append(88)
print(a)
print(b)
print(c)
print(id(c))
print(d)
print(id(d))
print(e)
print(id(e))

print('-----------------------------------')

# 其他拷贝方式
# 浅拷贝对不可变类型和可变类型的 copy 不同
# 可变: 创建新对象, 但不递归 copy
a = [11, 22, 33]
b = copy.copy(a)
print(id(a))
print(id(b))
a.append(44)
print(a)
print(b)

# 不可变: 指针赋值
a = (11, 22, 33)
b = copy.copy(a)
print(id(a))
print(id(b))

print('-----------------------------------')

a = 'abc'
b = a[:]
c = 'abc'
print(id(a))
print(id(b))
print(id(c))

print('-----------------------------------')
d = dict(name='zhangsan', age=23)
co = d.copy()
print(id(d))
print(id(co))

print('-----------------------------------')
a = list(range(10))
b = list(a)
print(id(a))
print(id(b))

print('-----------------------------------')
a = (1, 2, 3)
b = copy.copy(a)
print(id(a))
print(id(b))
