#!/usr/bin/env python

# 可以用raise语句来引发一个异常。异常/错误对象必须有一个名字，且它们应是Error或Exception类的子类

class ShortInputException(Exception):
    '''自定义的异常类'''
    def __init__(self, length, atleast):
        # 父类的初始化方法, 一般是要调用的
        super().__init__()
        self.length = length
        self.atleast = atleast

def main():
    try:
        s = input('请输入 --> ')
        if len(s) < 3:
            raise ShortInputException(len(s), 3)
    except ShortInputException as result:
        print('ShortInputException %d %d'%(result.length, result.atleast))
    else:
        print('没有异常发生.')


main()