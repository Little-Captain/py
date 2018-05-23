import os
import sys

f = open('name.txt', encoding='utf8')
names = f.readlines()
f.close()
tmp = []
for name in names:
    tmp.append(name.strip('\n'))
names = tmp
    
allmp4 = []
for filename in os.listdir('./'):
    tmp = filename.split('.')
    if filename.split('.')[-1] == 'mp4':
        allmp4.append(filename)

if len(names) == len(allmp4):
    for i in range(0, len(names)):
        print('old:', allmp4[i])
        print('new:', names[i]+'.mp4')
        os.rename(allmp4[i], names[i]+'.mp4')


