class rect:
    def __init__(self):
        self.l = 8
        self.b = 5
    def rectarea(self):
        return self.l * self.b
r = rect()
print("Area of rectangle is ", r.rectarea())
