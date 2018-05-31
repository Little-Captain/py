#!/usr/bin/env python

# pep8

# 代码更多是用来读而不是写
# 风格指南强调一致性。项目、模块或函数保持一致都很重要。


# 每级缩进用4个空格
# 括号中使用垂直隐式缩进或使用悬挂缩进。
# 后者应该注意第一行要没有参数，后续行要有缩进

# 垂直隐式缩进: 对准左括号
def long_function_name(var_one, var_two,
                       var_three, var_four):
    pass

# 悬挂缩进: 不对准左括号，但加多一层缩进，以和后面内容区别


def long_function_name1(
        var_one, var_two, var_three,
        var_four):
    pass

long_function_name(1, 2, 3, 4)

# 不使用垂直对齐时，第一行不能有参数。
# 参数的缩进和后续内容缩进要能区别。

# 4个空格的规则是对续行可选的
# 悬挂缩进不一定是4个空格
# if语句跨行时，两个字符关键字(比如if)加上一个空格，
# 再加上左括号构成了很好的缩进。后续行暂时没有规定，
# 至少有如下三种格式，建议使用第3种。
a = 1
b = 2
# 没有额外缩进，不是很好看，不推荐.
if (a and
    b):
    print(a, b)

# 额外添加缩进,推荐。 当然这个例子可以不夸多行
if (a
        and b):
    print(a, b)

# 右边括号也可以另起一行
# 右括号回退


def some_function_that_takes_arguments(*args):
    return 1

my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

# 限制所有行的最大行宽为79字符
# 文本长块，比如文档字符串或注释，行长度应限制为72个字符

# 空行
# 两行空行分割顶层函数和类的定义
# 类的方法定义用单个空行分割
# 额外的空行可以必要的时候用于分割不同的函数组，但是要尽量节约使用
# 额外的空行可以必要的时候在函数中用于分割不同的逻辑块，但是要尽量节约使用

# 导入在单独行
import os
import sys
# import os, sys
# 导入始终在文件的顶部，在模块注释和文档字符串之后，在模块全局变量和常量之前
# 导入顺序如下：标准库进口, 相关的第三方库，本地库。
# 各组的导入之间要有空行
# 禁止使用通配符导入

# 字符串引用
# Python中单引号字符串和双引号字符串都是相同的。
# 注意尽量避免在字符串中的反斜杠以提高可读性

# 括号里边避免空格
# 括号里边避免空格
# Yes
# spam(ham[1], {eggs: 2})
# No
# spam( ham[ 1 ], { eggs: 2 } )

# 逗号，冒号，分号之前避免空格
# Yes
# if x == 4: print x, y; x, y = y, x
# No
# if x == 4 : print x , y ; x , y = y , x

# 索引操作中的冒号当作操作符处理前后要有同样的空格
# 一个空格或者没有空格，建议没有。
# Yes
# ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
# ham[lower:upper], ham[lower:upper:], ham[lower::step]
# ham[lower+offset : upper+offset]
# ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
# ham[lower + offset : upper + offset]

# 函数调用的左括号之前不能有空格
# Yes
# spam(1)
# dct['key'] = lst[index]

# 赋值等操作符前后不能因为对齐而添加多个空格
# Yes
x = 1
y = 2
long_variable = 3

# 二元运算符两边放置一个空格
# 涉及 =、符合操作符 ( += , -=等)、
# 比较( == , < , > , != , <> , <= , >= , in , not in , is , is not )、
# 布尔( and , or , not )。
# 优先级高的运算符或操作符的前后不建议有空格。
# Yes
# i = i + 1
# submitted += 1
# x = x*2 - 1
# hypot2 = x*x + y*y
# c = (a+b) * (a-b)

# 关键字参数和默认值参数的前后不要加空格
# Yes
# def complex(real, imag=0.0):
#     return magic(r=real, i=imag)

# 通常不推荐复合语句(Compound statements: 多条语句写在同一行)。
# Yes
# if foo == 'blah':
#     do_blah_thing()
# do_one()
# do_two()
# do_three()

# 避免使用: l O I 等单个字符变量名. 在一些字体中不容易区分

# 包和模块名
# 模块名要简短，全部用小写字母，可使用下划线以提高可读性。
# 包名和模块名类似，但不推荐使用下划线。