class rect:
    def __init__(self):
        self.l = 8
        self.b = 5
    def area(self):
        return self.l * self.b
class triangle:
    def __init__(self):
        self.x = 17
        self.y = 13
    def area(self):
        return 1/2 * self.x * self.y
class both(rect, triangle):
    pass
r = both()
print("Area of rectangle is ", r.area())
print(r.l, r.b, r.x, r.y);
