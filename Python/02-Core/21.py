#!/usr/bin/env python

# 内建属性

class Person(object):
    pass

print(dir(Person))

# 常用方法和属性        说明                触发方式
# __init__           构造初始化函数        创建实例后,赋值时使用,在__new__后
# __new__            创建实例函数          创建实例时
# __class__          实例所在的类          实例.__class__
# __str__            实例字符串表示,可读性   print(类实例),如没实现，使用repr结果
# __repr__           实例字符串表示,准确性   类实例 回车 或者 print(repr(类实例))
# __del__            析构                 del删除实例(引用计数为0, 或 gc时)
# __dict__           实例自定义属性         实例.__dict__
# __doc__            类文档,子类不继承       help(类或实例)
# __getattribute__   属性访问拦截器          访问实例属性时
# __bases__          类的所有父类构成元素      类名.__bases__

# __getattribute__ 实例


class Little(object):

    def __init__(self, subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    # 属性访问时拦截器
    def __getattribute__(self, obj):
        if obj == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:
            return object.__getattribute__(self, obj)

    def show(self):
        print('this is Little')

s = Little('python')
print(s.subject1)
print(s.subject2)

# __getattribute__ 的注意点


class Person(object):

    def __getattribute__(self, obj):
        print('---test---')
        if obj.startswith('a'):
            return 'haha'
        else:
            # 获取 self 的 test 属性
            # 又会走 __getattribute__ 方法
            # 然后再到这儿
            # 参数无限递归调用
            # 堆栈溢出, 程序崩溃
            return self.test

    def test(self):
        print('heihei')

t = Person()
print(t.a)
# 程序会死掉
print(t.b)

# 注意：不要在 __getattribute__ 方法中调用 self.xxxx
