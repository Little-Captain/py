#!/usr/bin/env python

# 匹配字符串的起始和结尾以及单词边界
# 表示位置的操作符更多用于搜索而不是匹配
# 因为匹配总是从字符串开始位置进行匹配

import re

m = re.search('^The', 'The end.')
if m is not None:
    print(m.group())
else:
    print("None")

m = re.search('^The', 'end. The')
if m is not None:
    print(m.group())
else:
    print('None')

# r'': 代表非转义的原始字符串
# raw
m = re.search(r'\bthe', 'bite the dog')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.search(r'\bthe', 'bitethe dog')
if m is not None:
    print(m.group())
else:
    print('None')

m = re.search(r'\Bthe', 'bitethe dog')
if m is not None:
    print(m.group())
else:
    print('None')