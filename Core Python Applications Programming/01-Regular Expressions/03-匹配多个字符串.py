#/!/usr/bin/env python

# 匹配多个字符串(择一匹配)

import re

bt = 'bat|bet|bit'

m = re.match(bt, 'bat')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.match(bt, 'blt')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.match(bt, 'He bit me!')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.search(bt, 'He bit me!')
if m is not None:
    print(m.group())
else:
    print('None')
