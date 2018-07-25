#!/usr/bin/env python

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)