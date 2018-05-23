print('Input two numbers. the first will be divided by the second')

afirst = input('first number:')
asecond = input('second number:')

try:
    first=float(afirst)
    second = float(asecond)
    quotient = first / second
    print('Quotient 1st/2nd = ', quotient)
except Exception as diag:
    print(diag.__class__.__name__, ':', diag)