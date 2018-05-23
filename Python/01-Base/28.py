#!/usr/bin/env python
# 嵌套包的目录结构
# Phone/
#     __init__.py
#     common_util.py
#     Voicedta/
#         __init__.py
#         Pots.py
#         Isdn.py
#     Fax/
#         __init__.py
#         G3.py
#     Mobile/
#         __init__.py
#         Analog.py
#         igital.py
#     Pager/
#         __init__.py
#         Numeric.py

# 使用点语法导入子模块
# import Phone.Mobile.Analog
# Phone.Mobile.Analog.dial()

# 导入子模块
# from Phone import Mobile
# Mobile.Analog.dial('555-1212')

# from Phone.Mobile import Analog
# Analog.dial('555-1212')

# 可以一直沿子包的树状结构导入
# from Phone.Mobile.Analog import dial
# dial('555-1212')

# 支持 from-import all 语句
# from package.module import *

# 然而，这样的语句会导入哪些文件取决于操作系统的文件系统。
# 所以我们在__init__.py 中加入 __all__ 变量。该变量包含执行这样的语句时应该导入的模块的名字。
# 它由一个模块名字符串列表组成.