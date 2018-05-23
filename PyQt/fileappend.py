import sys
matter2 = ''' Its very hot today
Lets have a Cold drink '''
f = open('aboutbook.txt', 'a' )
f.write("\n%s" % matter2)
f.close()
f = open('aboutbook.txt', 'r')
lines = f.readlines()
f.close()
print('The contents in the file are:')
for line in lines:
    sys.stdout.write(line)
