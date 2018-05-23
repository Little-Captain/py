def f(x):
    return x * 2

print(f(3))

g = lambda x: x * 2
print(g(3))

print((lambda x: x * 2)(3))

def evenval(x):
    return x % 2 == 0

evens = filter(evenval, range(1, 11))
print(type(evens))
print(list(evens))

def square(x):
    return x * x
sqr = map(square, range(1, 11))
print(type(sqr))
print(list(sqr))

k = map(int, [5, 10.15, 20, 25.628, 7])
print(list(k))

import functools
def add(x, y):
    return x + y
r = functools.reduce(add, range(1, 101))
print(r)

print(add.__module__)
