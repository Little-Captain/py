#!/usr/bin/env python

# 多进程修改全局变量
import os
import time

num = 0

pid = os.fork()

if pid == 0:
    num += 1
    print('哈哈-1------num=%d'%num)
else:
    time.sleep(1)
    num += 1
    print('哈哈-2------num=%d'%num)

# 多进程中，每个进程中所有数据（包括全局变量）都各有拥有一份，互不影响
