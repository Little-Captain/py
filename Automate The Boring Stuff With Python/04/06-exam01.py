#!/usr/bin/env python

def dealList(list):
    s = ''
    if len(list) == 0:
        return s
    if len(list) == 1:
        return str(list[0])
    for i in range(len(list) - 1):
        s += str(list[i]) + ', '
    s += 'and ' + str(list[-1])
    return s

spam = [12, 'apples', 'bananas', 'tofu', 'cats', 12]
s = dealList(spam)
print(s)
print(dealList([1, 2, 3]))
