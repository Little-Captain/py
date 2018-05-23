def fruits(seq):
    for fruit in seq:
        yield '%s' % fruit

f = fruits(['Apple', 'Orange', 'Mango', 'Banana' ])
print('The list of fruits is:' )
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
f = fruits(['Apple', 'Orange', 'Mango', 'Banana' ])
print('The list of fruits is:' )
for x in f:
    print (x)
