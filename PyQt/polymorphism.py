class book:
    def __init__(self, x):
        self.price = x
class stockist(book):
    def __init__(self, x):
        book.__init__(self, x)
    def commission(self):
        self.comm = self.price * 5 / 100
        print("Commission of Stockist is %.2f" % self.comm)
class distributor(book):
    def __init__(self, x):
        book.__init__(self, x)
    def commission(self):
        self.comm = self.price * 8 / 100
        print("Commission of Distributor is %.2f" % self.comm)
class retailer(book):
    def __init__(self,x):
        book.__init__(self,x)
    def commission(self):
        self.comm = self.price * 10 / 100
        print("Commission of Retailer is %.2f" % self.comm)
r = stockist(100)
s = distributor(100)
t = retailer(100)
prncomm = [r, s, t]
for c in prncomm:
    c.commission()
