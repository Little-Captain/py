s = input("Enter a string: ")
n = len(s)
print("The first character of", s, "is", s[0])
print("The entered string will appear character wise as:")
for i in range(0,n):
    print(s[i])
print("The entered string will appear character wise as:")
for i in s:
    print (i)
print("String with its characters sorted is", "".join(sorted(s)))
print("String in reverse form is", "".join(reversed(s)))
