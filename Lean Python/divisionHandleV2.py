print('Input two numbers. the first will be divided by the second')

afirst = input('first number:')

try:
    first=float(afirst)
    asecond = input('2nd number:')
    try:
        second = float(asecond)
        try:
            quotient = first / second
            print('Quotient 1st/2nd = ', quotient)
        except ZeroDivisionError as diag:
            print(diag, ': 2nd number must be non-zero')
    except ValueError as diag:
        print(diag, '2nd number')
except ValueError as diag:
    print(diag, '1st number')