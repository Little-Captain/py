names = []
n = int(input("How many names? "))
print("Enter", n, "names")
for i in range (0,n):
    m = input()
    names.append(m)
print("The original list of names is", names)
p = input("Enter the name to search: ")
if p in names:
    print("The name", p, "is found in the list at location ", names.index(p) + 1)
else:
    print("The name", p, "is not found in the list ")
q = input("Enter the name to update/change: ")
if q in names:
    loc = names.index(q)
    r = input("Enter the new name: ")
    names[loc] = r
    print("The name", q, "in the list is changed to", r)
else:
    print ("The name", q, "is not found in the list")
names.sort()
print ("Sorted names are", names)
