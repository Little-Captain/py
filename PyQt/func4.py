def conv(x):
    if x==1:
        return "one"
    if x==2:
        return "two"
    if x==3:
        return "three"
    if x==4:
        return "four"
n = int(input("Enter a number between 1 and 4: "))
print(n, "in words is", conv(n))
