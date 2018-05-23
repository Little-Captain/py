#!/usr/bin/env python

# Python中没有像C++中public和private这些关键字来区别公有属性和私有属性
# 在属性名前面加了2个下划线'__'，则表明该属性是私有属性, 否则为公有属性
# 方法也是一样，方法名前面加了2个下划线的话表示该方法是私有的，否则为公有的

class Peopel(object):

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        if len(name) >=5:
            self.__name = name
        else:
            print('error: 名字长度需求大于或者等于5')

xiaoming = Peopel('dong dong')
print(xiaoming.getName())

xiaoming.setName('wang wang')
print(xiaoming.getName())

xiaoming.setName('li')
print(xiaoming.getName())
