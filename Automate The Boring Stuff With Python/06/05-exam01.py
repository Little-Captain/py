#!/usr/bin/env python

tableData = [
    ['apples', 'oranges', 'cherries', 'banana', 'csfasawegsafd'],
    ['Alice', 'Bob', 'Carol', 'David', 'c'],
    ['dogs', 'cats', 'moose', 'goose', 'abc']
]

colWidths = [0] * len(tableData)
for i in range(len(tableData)):
    w = 0
    for item in tableData[i]:
        newW = len(item)
        if newW > w:
            w = newW
    colWidths[i] = w

row = len(tableData[0])
col = len(tableData)
for r in range(row):
    for c in range(col):
        if c == 0:
            print(tableData[c][r].rjust(colWidths[c]), end=' ')
        else:
            print(tableData[c][r].ljust(colWidths[c]), end=' ')
    print()

