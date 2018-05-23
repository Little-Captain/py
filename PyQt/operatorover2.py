class rect:
    def __init__(self, x, y):
        self.l = x
        self.b = y
    def __str__(self):
        return 'Length is %d, Breadth is %d' % (self.l, self.b)
    def __eq__(self, other):
        return ((self.l == other.l) and (self.b == other.b))
    def rectarea(self):
        return self.l * self.b
r1 = rect(5,8)
r2 = rect(10,20)
if r1 == r2:
    print('The two instances are equal')
else:
    print('The two instances are not equal')

r2 = rect(5,8)
if r1 == r2:
    print('The two instances are equal')
else:
    print('The two instances are not equal')
