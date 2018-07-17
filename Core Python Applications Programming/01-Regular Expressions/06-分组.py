#!/usr/bin/env python

# 重复、特殊字符以及分组
# 正则表达式中最常见的情况包括:
# 1. 特殊字符的使用
# 2. 正则表达式模式的重复出现
# 3. 使用圆括号对匹配模式的各部分进行分组和提取操作
import re

# 重复
patt = '\w+@(\w+\.)?\w+\.com'

print(re.match(patt, 'nobody@xxx.com').group())
print(re.match(patt, 'nobody@www.xxx.com').group())

patt = '\w+@(\w+\.)*\w+\.com'

print(re.match(patt, 'nobody@www.xxx.yyy.zzz.com').group())

# 分组
m = re.match('\w\w\w-\d\d\d', 'abc-123')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.match('\w\w\w-\d\d\d', 'abc-xyz')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.groups())
else:
    print('None')

m = re.match('ab', 'ab')
if m is not None:
    print(m.group())
    print(m.groups())
else:
    print('None')

m = re.match('(ab)', 'ab')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.groups())
else:
    print('None')

m = re.match('(a)(b)', 'ab')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.groups())
else:
    print('None')

m = re.match('(a(b))', 'ab')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.groups())
else:
    print('None')

