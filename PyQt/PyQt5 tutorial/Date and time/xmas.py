from PyQt5.QtCore import QDate

xmas1 = QDate(2016, 12, 24)
xmas2 = QDate(2017, 12, 24)
nextyear = QDate(2018, 1, 1)

now = QDate.currentDate()

dayspassed = xmas1.daysTo(now)
print("{0} days have passed since last XMas".format(dayspassed))

nofdays = now.daysTo(xmas2)
print("There are {0} days until next XMas".format(nofdays))

print("There are {0} days until next year".format(now.daysTo(nextyear)))