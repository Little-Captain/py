#!/usr/bin/env python

# 模块
# 可以引入: 函数, 全局变量, 类等等

# Python解析器对模块位置的搜索顺序
# 当前目录
# shell 变量 PYTHONPATH 下的每个目录
# Python默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
# 模块搜索路径存储在 sys 模块的 sys.path 变量中。变量里包含 当前目录，PYTHONPATH 和 由安装过程决定的默认目录

import math
from math import sin
from math import *
import time as tt
from time import sleep as sp

print(math.sqrt(2))
print(sin(30))
print(cos(30))
tt.sleep(1)
sp(3)
