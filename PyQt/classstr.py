class rect:
    def __init__(self, x,y):
        self.l = x
        self.b = y
    def __str__(self):
        return 'Length is %d, Breadth is %d' % (self.l, self.b)
    def rectarea(self):
        return self.l * self.b
r = rect(5, 8)
print(r)
print("Area of rectangle is ", r.rectarea())
