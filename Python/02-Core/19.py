#!/usr/bin/env python
#-*-coding:utf-8-*-

# 垃圾回收

# 1. 小整数对象池
# a. [-5, 257)
# b. 单个字母
# 这些对象提前创建好, 不会被垃圾回收
# 在一个 Python 的程序中，所有位于这个范围内的整数使用的都是同一个对象
a = 13
print(id(a))
b = 13
print(id(b))

# 2. 大整数对象池 ???
# 每一个大整数，均创建一个新的对象

a = 1314123
print(id(a))
b = 1314123
print(id(b))

# 3. intern 机制
# 单个单词，不可修改，默认开启intern机制，共用对象
a1 = "HelloWorld"
a2 = "HelloWorld"
a3 = "HelloWorld"
a4 = "HelloWorld"
a5 = "HelloWorld"
a6 = "HelloWorld"
a7 = "HelloWorld"
a8 = "HelloWorld"
a9 = "HelloWorld"
print(id(a1))
print(id(a2))

# 字符串（含有空格），不可修改，没开启intern机制，不共用对象，引用计数为0，销毁 ???
a1 = 'hello world'
a2 = 'hello world'
print(id(a1))
print(id(a2))

# 数值类型和字符串类型在 Python 中都是不可变的，
# 这意味着你无法修改这个对象的值，每次对变量的修改，
# 实际上是创建一个新的对象

a = 1
print(id(a))
a += 1
print(id(a))
