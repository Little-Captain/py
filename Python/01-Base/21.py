#!/usr/bin/env python

try:
    # 可能出现异常的代码
    print('----test1----')
    # open('123.txt', 'r')
    print('----test2----')
    # print(num)
# except (IOError, NameError) as result:
# 捕获所有异常
except Exception as result:
    # 使用元组, 一次捕获多个异常
    # 处理错误的代码
    print(result)
else:
    print('没有任何异常')
