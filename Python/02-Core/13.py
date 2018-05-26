#!/usr/bin/env python

import copy

# == is
a = [11, 22, 33]
b = a

print(b == a)
print(a is b)

c = copy.deepcopy(a)
print(a == c)
print(a is c)

# is 是比较两个引用是否指向了同一个对象（引用比较）
# == 是比较两个对象是否相等
