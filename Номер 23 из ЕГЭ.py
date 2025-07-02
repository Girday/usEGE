'23'

'№ 11358 с Решу ЕГЭ'


def f(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a + 2, b) + f(a * 2, b)


print(f(3, 10) * f(10, 12))

'--------------------------------------------------------'

'№ 38957 с Решу ЕГЭ'


def f(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a * 3, b)


print(f(2, 28) * f(28, 90))

'--------------------------------------------------------'

'№ 6835 с Полякова'


def f(a, b):
    if (a > b) or (a == 23):
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 2, b) + f(a * 3, b) + f(a * 5, b)


print(f(1, 13) * f(13, 75))

'--------------------------------------------------------'

'№ 6062 с Полякова'


def f(a, b):
    g = str(a)
    if (a > b) or ('6' in g):
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a + 2, b) + f(a * 2, b)


print(f(1, 38))

'--------------------------------------------------------'

'№ 5216 с Полякова'


def f(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(int('2' + str(a)), b)


print(f(3, 678))

'--------------------------------------------------------'

