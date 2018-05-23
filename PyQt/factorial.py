def fact(x):
    if x == 1: return 1
    else: return x * fact(x-1)
print('The factorial of 5 is', fact(5))
