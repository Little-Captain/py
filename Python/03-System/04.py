#!/usr/bin/env python

# 多次 fork

import os
import time

pid = os.fork()
if pid == 0:
    print('哈哈-1')
else:
    print('哈哈-2')

pid = os.fork()
if pid == 0:
    print('哈哈-3')
else:
    print('哈哈-4')

time.sleep(1)

# 父进程、子进程执行顺序没有规律，完全取决于操作系统的调度算法