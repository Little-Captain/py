#/usr/bin/env python

# 经典类
# class 类名:
# 新式类
# class 类名(object):
#     方法列表

class Car:

    # 初始化方法
    def __init__(self, wheelNum, color):
        self.wheelNum = wheelNum
        self.color = color

    # 自描述字符串
    def __str__(self):
        return '颜色' + self.color + '\n' + '我有' + str(self.wheelNum) + '个轮胎'

    def move(self):
        print('车泵跑')

    def toot(self):
        print('车鸣笛')


BMW = Car(4, 'green')
BMW.move()
BMW.toot()
print(BMW.color)
print(BMW.wheelNum)
print(BMW)
