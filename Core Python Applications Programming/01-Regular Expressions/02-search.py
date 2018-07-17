#!/usr/bin/env python

# search : 搜索
# 使用 search() 在一个字符串中查找模式
# 想要搜索的模式出现在一个字符串中间部分的概率，远大于出现在字符串起始部分的概率
# search 与 match 的不同之处
# search 会用它的字符串参数, 在任意位置对给定正则表达式
# 模式搜索第一次出现的匹配情况
# 如果搜索到成功的匹配, 就返回一个匹配对象, 否则返回 None

import re

m = re.match('foo', 'seafood')
if m is not None:
    print(m.group())
else:
    print('None')

print('-----------------')

m = re.search('foo', 'seafood')
if m is not None:
    print(m.group())
else:
    print('None')
