p = input("Enter a string: ")
print("Entered String is ", p)
q = input("Enter the substring to search: ")
r = p.find(q)
if r == -1:
    print(q, "not found in", p)
else:
    print(q, "found in", p, "at location", r+1)
