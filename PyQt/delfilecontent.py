import sys
f = open('aboutbook.txt', 'r' )
lines = f.readlines()
print('Original content of the file:')
for line in lines:
    sys.stdout.write(line)
f.close()
del lines[1:3]
f = open('aboutbook.txt', 'w' )
f.writelines(lines)
f.close()
print('\nThe content of the file after deleting second and third line:')
f = open('aboutbook.txt', 'r' )
lines = f.read()
print (lines)
f.close()
