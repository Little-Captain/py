#!/usr/bin/env python

# 匹配任何单个字符
# 点号(.)不能匹配一个换行符\n 或者非字符

import re

anyend = '.end'
m = re.match(anyend, 'bend')
if m is not None:
    print(m.group())
else:
    print("None")

m = re.match(anyend, 'end')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.match(anyend, '\nend')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.search(anyend, 'The end.')
if m is not None:
    print(m.group())
else:
    print('None')

patt314 = '3.14'
pi_patt = '3\.14'

m = re.match(pi_patt, '3.14')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.match(patt314, '3014')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.match(patt314, '3.14')
if m is not None:
    print(m.group())
else:
    print('None')
