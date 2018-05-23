#!/usr/bin/env python

# 当定义的类型和运行的类型不一样, 体现的就是多态特性

class F1(object):
    def show(self):
        print('F1.show')

class S1(F1):
    def show(self):
        print('S1.show')

class S2(F1):
    def show(self):
        print('S2.show')

def Func(o):
    print(o.show())

s1_obj = S1()
Func(s1_obj)
s2_obj = S2()
Func(s2_obj)