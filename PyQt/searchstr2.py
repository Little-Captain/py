p = input("Enter a string: ")
print("Entered String is", p)
q = input("Enter the substring to search: ")
r = p.count(q)
if r == 0:
    print(q, "not found in", p)
else:
    print(q, "occurs in", p, r, "times")
