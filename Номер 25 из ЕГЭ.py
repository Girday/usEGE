'25'

'Легчайший способ решения маски от Афони :3'

import re  # Регулярные выражения

for i in range(31007, 10 ** 10 + 1, 31007):
    if re.match(r'^1[0-9]*34[0-9]5[0-9]9$', str(i)):  # Паттерн-матчинг
        print(i, i // 31007)
'----------------------------------------------------------------'

for i in range(12007, 10 ** 10 + 1, 12007):
    if re.match(r'^9[0-9]*[0-9]001[0-9]1$', str(i)):
        print(i, i // 12007)

'------------------------------------------------------------'

'+- 3 тип с делителями'


def is_prime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


c = 0
n = 450_001
while c != 6:
    d = n // 2 + 1
    while d > 1:
        if n % d == 0:
            if not (is_prime(d)):
                print(n, d)
                c += 1
            break
        else:
            d -= 1
    n += 1
'----------------------------------------------------------------'


def deliteli(n):
    a = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    d = sorted(list(set(a)))
    return d


c = 0
m = 800_000 - 1
while c != 5:
    ma = max(deliteli(m)[:-1])
    mi = min(deliteli(m)[1:])
    M = ma - mi
    if M % 17 == 0:
        print(m, M)
        c += 1
    m -= 1

'----------------------------------------------------------------'

'Из Полякова (хрень какая-то)'

N = 473265 // 2 + 1

primes = [i for i in range(N + 1)]
primes[1] = 0
i = 2
while i <= N:
    if primes[i] != 0:
        j = i * i
        while j <= N:
            primes[j] = 0
            j += 1
    i += 1
primes = [i for i in primes if i != 0]

n = 0
s = 0
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        if 412567 <= primes[i] * primes[j] <= 473265:
            s += primes[i] * primes[j]
            n += 1

print(n, s // n)

'------------------------------------------------------------'

'№ 6786 с Полякова'

from re import match


def ras(n):  # Разложение на простые множители
    b = 2
    res = []
    while n > 1:
        while n % b == 0:
            res.append(b)
            n //= b
        b += 1
    return res


for i in range(2, 10 ** 4):
    g = ras(i)
    if match(r'^[0-9]*2[0-9]2$', str(i)) and len(g) == 7:
        print(i, max(g))

'--------------------------------------------------------'

'№ 6785 с Полякова'

from re import match

for i in range(2468037, 10 ** 9, 13):
    if match(r'^24[02468]*68[39]35$', str(i)):
        print(i, i // 13)

'--------------------------------------------------------'

'№ 6655 с Полякова'

from re import match

for i in range(123046606, 124 * 10 ** 9, 4013):
    if match(r'^123[0-9]4[0-9]*5679$', str(i)):
        print(i, i // 4013)

'--------------------------------------------------------'

'№ 6654 с Полякова'

from re import match

for x in range(10 ** 6, 1, -1):
    c = 0
    delit = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            delit.append(i)
            delit.append(x // i)
    delit.sort()
    if len(delit) >= 24:
        p = []
        for i in delit:
            if match(r'^4[0-9]*$', str(i)):
                c += 1
                p.append(i)
        if c == 24:
            print(x, max(p))
