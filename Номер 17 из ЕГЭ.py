'17'

with open('17_2024.txt') as f:
    data = list(map(int, f.readlines()))

mx13 = max(elem for elem in data if str(elem).endswith('13'))

'or'

mx13 = max(elem for elem in data if str(elem)[-2:] == '13')

'or'

mx13 = max(elem for elem in data if abs(elem) % 100 == 13)


def f(x):
    return 99 < abs(x) < 1000
    'или return len(str(abs(x))) == 3'


ans = []

for i in range(len(data) - 2):
    if f(data[i]) + f(data[i + 1]) + f(data[i + 2]) == 2:
        if sum(data[i: i + 3]) <= mx13:
            ans.append(sum(data[i: i + 3]))

print(len(ans), max(ans))

'----------------------------------------------------------------'

'Проверка на простое число'


def is_prime(n):
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True


'----------------------------------------------------------------'

'Поляковский'


def sum_d(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s


maximum = 0
min_sum = 1000
c = 0
max_sum = 0
with open('123.txt') as f:
    lst = [int(i) for i in f]

for i in range(len(lst)):
    s = sum_d(lst[i])
    if s < min_sum:
        maximum = lst[i]
        min_sum = s
    elif s == min_sum:
        if lst[i] > maximum:
            maximum = lst[i]

for i in range(len(lst) - 1):
    if lst[i] > maximum and lst[i + 1] > maximum:
        c += 1
        s = sum_d(lst[i]) + sum_d(lst[i + 1])
        if s > max_sum:
            max_sum = s
print(c, max_sum)

'----------------------------------------------------------------'

with open('17-1.txt') as f:
    s = list(map(int, f.read().split('\n')[:-1]))

max_sum = -20000
cur_sum = 0
avg = sum(s) / len(s)
c = 0

for i in range(len(s) - 1):
    if (s[i] > avg) + (s[i + 1] > avg) >= 1 and (s[i] % 17 == 0) + (s[i + 1] % 17 == 0) >= 1:
        c += 1
        cur_sum = s[i] + s[i + 1]

    if cur_sum > max_sum:
        max_sum = cur_sum
        cur_sum = 0

print(c, max_sum)

'----------------------------------------------------------------'

'С тренировки 2.12.23'

with open('17_2024.txt') as f:
    lst = [int(x) for x in f]

minimum = min(lst)
c = 0
maximum = 0

for i in range(len(lst) - 1):
    if lst[i] % 117 == 0 or lst[i] % 117 == 0:
        c += 1
        if lst[i] + lst[i + 1] > maximum:
            maximum = lst[i + 1] + lst[i]

print(c, maximum)

'----------------------------------------------------------------'

'С АКР_вариант_2 (копия)'

with open('17.txt') as f:
    s = [int(x) for x in f.read().split('\n')]

max_su = -300_000
count = 0
for i in range(len(s) - 2):
    el1 = s[i]
    el2 = s[i + 1]
    el3 = s[i + 2]
    if len(str(abs(el1))) == 2 or len(str(abs(el2))) == 2 or len(str(abs(el3))) == 2:
        fac1 = str(el1).endswith('19')
        fac2 = str(el2).endswith('19')
        fac3 = str(el3).endswith('19')
        if fac1 or fac2 or fac3:
            els = [el1, el2, el3]
            oka = []
            for elem in els:
                if str(elem).endswith('19'):
                    oka.append(elem)
            m_oka = max(oka)
            su = sum(els)
            if su < m_oka:
                count += 1
                if max_su < su:
                    max_su = su

print(f'{count}; {max_su}')
