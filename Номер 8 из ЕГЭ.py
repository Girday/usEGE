from itertools import product, permutations

'Если нужно найти слово на каком-то месте (место - 1)'

words = list(product('АОУ', repeat=5))

print(*words[209])

'Ограничения на буквы'

words = list(product('ЖАСМИН', repeat=5))
glas = 'АИ'
n = 0

for word in words:
    c = ''.join(word)
    if c[0] != 'Ж' and c[-1] != 'С':
        if c.count('И') + c.count('А') == 1:
            n += 1
print(n)

'Если нужно найти 1 букву'

# product умеет реешать комбинации

words = product('АДЖИКА', repeat=6)  # мы хотим сделать декартово произведение этих строк

n = 0

for word in words:
    if "О" in word:  # БУКВА - РУССКАЯ!!
        n += 1

print(n)

'Если нужно найти 2+ буквы'

for word in words:
    if word.count('О') >= 2:  # БУКВА - РУССКАЯ!!
        n += 1

print(n)

'Если нужно найти букву после чего-нибудь'

for word in words:
    if word.count('О') != 1:
        continue
    if word[0] == 'О':
        continue
    pos = word.index('О')
    if word[pos - 1] not in 'СРП':
        continue
    n += 1

print(n)

'--------------------------------------------------------'

'Где все буквы встречаются ровно 1 раз либо сказано, что использована перестановка'

words = set(permutations('ВЕНТИЛЬ', 7))  # permutations - все возможные перестаноки

n = 0

for word in words:
    if word[-1] == 'Ь':
        continue
    w = ''.join(word)
    pos = word.index('Ь')
    if 1 <= pos <= 5:
        if w[pos - 1] in 'ЕИ' and w[pos - 1] in 'ЕИ':
            continue
    n += 1

print(n)

'Мы избегаем подряд идущих букв'

words = permutations('АДЖИКА')

n = 0

good = set()

for word in words:
    flag = True
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            flag = False
    if flag:
        good.add(word)
print(len(good))

'Когда нужно найти по алфавиту'

words = set(permutations('КОНДРАТ', 7))
words = [''.join(w) for w in words]
words.sort()

print(*words[2232])

'Когда нужно найти соотношение гласных и согласных'

words = set(product('ВАСИЛИСА', repeat=6))

n = 0

for word in words:
    g = 0
    s = 0
    for c in word:
        if c in 'АИ':
            g += 1
        else:
            s += 1
    if g > s:
        n += 1

print(n)

'----------------------------------------------------------------'

'Про числа'


def f(x):
    s = 0
    for elem in '1357':
        s += x.count(elem + '6') + x.count('6' + elem)
    return s


s = '01234567'
data = [''.join(elem) for elem in product(s, repeat=5) if elem[0] != '0' and elem.count('6') == 1]
data = [elem for elem in data if not f(elem)]
print(len(data))

from itertools import product, permutations

a = list(product('ЕПСУХ', repeat=5))
j = 1

for i in a:
    c = ''.join(i)
    if c == 'УСПЕХ':
        print(j)
    if i[-1] != 'У' and i[-1] != 'Е':
        j += 1

'----------------------------------------------------------------'

a = list(permutations('ТИМАШЕВСК'))

sogl = 'ТМВШСК'
glas = list(permutations('ИАЕ'))
c = 0

for elem in a:
    d = ''.join(elem)  # Составляем строку из кортежа
    if elem[0] in sogl and elem[-1] in sogl:  # Проверяем на окончание на согласную
        for gl in glas:  # Перебираем все наборы из 3 букв
            e = ''.join(gl)  # Составляем строку из кортежа
            if e in d:  # В строке из ТИМАШЕВСК есть 3 подряд идущие гласные буквы
                c += 1

# or

for elem in a:
    d = ''.join(elem)  # Составляем строку из кортежа
    if elem[0] in sogl and elem[-1] in sogl:  # Проверяем на окончание на согласную
        if any(''.join(gl) in d for gl in glas):
            c += 1

print(c)

'----------------------------------------------------------------'

a = list(product('ПРОЛИВ', repeat=6))

d = 0

for elem in a:
    c = ''.join(elem)
    if c.count('П') >= 1:
        d += 1

print(d)

'----------------------------------------------------------------'

'Задача Джобса (№6625 с Полякова)'

a = list(product('XO', repeat=12))
d = 0

for elem in a:
    c = ''.join(elem)
    if c.count('O') == 5:
        if 'OOOOO' not in c:
            d += 1

p = 1
for i in range(1, 8):
    p *= i

p1 = 1
for i in range(1, 6):
    p1 *= i

print(p * p1 * d)

'----------------------------------------------------------------'

'Про цифры'

al = [str(i) for i in range(0, 8)]
nechet = [str(i) for i in range(1, 8, 2)]
c = 0
for a1 in al[1:]:
    for a2 in al:
        for a3 in al:
            for a4 in al:
                for a5 in al:
                    s = a1 + a2 + a3 + a4 + a5
                    if s.count('6') == 1:
                        d = s.find('6')
                        if d == 4:
                            if s[3] not in nechet:
                                c += 1
                        elif d == 0:
                            if s[1] not in nechet:
                                c += 1
                        else:
                            if s[d - 1] not in nechet and s[d + 1] not in nechet:
                                c += 1

print(c)

'Или так'

al = [str(i) for i in range(9)]
povt = [str(i) * 2 for i in range(9)]
lst = list(product(al, repeat=7))
c = 0

for zap in lst:
    a = ''.join(zap)
    flag = True
    if a[0] != '0' and a[0] != '3' and a[0] != '7':
        for zna in povt:
            if zna in a:
                flag = False
        if flag:
            c += 1

print(c)

'№5890 С Полякова'

from itertools import product

lst = list(product('01234567', repeat=6))
chet = '0246'
b = 0
s = [''.join(x) for x in product(chet, repeat=3)]

for i in lst:
    c = ''.join(i)
    if all((x not in c) for x in s) and all(int(c[0]) < int(x) for x in c[2:]) and all(
            int(c[1]) < int(x) for x in c[2:]) and c[0] != '0':
        b += 1

print(b)
