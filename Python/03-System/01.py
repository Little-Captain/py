#!/usr/bin/env python

# 进程

# 模拟“唱歌跳舞”这件事情(单任务)

from time import sleep


def sing():
    for i in range(3):
        print('正在唱歌...%d'%i)
        sleep(1)


def dance():
    for i in range(3):
        print('正在跳舞...%d'%i)
        sleep(1)

if __name__ == '__main__':
    sing()
    dance()

# 多任务: 操作系统轮流让各个任务交替执行
# 真正的并行执行多任务只能在多核CPU上实现
# 由于任务数量远远多于 CPU 的核心数量
# 操作系统也会自动把很多任务轮流调度到每个核心上执行