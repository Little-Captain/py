#!/usr/bin/env python

def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacon'
    print(eggs)

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)
bacon()
ham()