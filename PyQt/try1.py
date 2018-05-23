import sys
try:
    n = input('Enter your name ')
except EOFError:
    print('EOF error has occurred')
    sys.exit(1)
except:
    print('Some error has occurred' )
else:
    print('The name entered is', n)
