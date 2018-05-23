def sum(a, b = 5):
    "Adds the two numbers"
    return a + b
sum.version = "1.0"
sum.author = "bintu"
k = sum(10, 20)
print('Sum is', k)
print('The documentation string is', sum.__doc__)
print('The function name is', sum.__name__)
print('The default values of the function are', sum.__defaults__)
print('The code object of the function is', sum.__code__)
print('The dictionary of the function is', sum.__dict__)
