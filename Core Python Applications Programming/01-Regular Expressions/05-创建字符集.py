#!/usr/bin/env python

# 创建字符集

import re

m = re.match('[cr][23][dp][o2]', 'c3po')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.match('[cr][23][dp][o2]', 'c2do')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.match('r2d2|c3po', 'c2do')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.match('r2d2|c3po', 'r2d2')
if m is not None:
    print(m.group())
else:
    print('None')
