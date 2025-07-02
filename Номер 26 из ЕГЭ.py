'26'

'Задание 26_25.01.2024_открытый_2022 c PUM.MAI.RU'

with open('26.txt') as f:
    s = f.read().split('\n')

max_s, N = map(int, s[0].split())
a = []
for i in s[1:]:
    a.append(int(i))
a.sort()

max_n = 0
s = 0  # Промежуточный счётчик для суммы
i = 0

while s + a[i] < max_s:
    s += a[i]
    max_n += 1
    i += 1

s -= a[max_n - 1]
i = len(a) - 1
while s + a[i] > max_s:
    i -= 1

print(max_n, a[i])

'----------------------------------------------------------------'

'26_2023_25.01.2024_открытый_2023_01 c PUM.MAI.RU'

with open('26.txt') as f:
    s = f.read().split('\n')
    N = int(s[0])
    s.remove(s[0])
    s = [tuple(map(int, x.split())) for x in s]

s.sort(key=lambda x: x[0])
b = [s[0]]
k = 0

for i in range(1, len(s)):
    if s[i][0] >= b[k][1]:
        b.append(s[i])
        k += 1
    elif s[i][1] < b[k][1]:
        b[k] = s[i]

print(len(b), s[-1][0] - b[-2][1])

'----------------------------------------------------------------'

'26_Тренировочная_работа_01.02.2024_вариант_04 c PUM.MAI.RU'

from math import ceil

with open('26.txt') as f:
    N = int(f.readline())
    s = sorted([int(x) for x in f.read().split('\n')])
    pod = [x for x in s if x <= 150]
    s = [x for x in s if x > 150]

p = 0
for x in range(len(s) // 2):
    p += s[x] * 0.8

print(sum(pod) + sum(s[len(s) // 2:]) + ceil(p), s[x])

'----------------------------------------------------------------'

'26_06.02.2024_Задача_№60_kpolyakov.spb.ru с PUM.MAI.RU'

with open('26.txt') as f:
    k, n = map(int, f.readline().split())
    places = []
    for _ in range(k):
        places.append(int(f.readline()))
    a = [[] for _ in range(k)]
    for _ in range(n):
        score, way = map(int, f.readline().split())
        a[way].append(score)

for way in a:
    way.sort(reverse=True)

n = 0
ko = []
for i in range(len(a)):
    n += min(len(a[i]), places[i])
    ko.append(len(a[i]) / places[i])

i = ko.index(max(ko))
print(n, a[i][:places[i]][-1])

'----------------------------------------------------------------'

'№ 3023 из КЕГЭ'

from re import finditer

mat = [['0'] * 480 for _ in range(640)]
with open('26.txt') as f:
    n = int(f.readline())
    s = [list(map(int, x.split())) for x in f.readlines()]
    for x in s:
        i, j = x[0] - 1, x[1] - 1
        mat[i][j] = '1'

a = []
for x in range(len(mat)):
    y = ''.join(mat[x])
    for m in finditer(r'(10)*1', y):
        a.append([m.group().count('1'), x + 1])

a.sort(key=lambda x: x[0], reverse=True)
obj = a[0][0]
fact = [x for x in a if x[0] == obj]

print(*min(fact, key=lambda x: x[1]))


'----------------------------------------------------------------'

'№ 4115 из КЕГЭ'

with open('26.txt') as f:
    n = int(f.readline())
    s = set([x[:-1] for x in f.readlines()])
    a = []
    for x in s:
        a.append(tuple(x.split()))

a.sort(key=lambda x: (x[0], x[1]))

c = 0
prod = []
for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    first, second = int(x[0]), int(x[1])
    if int(y[0]) == first and int(y[1]) == second + 1:
        c += 1
    else:
        prod.append([c + 1, first])
        c = 0

fact = sorted(prod, key=lambda x: x[0], reverse=True)
obj = fact[0][0]
con = [x for x in fact if x[0] == obj]

print(*min(con, key=lambda x: x[1]))
