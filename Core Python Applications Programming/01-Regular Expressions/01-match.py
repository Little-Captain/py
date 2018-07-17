#!/usr/bin/env python

# match : 匹配
# 使用 match() 方法匹配字符串
# match() 试图从字符串的起始部分开始匹配模式

import re

m = re.match('foo', 'foo')
if m is not None:
    print(m.group())
    print(m)
else:
    print("None")

print('------------------')

m = re.match('foo', 'bar')
if m is not None:
    print(m.group())
else:
    print('None')

print('------------------')

m = re.match('foo', 'food on the table')
if m is not None:
    print(m.group())
else:
    print('None')

print('------------------')
