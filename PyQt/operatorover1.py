class rect:
    def __init__(self, x, y):
        self.l = x
        self.b = y
    def __str__(self):
        return 'Length is %d, Breadth is %d' % (self.l, self.b)
    def __add__(self, other):
        print(self.l)
        return rect(self.l + other.l, self.b + other.b)
    def rectarea(self):
        return self.l * self.b
r1 = rect(5, 8)
r2 = rect(10, 20)
r3 = r1 + r2
print(r3)
print("Area of rectangle is ", r3.rectarea())
