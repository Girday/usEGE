def f(a, c):
    if c > 4:
        return 0
    if (c == 2 or c == 4) and a >= 386:
        return 1
    elif (c != 2 or c != 4) and a >= 386:
        return 0
    else:
        if c % 2 == 1:
            return f(a + 1, c + 1) or f(a + 4, c + 1) or f(a * 2, c + 1)
        else:
            return f(a + 1, c + 1) and f(a + 4, c + 1) and f(a * 2, c + 1)


def f1(a, c):
    if c > 2:
        return 0
    if c == 2 and a >= 386:
        return 1
    elif c != 2 and a >= 386:
        return 0
    else:
        if c % 2 == 1:
            return f1(a + 1, c + 1) or f1(a + 4, c + 1) or f1(a * 2, c + 1)
        else:
            return f1(a + 1, c + 1) and f1(a + 4, c + 1) and f1(a * 2, c + 1)


for s in range(1, 386):
    if f(s, 0) and not f1(s, 0):
        print(s)
