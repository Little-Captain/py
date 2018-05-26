#!/usr/bin/env python

# python 中的垃圾回收机制
# 引用计数为主, 标记清除和分代收集为辅

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
