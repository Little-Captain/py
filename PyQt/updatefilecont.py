import sys
f = open('aboutbook.txt', 'r')
lines = f.readlines()
print('Original content of the file:')
for line in lines:
    sys.stdout.write(line)
f.close()
n = int(input("\n\nEnter the line number to change: "))
if n <=len(lines):
    r = input("Enter the new content: ")
    lines[n-1] = r + "\n"
    f = open('aboutbook.txt', 'w' )
    f.writelines(lines)
    f.close()
    print('The content of the file after updating line' , n)
    f = open('aboutbook.txt', 'r' )
    lines = f.read()
    print (lines)
    f.close()
else:
    print ("The line number", n, "is not found in the file" )
