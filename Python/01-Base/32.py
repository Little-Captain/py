#!/usr/bin/env python

a = set()
print(type(a))

b = [1, 2, 3, 4]
print(b)

c = set(b)
print(type(c))
print(c)

d = list(c)
print(d)

e = tuple(d)
print(e)

f = list(e)
print(f)

g = set(e)
print(g)

# 使用set，可以快速的完成对list中的元素去重复的功能