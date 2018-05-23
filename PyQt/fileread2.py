import sys
f = open('aboutbook.txt', 'r')
lines = f.readlines()
f.close()
print('The contents in the file are:', lines)
print('\nThe contents in the file are:')
for line in lines:
    sys.stdout.write(line)
print('\n\nThe contents in the file are:')
for i in range(0, len(lines)):
    sys.stdout.write(lines[i])
