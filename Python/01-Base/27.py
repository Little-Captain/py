#!/usr/bin/env python

# import 模块/包
# from 模块/包 import 模块/包/类/全局变量/...

# import 文件.模块
# import msg.sendmsg
# from 文件夹 import 模块
# from msg import sendmsg
# 但不能使用 from msg import *, 如果要使用必须创建 __init__.py 文件
from msg import *
import msg
msg.recvmsg.recvmsg()
sendmsg.sendmsg()
recvmsg.recvmsg()

# 包将有联系的模块组织在一起，即放到同一个文件夹下，并且在这个文件夹创建
# 一个名字为__init__.py 文件，那么这个文件夹就称之为包
# 有效避免模块名称冲突问题，让应用组织结构更加清晰
# __init__.py 文件的作用: 控制着包的导入行为
# 如果 __init__.py 为空, 那么仅仅是把这个包导入，不会导入包中的模块
# 在__init__.py 文件中，定义一个 __all__ 变量，它控制着 from 包名 import * 时导入的模块
# __init__.py 中的代码, 会在导入时被执行
# __init__.py 就是初始化包文件. from-import 语句导入子包时需要用到它。 如果没有用到，他们可以是空文件
