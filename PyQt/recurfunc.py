def addseq(x):
    if x == 1: return 1
    else: return x + addseq(x-1)
print('The sum of first 10 sequence numbers is', addseq(10))
