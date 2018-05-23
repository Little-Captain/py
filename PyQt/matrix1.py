table = [ [ 0 for i in range(3) ] for j in range(3) ]
print("Enter values for a matrix of order 3 x 3")
for d1 in range(3):
    for d2 in range(3):
        table[d1][d2] = int(input())
print("Elements of the matrix are", table)
print("Elements of the matrix are")
for row in table:
    print(row)
s = 0
for row in table:
    for n in row:
        s += n
print("The sum of elements in matrix is", s)
