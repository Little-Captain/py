m1 = [ [1, 2], [3, 4], [5, 6], [7, 8] ]
m2 = [ [9, 8], [7, 6], [5, 4], [3, 2] ]
m3 = [ 2*[0] for i in range(4) ]
print("Addition of two matrices is")
for i in range(4):
    for j in range(2):
        m3[i][j] = m1[i][j] + m2[i][j]
for row in m3:
    print (row)
