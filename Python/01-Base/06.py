# def 函数名():
    # 代码

def test(a, b):
    "用来完成对2个数求和"
    print('a=%d'%a)
    print('b=%d'%b)
    print('%d'%(a+b))

test(1, 2)

help(test)

test(b=1, a=2)

def printOneLine():
    print('-'*30)

def printNumLine(num):
    i = 0

    while i < num:
        printOneLine()
        i += 1

printNumLine(3)

a = 100

def test1():
    print(a)

def test2():
    print(a)

test1()
test2()

a = 100

def test1():
    global a

    print(a)
    a = 200
    print(a)

def test2():
    print(a)

test1()
test2()

a = 1

def f():
    global a
    a += 1
    print(a)

f()

def divid(a, b):
    shang = a//b
    yushu = a%b
    # 这个返回值类型是元组
    return shang, yushu

print(divid(1, 2))

# 注意: 带默认值的参数一定要位于参数列表最后
def printInfo(name, age=35):
    print('name: %s'%name)
    print('age: %d'%age)

printInfo('miki')
printInfo(age=9, name='miki')

# def functionName([formal_args,], *args, **kwargs):
#     "函数文档字符串"
#     function_suite
#     return [expression]

# 加了星号（*）的变量args会存放所有未命名的变量参数，args为元组；
# 而加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典。

def fun(a, b, *args, **kwargs):
    """可变参数"""
    print('a=', a)
    print('b=', b)
    print('args=', args)
    print('kwargs: ')
    for k, v in kwargs.items():
        print(k, '=', v)

fun(1, 2, 3, 4, 5, m=7, n=8, p=9)
c =  (3, 4, 5)
d = {'m':6, 'n':7}
# 使用星号解构
fun(1, 2, *c, **d)
fun(1, 2, c, d)

def selfAdd(a):
    # a += a
    a = a + a
a_int = 1
selfAdd(a_int)
print(a_int)

a_list = [1, 23]
selfAdd(a_list)
print(a_list)
# Python中的函数是引用传递
# 对于不可变类型，因变量不能修改，所以运算不会影响到变量自身
# 对于可变类型来说，函数体中的运算有可能会更改传入的参数变量

# lambda [arg1 [, arg2, ..., argn]]:expression
sum = lambda arg1,arg2:arg1+arg2
print('Value of total: ', sum(10, 20))

# Lambda函数能接收任何数量的参数但只能返回一个表达式的值
# 匿名函数不能直接调用print，因为lambda需要一个表达式

def fun(a, b, opt):
    print('a=', a)
    print('b=', b)
    print('result=', opt(a, b))

fun(1, 2, lambda x,y:x+y)

stus = [
    {"name":"zhangsan", "age":18},
    {"name":"lisi", "age":19},
    {"name":"wangwu", "age":17}
]
stus.sort(key=lambda x:x['name'])
print(stus)

stus.sort(key=lambda x:x['age'])
print(stus)

def test(a):
    if a:
        return 1
    else:
        return 'False'

print(test(True))
