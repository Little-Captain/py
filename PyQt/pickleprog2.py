import pickle
class user:
    def __init__(self, x, y, z):
        self.id = x
        self.name = y
        self.emailadd = z
    def dispuser(self):
        print('User ID:', self.id)
        print('User Name:', self.name)
        print('Email Address:', self.emailadd)
f = open('UsersInfo.bin', 'wb')
n = int(input('How many users? '))
print('Enter', n, 'numbers')
for i in range(0, n):
    u = input('User ID: ')
    n = input('User Name: ')
    e = input('Email Address: ')
    usrobj = user(u, n, e)
    pickle.dump(usrobj,f)
f.close()
print('\nInformation of the users is:')
f = open('UsersInfo.bin', 'rb')
while True:
    try:
        usrobj = pickle.load(f)
    except EOFError:
        break
    else:
        usrobj.dispuser()
f.close()
