#!/usr/bin/env python

# 列表推导式

# 基本
a = [x for x in range(4)]
print(a)

a = [x for x in range(3, 4)]
print(a)

a = [x for x in range(3, 19)]
print(a)

# 循环的过程中使用 if
a = [x for x in range(3, 10) if x % 2 == 0]
print(a)

a = [x for x in range(3, 10) if x % 2 != 0]
print(a)

a = [x for x in range(3, 10)]
print(a)

# 嵌套 for 循环
a = [(x, y) for x in range(1, 3) for y in range(3)]
print(a)

a = [(x, y, z) for x in range(1, 3) for y in range(3) for z in range(4, 6)]
print(a)

a = [[x, x+1, x+2] for x in range(1, 100, 3)]
print(a)
