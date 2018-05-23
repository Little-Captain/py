import sys
try:
    f = open('aboutbook.txt', 'r')
    try:
        lines = f.read()
    finally:
        f.close()
except IOError:
    print('File aboutbook.txt does not exist')
    sys.exit(1)
print(lines)
