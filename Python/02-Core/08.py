#!/usr/bin/env python

# 再议装饰器


def makeBold(fn):

    def wrapped():
        return '<b>' + fn() + '</b>'

    return wrapped


def makeItalic(fn):

    def wrapped():
        return '<i>' + fn() + '</i>'

    return wrapped

@makeBold
def xtest1():
    return 'hello world-1'


@makeItalic
def xtest2():
    return 'hello world-2'


@makeBold
@makeItalic
def xtest3():
    return 'hello world-3'

print(xtest1())
print(xtest2())
print(xtest3())