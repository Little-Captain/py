s = input('Enter a sentence: ')
n = len(s)
c = 0
for i in range(0,n):
    if (s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or\
        s[i]=='I' or s[i] =='o' or s[i]=='O' or s[i]=='u' or s[i]=='U'):
        c+=1
print ('The number of vowels in the sentence is' , c)
t = s.count('a', 0, n) + s.count('A', 0, n) + s.count('e', 0, n) \
    + s.count('E', 0, n) + s.count('i', 0, n) + s.count('I', 0, n) \
    + s.count('o', 0, n) + s.count('O', 0, n) + s.count('u', 0, n) \
    + s.count('U', 0, n)
print ('The number of vowels in the sentence is' , t)
v = s.count('a') + s.count('A') + s.count('e') + s.count('E') + s.count('i' )\
    + s.count('I')+ s.count('o')+ s.count('O')+ s.count('u')+s.count('U')
print ('The number of vowels in the sentence is' , v)
