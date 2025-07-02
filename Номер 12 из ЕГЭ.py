'12'

'№9365 с Решу ЕГЭ'


def red(s):
    while '222' in s or '888' in s:
        if '222' in s:
            s = s.replace('222', '8', 1)
        else:
            s = s.replace('888', '2', 1)
    return s


s = '8' * 68

print(red(s))

'--------------------------------------------------------'

'№60254 с Решу ЕГЭ'


def red(s):
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:  # Не elif! т.к. в условии указано ЕСЛИ, а не ИНАЧЕ ЕСЛИ
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    return s


for n in range(9999, 2, -1):
    s = red('5' + '2' * n)
    if sum([int(x) for x in s]) == 64:
        print(n)
        exit()

'--------------------------------------------------------'

'№ 6824 с Полякова'


def red(s):
    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s = s.replace('18', '8', 1)
        if '388' in s:
            s = s.replace('388', '81', 1)
        if '888' in s:
            s = s.replace('888', '3', 1)
    return s


minres = 10000 - 1

for n in range(4, 10000):
    s = '1' + '8' * n
    res = red(s)
    if res.count('1') == 3 and n < minres:
        minres = n

print(minres)

'--------------------------------------------------------'

'№ 6737 с Полякова'


def red(s):
    while '17' in s or '377' in s or '777' in s:
        if '17' in s:
            s = s.replace('17', '1', 1)
        if '377' in s:
            s = s.replace('377', '73', 1)
        if '777' in s:
            s = s.replace('777', '3', 1)
    return s


for n in range(1, 1000):
    s = '1' + '7' * n
    res = red(s)
    if res.count('3') == 2:
        print(n)
        break

'--------------------------------------------------------'

'№ 6633 с Полякова'


def red(s):
    while '25' in s or '32' in s or '555' in s:
        while '555' in s or '11' in s or '2' in s:
            if '555' in s:
                s = s.replace('555', '1', 1)
            if '11' in s:
                s = s.replace('11', '25', 1)
            if '2' in s:
                s = s.replace('2', '5', 1)
    return sum(list(map(int, list(s))))


maximum = 0
min_n = []

for n in range(108, 1000, 9):
    s = '5' * n
    res = red(s)
    if res > maximum:
        maximum = res
        min_n = [n]
    elif res == maximum:
        min_n.append(n)

print(min(min_n))
