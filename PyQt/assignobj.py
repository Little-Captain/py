class rect:
    def __init__(self, x, y):
        self.l = x
        self.b = y
    def rectarea(self):
        return self.l * self.b
r = rect(5, 8)
s = r
print(r)
print(s)
print("Area of rectangle is ", r.rectarea())
print("Area of rectangle is ", s.rectarea())
