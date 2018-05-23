#!/usr/bin/env python

class base(object):
    def test(self):
        print('---- base test')

class A(base):
    def test(self):
        print('--- A test')

class B(base):
    def test(self):
        print('--- B test')

class C(A, B):
    pass

obj_c = C()
obj_c.test()

# 可以查看C类的对象搜索方法时的先后顺序
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.base'>, <class 'object'>)
print(C.__mro__)