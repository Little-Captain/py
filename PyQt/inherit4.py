class student:
    def __init__(self, r, n):
        self.roll = r
        self.name = n
    def showstudent(self):
        print("Roll : ", self.roll)
        print("Name is ", self.name)
class science(student):
    def __init__(self, r, n, p, c):
        student.__init__(self, r, n)
        self.physics = p
        self.chemistry = c
    def showscience(self):
        student.showstudent(self)
        print("Physics marks : ", self.physics)
        print("Chemistry marks : ", self.chemistry)
class arts(student):
    def __init__(self, r,n,h,g):
        student.__init__(self,r,n)
        self.history = h
        self.geography=g
    def showarts(self):
        student.showstudent(self)
        print("History marks : ", self.history)
        print("Geography marks : ", self.geography)
s = science(101, 'David', 65, 75)
a = arts(102, 'Ben', 70, 60)
print("Information of science student is ")
s.showscience()
print("\nInformation of arts student is ")
a.showarts()
