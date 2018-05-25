#!/usr/bin/env python

# 元类
# 类也是对象


class ObjectCreator(object):
    pass

my_object = ObjectCreator()
print(my_object)

# Python 的类也是一种对象.
# 只要你使用关键字 class，Python 解释器在执行的时候就会创建一个对象

# 分析
# 在内存中创建一个对象，名字就是 ObjectCreator。
# 类对象 ObjectCreator 拥有创建对象（实例对象）的能力
# 但它的本质仍然是一个对象. 所有可以做如下操作
# 1. 你可以将它赋值给一个变量
# 2. 你可以拷贝它
# 3. 你可以为它增加属性
# 4. 你可以将它作为函数参数进行传递

print(ObjectCreator)

def echo(o):
    print(o)

echo(ObjectCreator)

ObjectCreator.new_attribute = 'foo'
print(ObjectCreator.new_attribute)
print(hasattr(ObjectCreator, 'new_attribute'))

ObjectCreatorMirror = ObjectCreator
print(ObjectCreatorMirror())

# 动态地创建类
# 类也是对象，你可以在运行时动态的创建它们，就像其他任何对象一样

# 函数中创建类
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar

MyClass = choose_class('foo')
print(MyClass)
print(MyClass())

# 当你使用 class 关键字时，Python 解释器自动创建这个对象。
# 但就和 Python 中的大多数事情一样，Python 仍然提供给你手动处理的方法

print(type(1))
print(type('1'))
print(type(ObjectCreator()))
print(type(ObjectCreator))

# 使用 type 创建类
# type有一种完全不同的功能，动态的创建类
# type可以接受一个类的描述作为参数，然后返回一个类
# type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
class Test(object):
    pass
print(Test())

Test2 = type('Test2', (), {})
print(Test2())
print(help(Test2))
print(help(Test))

# 元组中是类名字, 不是字符串
# 添加的属性是类属性
Foo = type('Foo', (object,), {'bar': True})
print(help(Foo))
print(Foo)
print(Foo())
print(Foo.bar)
f = Foo()
print(f)
print(f.bar)
FooChild = type('FooChild', (Foo,), {})
print(FooChild)
print(help(FooChild))
print(FooChild.bar)
print(FooChild().bar)

# 使用 type 创建带有方法的类
# 为类添加方法, 定义一个有着恰当签名的函数, 将其作为属性赋值
def echo_bar(self):
    print(self.bar)

# 添加实例方法
FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
print(hasattr(Foo, 'echo_bar'))
print(hasattr(FooChild, 'echo_bar'))

my_foo = FooChild()
my_foo.echo_bar()

# 添加静态方法
@staticmethod
def testStatic():
    print('static method')

FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar, 'testStatic': testStatic})
fooChild = FooChild()
print(fooChild.testStatic)
fooChild.testStatic()
fooChild.echo_bar()

# 添加类方法
@classmethod
def testClass(cls):
    print(cls.bar)

FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar, 'testStatic': testStatic, 'testClass': testClass})
fooChild = FooChild()
fooChild.testClass()
FooChild.testClass()

# 元类的实质
# 元类就是用来创建类的类
# MyClass = MetaClass()
# MyObject = MyClass()
MyClass = type('MyClass', (), {})
# 函数 type 实际上是一个元类
# type 是 Python 在背后用来创建所有类的元类
# 为什么 type 会采用小写形式而不是 Type
# str 是用来创建字符串对象的类，int是用来创建整数对象的类
# type 就是用来创建类对象的类
# 可以通过 __class__ 属性来看对象所属的类
# Python 中所有的东西都是对象, 且都是从一个类中创建出来的, 这个类就是 type

age = 35
print(age.__class__)
print(age.__class__.__class__)
name = 'bob'
print(name.__class__)
print(name.__class__.__class__)
def foo():
    pass
print(foo.__class__)
print(foo.__class__.__class__)
class Bar(object):
    pass
print(Bar.__class__)
print(Bar.__class__.__class__)
print(Bar().__class__)
print(Bar().__class__.__class__.__class__.__class__)
# 元类是创建类的类. type 是 Python 的内建元类.

# __metaclass__ 属性
# 可以在定义一个类的时候为其添加__metaclass__属性
# class Foo(object):
#     __metaclass__ = xxx
#     ...
# 首先写下 class Foo(object) ，但是类 Foo 还没有在内存中创建。
# Python 会在类的定义中寻找 __metaclass__ 属性，如果找到了，
# Python 就会用它来创建类 Foo，如果没有找到，就会用内建的type来创建这个类
class Foo(Bar):
    pass
# 上述代码, Python 做的操作:
# 1. Foo中有__metaclass__这个属性吗？如果是，
# Python会通过__metaclass__创建一个名字为Foo的类(对象)
# 2. 如果Python没有找到__metaclass__，它会继续在Bar（父类）
# 中寻找__metaclass__属性，并尝试做和前面同样的操作
# 3. 如果Python在任何父类中都找不到__metaclass__，它就会在模块层次
# 中去寻找__metaclass__，并尝试做同样的操作
# 4. 如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象

# 该为 __metaclass__ 赋值什么? 可以创建一个类的东西
# type. 使用到type, 子类化 type

# 自定义元类
# 元类的主要目的就是为了当创建类时能够自动地改变类


def upper_attr(future_class_name, future_class_parents, future_class_attr):

    newAttr = {}
    for name, value in future_class_attr.items():
        if not name.startswith('__'):
            newAttr[name.upper()] = value

    return type(future_class_name, future_class_parents, newAttr)


class Foo(object, metaclass=upper_attr):
    bar = 'bip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)


# 使用 class 做元类
class UpperAttrMetaClass(type):
    # __new__ 是在 __init__ 之前被调用的特殊方法
    # __new__ 是用来创建对象并返回之的方法
    # 而 __init__ 只是用来将传入的参数初始化给对象
    # 你很少用到 __new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写 __new__
    # 如果你希望的话，你也可以在 __init__ 中做些事情
    # 还有一些高级的用法会涉及到改写 __call__ 特殊方法，但是我们这里不用
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        newAttr = {}
        for name, value in future_class_attr.items():
            if not name.startswith('__'):
                newAttr[name.upper()] = value

        # 方法1：通过'type'来做类对象的创建
        # return type(future_class_name, future_class_parents, newAttr)

        # 方法2：复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        # return type.__new__(cls, future_class_name, future_class_parents, newAttr)

        # 方法3: 使用 super 方法
        return super(UpperAttrMetaClass, cls).__new__(cls, future_class_name, future_class_parents, newAttr)

class Foo(object, metaclass=UpperAttrMetaClass):
    bar = 'bip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f= Foo()
print(f.BAR)

# 元类
# 1. 拦截类的创建
# 2. 修改类
# 3. 返回修改之后的类
