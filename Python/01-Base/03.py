# 切片语法: [起始:结束:步长]
# 不包括 结束位
name = 'abcdef'
print(name[0:3])
print(name[:3])
print(name[::2])
print(name[5:1:2])
print(name[1:5:2])
print(name[::-2])
print(name[5:1:-2])

str = 'hello world'
print(str.find('hello1'))
# print(str.index('hello1'))
print(str.count('hello'))
print(str.replace('he', 'ha'))
print(str.split(' '))
str = 'hello'
print(str.ljust(10))
print(str.center(15))
print(str.ljust(10).rstrip())
str = '  hello '
print(str.strip())
print(str.rfind('l'))
print(str.find('l'))

nameList = ['xiaoWang','xiaoZhang','xiaoHua']
findName = 'xiaoWang'
if findName in nameList:
    print('有')
else:
    print('无')

# del: 下标
# pop: 删最后
# remove: 根据元素值删除, 如果有相同的值, 删除开始的
del nameList[2]
print(nameList)
nameList.append('hhh')
print(nameList)
print(nameList.pop())
print(nameList)
print(nameList.remove('xiaoWang'))
print(nameList)
# python 中的区间一般都是 左闭右开
