#!/usr/bin/env python
import os
# 打开一个已经存在的文件
f = open('test.txt', 'r')
str = f.read(3)
print('读取的数据是: ', str)

# 查找当前位置
position = f.tell()
print('当前文件位置: ', position)

str = f.read(3)
print('读取的数据: ', str)

position = f.tell()
print('当前文件位置: ', position)

f.close()

# 打开一个已经存在的文件
f = open('test.txt', 'r')
str = f.read(30)
print('读取的数据是: ', str)

position = f.tell()
print('当前文件位置: ', position)

f.seek(5, 0)

position = f.tell()
print('当前文件位置: ', position)

f.close()

f = open('test.txt', 'r')

position = f.tell()
print('当前文件位置: ', position)

# f.seek(-3, 2)

str = f.read()
print('数据是: ', str)

f.close()

os.rename('test.txt', 'test1.txt')
os.remove('test1.txt')
