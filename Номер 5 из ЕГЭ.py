'''Задача 5'''

'''

Перевод в любую СС

def a(n, p):
    lst = []
    while n:
        lst.append(n % p)
        n //= p
    return lst[::-1]
    
'''




def f(n):
    b = bin(n)[2:] # Важно, т.к. bin() выводит лишние 2 символа (служебные)
    if n % 3 == 0:
        b += b[-3:]
    else:
        b += bin((n % 3) * 3)[2:]
    return int(b, 2)

ans = []

for i in range(1, 100):
    if f(i) <= 150:
        ans.append(i)

print(max(ans))


'Если нужно переводить в нестандартную СС'

def s80(n):
    s = []
    while n:
        s.append(n % 80)
        n //= 80
    return s

'Сложная 5-я'

a = []

for i in range(10 ** 8, 10 ** 9):
    s = 0
    for digit in str(i):
        s += int(digit)
    bi = bin(s)[2:]
    if bi.count('1') % 2 == 0:
        bi = '1' + bi + '00'
    else:
        bi = '10' + bi + '1'

    if int(bi, 2) == 21:
        a.append(i)

print(len(a))

'Ещё с Решу ЕГЭ'

for N in range(1, 100):
    b = bin(N)[2:]
    if sum([int(x) for x in b]) % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    if int(b, 2) > 40:
        print(N)
        exit()

'----------------------------------------------------------------'
def troic(a):
    s = ''
    while a:
        s += str(a % 3)
        a //= 3
    return s[::-1]


def coun(a):
    return len(str(a))


for N in range(1, 1000):
    b = troic(N) + str(N % 3)
    if coun(int(b, 3)) == 4:
        print(int(b, 3))

'----------------------------------------------------------------'

for N in range(1000, 10000):
    bob = [int(x) for x in str(N)]
    s = [bob[0] + bob[1],
          bob[1] + bob[2],
          bob[2] + bob[3]]
    s.sort(reverse=True)
    s = s[:-1]
    if ''.join([str(i) for i in s]) == '1514':
        print(N)
        break

'----------------------------------------------------------------'

for N in range(1, 1000):
    b = bin(N)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    if int(b, 2) > 96:
        print(int(b, 2))
        break

'----------------------------------------------------------------'

'№7663 с Решу ЕГЭ'
a = []

for N in range(100, 1000):
    c = str(N)
    s1 = int(c[0]) + int(c[1])
    s2 = int(c[1]) + int(c[2])
    if s1 < s2:
        s1, s2 = s2, s1
    s = str(s1) + str(s2)
    if s == '1412':
        a.append(N)

print(min(a))
