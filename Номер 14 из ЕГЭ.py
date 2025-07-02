'14'

'Прямое сложение в СС'

a = 2 * 729 ** 1333 + 2 * 243 ** 1334 - 81 ** 1335 + 2 * 27 ** 1336 - 2 * 9 ** 1337 - 2024
n = 0

while a:
    if a % 27 > 9:
        n += 1
    a //= 27

print(n)

'--------------------------------------------------------'

'''

Вот так можно достать буквы алфавита какой-нибудь СС

from string import ascii_uppercase

n = 27
alp = '0123456789' + ascii_uppercase[:n - 10]
print(alp)

Весь алфавит: ABCDEFGHIJKLMNQPRSTUVWXYZ
'''

'Операции в одной СС'

b = []

for x in '0123456789ABCDEFGHJKLMNOPQ':
    a = int(f'14353{x}17', 27) + int(f'137{x}21', 27)
    if a % 26 == 0:
        b.append(a // 26)
print(b[-1])
