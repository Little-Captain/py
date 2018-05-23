#!/usr/bin/env python

class Cat(object):

    def __init__(self, name, color='白色'):
        self.name = name
        self.color = color

    def run(self):
        print('%s--run'%self.name)

# 父类的属性、方法, 会被子类继承
class Bosi(Cat):

    # __init__ 方法是继承父类的哦

    def setNewName(self, newName):
        self.name = newName

    def eat(self):
        print('%s--eat'%self.name)

bs = Bosi('印度猫')
print('bs的名字为:%s'%bs.name)
print('bs的颜色:%s'%bs.color)
bs.eat()
bs.setNewName('博士')
bs.run()