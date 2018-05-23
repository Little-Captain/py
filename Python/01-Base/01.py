# -*- coding:utf-8 -*-
print('你好')
print('hello world')
# 测试
'''
多行注释
多行注释
多行注释
'''

num1 = 100
num2 = 89
result = num1+num2
print(result)

print(type(result))

age = 10
print("我的年龄%d岁"%age)
name = 'hehe'
print('我的姓名%s,年龄是%d'%(name,age))

# python2 中的输入
# 1. raw_input() 和 python3 中的 input 类似
# 2. input() 对输入的文字进行表达式求值. 所以输入的必须是表达式
# 3. python3 中的 input 对获取的数据都是以字符串的形式保存的

# // 取整除法, 返回商的整数部分
print(7//2)
print(7.4//2)
