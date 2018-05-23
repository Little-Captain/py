# 1.和字符串相关的常用操作
stringInDoubleQuotes = "Hello Python!"
stringInSingleQuotes = 'Hello Python!'
stringInTripleQuotes = '''Hello Python!
This might be a long string
going through multiple lines.
'''
print(stringInDoubleQuotes)
print(stringInSingleQuotes)
print(stringInTripleQuotes)

stringInDoubleQuotes = "Hello 'Python'!"
stringInSingleQuotes = 'Hello "Python"!'
stringInTripleQuotes = '''Hello 'Python'!
This might be a "long string"
acrossing multiple lines.
'''
print(stringInDoubleQuotes)
print(stringInSingleQuotes)
print(stringInTripleQuotes)

aNumber = 123
aString = str(aNumber)

oneTwoThree = int("234")

action = "Hello "
name = "Mars!"
welcome = action + name
welcome.upper()
welcome.lower()

action.strip()

print(dir(action))
print(help(action.count))

aString[0]
print(action[0:5])

# 2.各种各样的String Template
# printf("Hello %s!", "Mars")
print("Hello %s!" % "Mars")
name = "Mars"
print("%s %s" % ("Hello", name))
print("PI: %.2f" % 3.14)

welcome = {"action": "Hello", "name": "Mars"}
print("%(action)s %(name)s" % welcome)
print("{0} {1}!".format("Hello", "Mars"))
print("{action} {name}!".format(**welcome))

# 3.理解Python中的数组类型 - list
list1 = []
list2 = list()
numList = [8, 6, 5, 7, 2]
mixList = [1, "one", 1.0]
nestedList = [numList, mixList]
print(mixList + numList)
print(mixList.extend(numList))
print(mixList)
numList.append(9)
print(numList)
numList.append([9, 10])
print(numList)
numList = [8, 6, 5, 7, 2]
print(numList)
numList1 = numList.copy()
numList.sort()
print(numList)
print(numList1)

print(numList[0])
print(numList[0:-1])

numList.insert(1, 9)
print(numList)

numList.insert(100, 9)
print(numList)

numList = [9, 8, 5, 2, 5, 4, 2]
print(numList.pop(0))
print(numList)
print(numList.remove(2))
print(numList)

numList = [8, 4, 4, 6, 2]
del(numList[0:5:2])
print(numList)
print(len(numList))
print(numList.index(4))

# 4.Python中的只读集合 - Tuple
empty = ()
numbers = (1, 2, 3)
mix = (1, 2, 'Three')
# list -> Tuple
numbers1 = ([1, 2, 3])
numbers2 = tuple([1, 2, 3])
print(numbers1)
print(numbers2)
numbers = (1, 2, 3)
sum = numbers + numbers
print(sum)
print((numbers) * 2)
print(numbers * 2)
print(numbers[0])
print(numbers[0:2])
print(numbers[0:3:2])

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(3 in numbers)

numbers = (1, 2, 3)
del numbers
# print(numbers)

# 5.在Python中使用dictionary

empty = {}
user = {"email": "11@boxue.io", "workId": 11}
print(user)
empty = dict()
user = dict(user)
print(user)
print(user["email"])
user['email'] = '10@boxue.io'
print(user['email'])
user['address'] = "Beijing xxxxx"
print(user['address'])
user.update({'address': 'Beijing', 'xxx': 'abc'})
print(user)
del(user['address'])
print(user)
del(user)
user = {'user': 'user'}
print(user)
user.clear()
print(user)
user = dict({"email": "11@boxue.io", "workId": 11, "workId": 10})
print(user)
user = dict({"email": "11@boxue.io", "workId": 11, (11, 1101): "Floor&Room"})
print(user.keys())
print(user.values())
print('email' in user)
print('email' in user.keys())

# 6.理解分支语句和boolean表达式
num = 2
if num < 10:
    conten = '{0} is less than 10'.format(num)
    print(conten)

if num < 10:
    conten = '{0} is less than 10'.format(num)
    print(conten)
# elif 10 < num < 20:
elif num > 10 and num < 20:
    print('between 10 and 20')
elif num == 10 or num == 20:
    print('equal to 10 or 20')
