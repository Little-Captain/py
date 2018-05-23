class student:
    def __init__(self, r, n):
        self.roll = r
        self.name = n
    def showstudent(self):
        print("Roll : ", self.roll)
        print("Name is ", self.name)
class science:
    def __init__(self, p, c):
        self.physics = p
        self.chemistry = c
    def showscience(self):
        print("Physics marks : ", self.physics)
        print("Chemistry marks : ", self.chemistry)
class results(student, science):
    def __init__(self, r, n, p, c):
        student.__init__(self, r, n)
        science.__init__(self, p, c)
        self.total = self.physics + self.chemistry
        self.percentage = self.total / 200 * 100
    def showresults(self):
        student.showstudent(self)
        science.showscience(self)
        print("Total marks : ", self.total)
        print("Percentage marks : ", self.percentage)
s = results(101, 'David', 65, 75)
print("Result of student is ")
s.showresults()
