#!/usr/bin/env python

# 进程的创建-fork

# 很粗糙的区别: 进程和程序
# 程序: 没有运行的代码
# 进程: 运行中的代码. 进程，除了包含代码以外，还有需要运行的环境等

# fork 函数
# os 模块: 封装了一些常见的系统调用
# fork: 可以在 Python 程序中创建子进程

# import os
#
# # 注意，fork函数，只在 Unix/Linux/Mac 上运行，windows不可以
# # 新建的子进程的 pid != 0, 这个 pid 被父进程获得, 也就是父进程中返回子进程的 id 号
# # 在子进程中, 这个 pid == 0
# pid = os.fork()
# if pid == 0:
#     print('哈哈-1')
# else:
#     print('哈哈-2')

# 1. 程序执行到os.fork()时，操作系统会创建一个新的进程（子进程），
# 然后复制父进程的所有信息到子进程中
# 2. 然后父进程和子进程都会从fork()函数中得到一个返回值，
# 在子进程中这个值一定是0，而父进程中是子进程的 id 号
# 3. 普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
# 然后，分别在父进程和子进程内返回。
# 4. 子进程永远返回0，父进程返回子进程的ID
# 5. 一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，
# 而子进程只需要调用 getppid ()就可以拿到父进程的ID

# getpid getppid 函数

import os

rpid = os.fork()
if rpid < 0:
    print('fork 调用失败')
elif rpid == 0:
    print('我是子进程(%s), 我的父进程是(%s)'%(os.getpid(), os.getppid()))
else:
    print('我是父进程(%s), 我的子进程是(%s)'%(os.getpid(), rpid))
