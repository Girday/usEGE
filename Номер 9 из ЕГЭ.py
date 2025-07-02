from collections import Counter

with open('9.csv') as f:
    text = f.read()

lines = text.split('\n')[:-1]
n = 0

for line in lines:
    a = list(map(int, line.split(',')))
    c = Counter(a)
    counts = list(c.values())
    if not (counts.count(2) == 2 and counts.count(1) == 3):
        continue
    s = 0
    for key, value in c.items():
        if value == 2:
            s += key
    avg1 = s / 2
    avg2 = sum(a) / 7
    if avg1 >= avg2:
        continue
    n += 1

print(n)


'----------------------------------------------------------------'

'№56509 с Решу ЕГЭ'

with open('9.csv') as f:
    s = [list(map(int, x.split(';'))) for x in f.readlines()]

c = 0
for x in s:
    se = list(set(x))
    if len(se) < len(x) and any((x.count(b) == 1) for b in se):
        pov, nep = [], []
        for i in x:
            if x.count(i) == 1:
                nep.append(i)
            else:
                pov.append(i)
        sr1, sr2 = (sum(pov) / len(pov)), (sum(nep) / len(nep))
        if sr2 > sr1:
            c += 1

print(c)

