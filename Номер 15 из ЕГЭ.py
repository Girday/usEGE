'15'

'Координатная плоскость'

for A in range(1, 1000):
    flag = True
    for x in range(1, 100):
        if not('выражение'):
            flag = False
    if flag:
        print(A)

'Или так - через all'

for A in range(1, 1000):
    if all('выражение' for x in range(1, 1000))):
        print(A)

'----------------------------------------------------------------'

'Задача с делителем'

def delit(n, m):
    return n % m == 0


for A in range(1, 5000):
    if all(((delit(x, 2) <= (not(delit(x, 13)))) or ((x + A) >= 1000)) for x in range(1, 5000)):
        print(A)

'----------------------------------------------------------------'

'Битовые логические опирации'

for A in range(1, 1000):
    if not(any((((x & A) != 0) and ((x & 58) == 0) and ((x & 22) == 0)) for x in range(1, 1000))):
        print(A)
