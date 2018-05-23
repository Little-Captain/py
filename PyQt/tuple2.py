names = ('John', 'Kelly', 'Caroline', 'Steve', 'Katheline')
n = input("Enter the name to search: ")
if n in names:
    print("The name", n, "is present in the tuple")
else:
    print("The name", n, "does not exist in the tuple")
countries = ('U.S.', 'U.K', 'India')
names += countries
print("The tuples are concatenated. The concatenated tuple is", names)
