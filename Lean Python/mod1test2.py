from mod1 import greeting, hello, writtenby

hello()
hello.writtenby = 'xxxx'
print('written by', hello.writtenby)
print(writtenby)

greet = greeting()
greet.morning()
greet.evening()