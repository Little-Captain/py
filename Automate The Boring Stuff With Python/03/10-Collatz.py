#!/usr/bin/env python

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    col = collatz(int(input('请输入:\n')))
    while col != 1:
        print(col)
        col = collatz(col)
    else:
        print(col)
except ValueError:
    print('请输入一个整数')
