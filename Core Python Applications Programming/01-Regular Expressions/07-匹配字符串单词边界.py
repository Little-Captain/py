#!/usr/bin/env python

# 匹配字符串的起始和结尾以及单词边界
# 表示位置的操作符更多用于搜索而不是匹配
# 因为匹配总是从字符串开始位置进行匹配

import re

m = re.search('^The', 'The end.')
if m is not None:
    print('')