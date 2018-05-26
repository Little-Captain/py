#!/usr/bin/env python

# import 搜索路径

import importlib
import sys

print(sys.path)

# 程序执行时, 改变导入模块的搜索路径
sys.path.append('~/.bin')
sys.path.insert(0, '/')

print(sys.path)

# 重新导入模块, 需要调用 reload(模块名) 方法
print(importlib.reload(sys))