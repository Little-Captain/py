#!/usr/bin/env python

# 进程池 Pool

# 当需要创建的子进程数量不多时，可以直接利用 multiprocessing 中的 Process 动态成生多个进程，
# 如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，就可以用到 multiprocessing 模块
# 提供的 Pool 方法