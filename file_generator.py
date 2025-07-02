from random import randint as ran

f = open('26.txt', 'w')
f.write('100000\n')
for i in range(100000):
    f.write(f'{ran(1, 500)} {ran(1, 400)}\n')
print('end')
