# 公共方法
# +: 合并
# *: 复制
# in: 元素是否存在
# not in: 元素是否不存在
print("hello " + "itcast")
print([1, 2] + [3, 4])
print(('a', 'b') + ('c', 'd'))

print('ab'*4)
print([1, 2]*4)
print(('a', 'b')*4)

print(3 in [1, 2])

# id: 获取对象的引用
a = 1
b = a
print(id(a))
print(id(b))
a = 2
print(id(a))
print(b)

a = [1, 2]
b = a
print(id(a))
print(id(b))
a.append(3)
print(a)
print(b)
print(id(a))
print(id(b))

# 可变类型与不可变类型
# 可变: list、dict
# 不可变: int、long、bool、float、str、tuple