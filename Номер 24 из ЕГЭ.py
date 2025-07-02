'24'

with open('k7a-2.txt') as f:
    s = f.read()

cur_lenght = 0
max_lenght = 0

for i in s:
    if i == 'A' or i == 'B' or i == 'E' or i == 'F':
        cur_lenght += 1
        if cur_lenght > max_lenght:
            max_lenght = cur_lenght
    else:
        cur_lenght = 0

print(max_lenght)

# or

s = s.replace('C', ' ').replace('D', ' ').split()
print(len(max(s, key=len)))

'----------------------------------------------------------------'

'Из допов'

sog = 'BCD'
gl = 'AO'

lst = [i + j for i in sog for j in gl]

cur_len = 0
max_len = 0
flag = False

for i in range(len(s) - 1):
    if flag:
        flag = False
        continue
    if s[i] + s[i + 1] in lst:
        cur_len += 1
        flag = True
    else:
        if cur_len > max_len:
            max_len = cur_len
        cur_len = 0

print(max_len)

'----------------------------------------------------------------'

'Задание 24. №№181-185 с PUM.MAI.RU c точками'

with open('24.txt') as f:
    s = f.read()

k = 4  # Количество точек

to = []
for x in range(len(s)):
    if s[x] == '.':
        to.append(x)

to.insert(0, -1)
to.append(len(s))

su = []
for i in range(len(to) - (k + 1)):
    su.append(to[i + (k + 1)] - to[i] - 1)

print(max(su))

'----------------------------------------------------------------'

'Задание 24. № 187 с PUM.MAI.RU c точками'

with open('24.txt') as f:
    s = f.read()

s = s.split('.')
max_l = 0

for elem in s:
    if elem.count('A') >= 3:
        max_l = max(max_l, len(elem))

print(max_l)


'----------------------------------------------------------------'

'Задание 24. № 188 с PUM.MAI.RU c точками'

with open('24.txt') as f:
    s = f.read()

s = s.split('Y')
max_l = 0

for elem in s:
    if elem.count('.') >= 5:
        max_l = max(max_l, len(elem))

print(max_l)

'----------------------------------------------------------------'

'Задание 24. Открытый вариант №1_ 2023 c PUM.MAI.RU'

with open('24.txt') as f:
    s = f.read()

k = 100  # Количество точек

to = []
for x in range(len(s)):
    if s[x] == 'T':
        to.append(x)

to.insert(0, -1)
to.append(len(s))

su = []
for i in range(len(to) - (k + 1)):
    su.append(to[i + (k + 1)] - to[i] - 1)

print(max(su))

'----------------------------------------------------------------'

'Задание 24. Задача № 189 c PUM.MAI.RU с точками'

with open('24.txt') as f:
    s = f.read()

s = s.split('.')
max_l = 0
print(s)

for elem in s:
    if (elem.count('A') + elem.count('E') + elem.count('I') + elem.count('O') + elem.count('U') + elem.count('Y')) <= 7:
        max_l = max(max_l, len(elem))

print(max_l)

'----------------------------------------------------------------'

'24_22.02.2024_вариант 16 c PUM.MAI.RU'

with open('24.txt') as f:
    s = f.read()

s = s.split('TAA')
k = []
l = []

for i in s:
    p = i.find('ATG')
    k.append(i[p:])

for i in k:
    i = i.replace('ATG', '*', 1)
    if 'TGA' in i or 'TAG' in i:
        continue
    else:
        l.append(i)

g = max(l, key=len).replace('*', 'ATG', 1) + 'TAA'

print(len(g))
