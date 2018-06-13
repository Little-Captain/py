#!/usr/bin/env python

# multiprocessing: 跨平台版本的多进程模块
# multiprocessing 模块提供了一个 Process 类来代表一个进程对象

# 启动一个子进程并等待其结束
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('子进程运行中, name=%s, pid=%d...'%(name, os.getpid()))

if __name__ == '__main__':
    print('父进程%d.'%os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('子进程将要执行')
    p.start()
    p.join()
    print('子进程已结束')

#