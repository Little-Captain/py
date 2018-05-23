#!/usr/bin/env python

# 异常的传递

# 如果try嵌套，那么如果里面的try没有捕获到这个异常，那么外面的try会接收到这个异常，
# 然后进行处理，如果外边的try依然没有捕获到，那么再进行传递。。。

# 如果一个异常是在一个函数中产生的，例如函数A---->函数B---->函数C,而异常是在函数C中产生的，
# 那么如果函数C中没有对这个异常进行处理，那么这个异常会传递到函数B中，如果函数B有异常处理那么
# 就会按照函数B的处理方式进行执行；如果函数B也没有异常处理，那么这个异常会继续传递，以此类推。。。

# __all__ 变量决定了在外界使用 from xxx import * 时, 导入的内容
# 只有这个变量包含的内容, 才会被导入
__all__ = ['test1', 'test3']

def test1():
    print('-----test1-1-----')
    print(num)
    print('-----test1-2-----')

def test2():
    print('-----test2-1-----')
    test1()
    print('-----test2-2-----')

def test3():
    try:
        print('-----test3-1-----')
        test1()
        print('-----test3-2-----')
    except Exception as result:
        print('捕获到了异常, 信息是: %s'%result)

    print('-----test3-3-----')

# 根据__name__变量的结果能够判断出，是直接执行的python脚本还是被引入执行的，
# 从而能够有选择性的执行测试代码
if __name__ == '__main__':

    test3()
    print('------------------------')
    test2()