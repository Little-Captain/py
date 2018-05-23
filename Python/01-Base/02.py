import random
player = input('请输入: 剪刀(0) 石头(1) 布(2):')
player = int(player)
computer = random.randint(0, 2)

if ((player == 0) and (computer == 2)) or ((player ==1) and (computer == 0)) or ((player == 2) and (computer == 1)):
    print('win')
elif player == computer:
    print('small')
else:
    print('lose')

i = 10
while i > 0:
    print(i)
    i -= 1

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

name = 'Little-Captain'
for x in name:
    print(x)
else:
    print('completion')
