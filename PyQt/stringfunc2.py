s = input("Enter a sentence: ")
print('The original sentence is:', s)
if s.startswith('It'):
    print('The entered sentence begins with the word It' )
if s.startswith('It', 0, 2):
    print('The entered sentence begins with the word It' )
if s.endswith('today'):
    print('The entered sentence ends with the word today' )
if s.endswith('today', 10, 15):
    print('The entered sentence ends with the word today' )
