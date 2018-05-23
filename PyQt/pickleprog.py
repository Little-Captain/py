import pickle
class rect:
    def __init__(self, x, y):
        self.l = x
        self.b = y
    def rectarea(self):
        return "Area of rectangle is", self.l * self.b
r = rect(5, 8)
f = open('studentinfo.bin', 'wb')
pickle.dump(r, f)
f.close()
del r
f = open('studentinfo.bin','rb')
storedobj = pickle.load(f)
print(type(storedobj))
print(storedobj.rectarea())
