#/usr/bin/env python

# 所谓重写, 就是子类中, 有一个和父类相同名字的方法, 在子类中的方法会覆盖掉父类中同名的方法

class Cat(object):

    def __init__(self, name):
        self.name = name
        self.color = 'yellow'

    def sayHello(self):
        print('halou-----1')


class Bosi(Cat):

    def __init__(self, name):
        # 调用父类 __init__ 方法1
        # Cat.__init__(self, name)
        # 调用父类 __init__ 方法2
        # super(Bosi, self).__init__(name)
        # 调用父类 __init__ 方法3
        super().__init__(name)

    def sayHello(self):
        print('halou------2')


bosi = Bosi('xiaohua')
bosi.sayHello()