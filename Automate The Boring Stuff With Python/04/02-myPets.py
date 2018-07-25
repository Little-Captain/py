#!/usr/bin/env python

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name: ')
name = input()
if name not in myPets:
    print('I do not hava a pet named ' + name)
else:
    print(name + ' is my pet.')


# 多重赋值技巧
cat = ['fat', 'black', 'loud']
# 变量的数目和列表的长度必须严格相等
size, color, disposition = cat
print(size, color, disposition)