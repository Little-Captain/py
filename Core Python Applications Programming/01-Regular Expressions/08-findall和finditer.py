#!/usr/bin/env python

import re

# 使用 findall() 和 finditer() 查找每一次出现的位置

# findall() 查询字符串中某个正则表达式模式全部的非重复出现情况
# findall() 总是返回一个列表, 没有找到返回空列表

m = re.findall('car', 'car')
print(m)

m = re.findall('car', 'scary')
print(m)

m = re.findall('car', 'carry the barcardi to the car')
print(m)
