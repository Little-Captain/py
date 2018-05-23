tmplist = ['John', 'Kelly', 10, 'Caroline', 15, 'Steve', 'Katheline']
print("The original list is", tmplist)
print("The first four elements in the list are:", tmplist[0:4])
print("The number of elements in the list are", len(tmplist))
m = input("Enter a name to add to the list ")
tmplist.append(m)
print("The elements in the list now are", tmplist)
n = int(input("Enter the element number to delete "))
del tmplist[n-1]
print("The elements in the list now are", tmplist)
print("The elements in the list can also be displayed as shown:")
for i in range(0, len(tmplist)):
    print (tmplist[i])
