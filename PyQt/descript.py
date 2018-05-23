class product:
    def __init__(self, name, x = 5):
        self.name = name
        self.price = x
    def __set__(self, obj, value):
        print ('Setting attribute' , self.name, obj, value)
        self.price = value
    def __get__(self, obj, objtype):
        print ('Getting attribute',self.name, obj, objtype)
        return self.price
class cart:
    p = product('butter', 7)
k = cart()
print(k.p)
k.p = 10
print(k.p)
