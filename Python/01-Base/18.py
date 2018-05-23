#!/usr/bin/env python

# 类对象所拥有的方法，需要用修饰器 @classmethod 来标识其为类方法，
# 对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数
# 能够通过实例对象和类对象去访问

class People(object):
    country = 'china'

    @classmethod
    def getCountry(cls):
        print('cls')
        return cls.country

    @classmethod
    def setCountry(cls, country):
        cls.country = country

    # 不会传入 cls 类对象
    @staticmethod
    def getcountrystatic():
        return People.country

    # 这样覆盖, 类方法就没了
    # def getCountry(self):
    #     print('obj')
    #     return People.country


p = People()
print(p.getCountry())
People.country = 'japan'
print(People.getCountry())
p.setCountry('jp')
print(p.getCountry())
print(People.getCountry())
print(People.getcountrystatic())