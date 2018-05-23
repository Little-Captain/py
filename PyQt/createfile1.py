matter = '''Python is a great language
Easy to understand and learn
Supports Object Oriented Programming
Also used in web development '''
f = open('aboutbook.txt', 'w')
print(type(f))
f.write(matter)
f.close()
f = open('aboutbook.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print (line)
f.close()
