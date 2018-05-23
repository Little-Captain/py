class rect:
    def __init__(self):
        self.l = 8
        self.b = 5
    def rectarea(self):
        return self.l * self.b
class triangle(rect):
    def __init__(self):
        rect.__init__(self)
        self.x = 17
        self.y = 13
    def trigarea(self):
        return 1/2 * self.x * self.y

r=triangle()
print("Area of rectangle is ", r.rectarea())
print("Area of triangle is ", r.trigarea())
