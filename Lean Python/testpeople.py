from people import person

joe = person('Joe Bloggs', 47)

print("Joe's age is ", joe.age)

print("Joe's full name is ", joe.name)

joe.addChild('Dick',7)
joe.addChild('Dora',9)

joe.listChildren()

joekids=joe.getChildren()

print("** Joe's attributes **")
print(vars(joe))

print("** Joe's Children **")
for j in joekids:
    print(j.name,'attributes')
    print(vars(j))