#!/usr/bin/env python

# 集合 set
# 集合与之前列表、元组类似，可以存储多个数据，但是这些数据是不重复的
# 集合对象还支持 union(联合), intersection(交), difference(差)
# sysmmetric_difference(对称差集)等数学运算.

x = set('abcd')
print(x)
print(type(x))

y = set(['h', 'e', 'l', 'l', 'o'])
print(y)

z = set('spam')
print(z)

# 交集
print(y & z)
print(x & z)

# 并集
print(x | z)
print(x | y)

# 差集
print(x - y)

# 对称差集: 在x或z中，但不会同时出现在二者中
print(x ^ z)

print(len(x))
print(len(y))
print(len(z))
