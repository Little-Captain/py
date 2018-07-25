#!/usr/bin/env python

# 在一个函数中，一个变量要么总是全局变量，要么总是局部变量!!!

def spam():
    eggs = 'sss'
    print(eggs)
    # global eggs
    eggs = 'spam local'

eggs = 'global'
spam()