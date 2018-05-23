student1 = {'John' : 60, 'Kelly' : 70, 'Caroline' : 80}
student2 = dict([('David', 90), ('John',55)])
print('The items in dictionary student1 are:', student1.items())
print('The keys in student1 dictionary are:', student1.keys())
print('The values in student1 dictionary are:', student1.values())
student1.update(student2)
print('The items in dictionary student1 after merging with student2 dictionary are:', student1.items())
n = input('Enter name whose marks you want to see: ')
if n in student1: # key
    print('The marks of', n , 'are' , student1.get(n))
else:
    print('Sorry the name', n, 'does not exist in student1 dictionary')