elif num != 10:
    print('not equal to 10')
elif num not in [10, 20]:
    print('not equal to 10 or 20')
else:
    print('greater than or equal to 20')

if not "":
    print('empty string')

if not ():
    print('empty string')

if not []:
    print('empty string')

if not None:
    print('empty string')

if __name__ == '__main__':
    print('execute as a single script')

# 7.在Python中使用循环
for num in range(1, 5):
    print(num)

for num in [1, 2, 4, 5, 6]:
    print(num)

user = {'email': '11@boxue.io', 'name': 'Mars'}
for info in user:
    print(info)
    print(user[info])

for num in range(1, 6):
    if num == 2:
        break
    print(num)
else:
    print('all numbers are iterated')

num = 1
while num < 10:
    if num % 2 == 0:
        num += 1
        continue

    print(num)
    num += 1

# 8.用数学思维理解Comprehension
numbers = [i for i in range(1, 6)]
print(numbers)
numbers = [i for i in range(1, 6) if i % 2 == 0]
print(numbers)
strings = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
flatten = [int(i) for items in strings for i in items]
print(flatten)
xSample = [2, 5, 8]
ySample = [2, 6, 8]
points = [(x, y) for x in xSample for y in ySample if x != y]
print(points)
numbersSet = {x for x in range(1, 6)}
print(numbersSet)
numbersDict = {i: str(i) for i in range(1, 6)}
print(numbersDict)
print(user)
switch = {value: key for key, value in user.items()}
print(switch)

# 9.认识Python中的异常处理
try:
    3/1
    # fn()
    # "Hello".index(1)
except ZeroDivisionError:
    print('Divide by zero')
except NameError:
    print('Invalid name')
except:
    print("Default handler")
else:
    print("No errors.")
finally:
    print('Clean up acionts.')

# 10.引入第三方代码的三种方式
import math
print(math.gcd(4, 6))  # 2
import math as m
print(m.gcd(4, 6))
from math import gcd
print(gcd(4, 6))
from math import *
print(sqrt(gcd(4, 6)))

# 11.自定义函数的4种方法


def a_stub_function():
    pass


def add(m, n):
    return m + n

a = add(1, 2)
print(a)
a = add(n=2, m=3)
print(a)


def addx(m=2, n=1):
    return m + n

print(addx())


def addy(*args):
    tmp = 0

    for i in args:
        tmp += i

    return tmp

print(addy(1, 2, 3, 4))


def addz(**args):
    tmp = 0
    for i in args:
        tmp += args[i]

    return tmp

print(addz(n1=1, n2=2, n3=3))


def addzz(*args, **k_args):
    tmp = 0

    for i in args:
        tmp += i

    for i in k_args:
        tmp += k_args[i]

    return tmp

print(addzz(1, 2, n1=1, n2=2))

# 12.用class描述一个事物


class Person:
    """A general person class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def wakeup(self, at):
        print('{0} wake up at {1} am'.format(self.name, at))

    def __del__(self):
        print(self.name + ' is reclaimed')


mars = Person("Mars", 30)
print(mars.name)
print(mars.age)
print(hasattr(mars, 'name'))
print(getattr(mars, 'name'))
setattr(mars, 'name', '10')
print(mars.name)
# delattr(mars, 'name')
# print(getattr(mars, 'name'))

mars.wakeup(at=7)

mars = Person('mars', 30)
eleven = mars
print(id(mars))
print(id(eleven))

del eleven
print('only 1 ref')

del mars


class Employee(Person):
    __counter = 0

    def __init__(self, work_id, name, age):
        Person.__init__(self, name, age)
        self.work_id = work_id
        Employee.__counter += 1

    def __str__(self):
        return "Employee"

    def __eq__(self, other):
        return self.name == other.name and \
                self.age == other.age and \
                self.work_id == other.work_id

mars = Employee(11, "mars", 30)
test = Employee(11, "mars", 30)
print(mars == test)

print(issubclass(Employee, Person))

print(isinstance(mars, Person))
print(isinstance(mars, Employee))
print(mars.__repr__())
print(mars.__str__())
print(Employee._Employee__counter)


