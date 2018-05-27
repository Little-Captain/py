#!/usr/bin/env python

# python 中的垃圾回收机制
# 引用计数为主, 分代收集为辅

# 引用计数的优点:
# 1. 简单
# 2. 实时性：一旦没有引用，内存就直接释放了。不用像其他机制等到特定时机。
# 实时性还带来一个好处：处理回收内存的时间分摊到了平时
# 引用计数的缺点:
# 1. 维护引用计数消耗资源
# 2. 循环引用(致命, 如果不小心引入, 就是内存泄漏)

# GC系统: GC系统所承担的工作远比"垃圾回收"多得多
# 1. 为新生成的对象分配内存
# 2. 识别垃圾对象
# 3. 从垃圾对象那回收内存
# GC系统就像心脏一样为身体持续提供血液和营养物质

# 使用 GC 模块

# Python中的垃圾回收是以引用计数为主，分代收集为辅

# 导致引用计数 +1 的情况
# 1. 对象被创建
# 2. 对象被引用
# 3. 对象被作为参数，传入到一个函数中
# 4. 对象作为一个元素，存储在容器中

# 导致引用计数-1的情况
# 1. 对象的别名被显式销毁
# 2. 对象的别名被赋予新的对象
# 3. 一个对象离开它的作用域
# 4. 对象所在的容器被销毁，或从容器中删除对象

# 查看一个对象的引用计数
import sys

a = 'hello world'
print(sys.getrefcount(a))
b = 'hello world'
print(sys.getrefcount(b))

# 循环引用导致内存泄露
# 引用计数的缺陷是循环引用的问题
import gc
import time


class ClassA(object):

    def __init__(self):
        print('object born, id: %s'%str(hex(id(self))))

    def __del__(self):
        print('object del, id: %s'%str(hex(id(self))))

def f2():
    c1 = ClassA()
    c2 = ClassA()
    c1.t = c2
    c2.t = c1
    # 只有在程序执行完毕后才会销毁对象 c1 c2
    del c1
    del c2

def f3():
    print('---0---')
    c1 = ClassA()
    c2 = ClassA()
    c1.t = c2
    c2.t = c1
    print('---1---')
    del c1
    del c2
    print('---2---')
    print(gc.garbage)
    print('---3---')
    # 显式执行垃圾回收
    print(gc.collect())
    print('---4---')
    print(gc.garbage)
    print('---5---')

if __name__ == '__main__':
    # 情况1
    # 不启动 gc
    # gc.disable()
    #
    # f2()
    # time.sleep(10)
    # 情况2
    gc.set_debug(gc.DEBUG_LEAK)
    f3()

# 垃圾回收后的对象会放在 gc.garbage 列表里面
# gc.collect() 会返回不可达的对象数目

# 触发垃圾回收的三种情况
# 1. 调用gc.collect()
# 2. 当gc模块的计数器达到阀值的时候
# 3. 程序退出的时候

# gc模块常用功能
# gc模块提供一个接口给开发者设置垃圾回收的选项
# 采用引用计数的方法管理内存的一个缺陷是循环引用，
# 而gc模块的一个主要功能就是解决循环引用的问题

# 常用函数
# 1. gc.set_debug(flags) 设置 gc 的 debug 日志，一般设置为 gc.DEBUG_LEAK
# 2. gc.collect([generation]) 显式进行垃圾回收，可以输入参数，
# 0代表只检查第一代的对象，1代表检查一，二代的对象，
# 2代表检查一，二，三代的对象，如果不传参数，执行一个full collection，也就是等于传2。
# 返回不可达（unreachable objects）对象的数目
# 3. gc.get_threshold() 获取的 gc 模块中自动执行垃圾回收的频率
# 4. gc.set_threshold(threshold0[, threshold1[, threshold2]) 设置自动执行垃圾回收的频率
# 5. gc.get_count() 获取当前自动执行垃圾回收的计数器，返回一个长度为3的列表

# gc 模块的自动垃圾回收机制
# 必须要 import gc 模块，并且 is_enable()=True 才会启动自动垃圾回收
# 这个机制的主要作用就是发现并处理不可达的垃圾对象
# 垃圾回收 = 垃圾检查 + 垃圾回收
# 在Python中，采用分代收集的方法。
# 把对象分为三代，一开始，对象在创建的时候，放在一代中，
# 如果在一次一代的垃圾检查中，改对象存活下来，就会被放到二代中，
# 同理在一次二代的垃圾检查中，该对象存活下来，就会被放到三代中
# gc 模块里面会有一个长度为 3 的列表的计数器，可以通过 gc.get_count() 获取
# gc 模快有一个自动垃圾回收的阀值，即通过 gc.get_threshold 函数获取到的长度为3的元组
# 每一次计数器的增加，gc模块就会检查增加后的计数是否达到阀值的数目，
# 如果是，就会执行对应的代数的垃圾检查，然后重置计数器

# 注意: gc 模块唯一处理不了的是循环引用的类都有 __del__ 方法，
# 所以项目中要避免定义 __del__ 方法

import gc


class ClassA():
    pass
    # def __del__(self):
    #     print('object born,id:%s'%str(hex(id(self))))


gc.set_debug(gc.DEBUG_LEAK)
a = ClassA()
b = ClassA()

a.next = b
b.prev = a

print('---1---')
print(gc.collect())
print('---2---')
del a
print('---3---')
del b
print('---3-1---')
print(gc.collect())
print('---4---')
