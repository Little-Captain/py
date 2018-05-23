m = input("Enter a string: ")
n = input("Enter a substring: ")
if n in m:
    print(n, "is found in the string", m)
else:
    print(n, "does not exist in the string", m)
