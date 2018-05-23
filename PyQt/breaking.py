s = 'education '
k = s.partition('cat')
print('The word', s, 'is partitioned into three parts')
print('The first part is', k[0], 'separator is', k[1], 'and the third part is',k[2])
t = input('Enter a sentence: ')
print('The original sentence is', t)
print('The sentence after replacing all the characters "a" by "#" is:',\
      t.replace('a', '#'))
print('The sentence after replacing first three "a" characters by "#" is:',\
      t.replace('a', '#', 3))
u = t.split(' ')
print('The words in the entered sentence are', u)
print('The words in the entered sentence are')
for i in range(0, len(u)):
    print(u[i])
u = t.split(' ',1)
print('The sentence is split into two parts:', u[0], 'and', u[1])
