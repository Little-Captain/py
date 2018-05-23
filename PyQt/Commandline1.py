import sys
print('There are %d arguments' % len(sys.argv))
print('The command line arguments are:' )
print(sys.argv)
for i in sys.argv:
    print(i)
    print('Path of the Python is' , sys.path)
