import sys
try:
    f = open('aboutbook.txt', 'r')
    lines = f.read()
except IOError:
    print('File aboutbook.txt does not exist')
    sys.exit(1)
f.close()
print (lines)
