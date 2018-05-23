import sys
n = input('Enter a number ')
if n.isdigit():
    n = int(n)
try:
    m = 15 / n
except TypeError as ex:
    print('You have not entered a numeric value:', ex)
    sys.exit(1)
except ZeroDivisionError as ex:
    print('You have entered zero value:', ex)
    sys.exit(1)
print('The result is', m)
