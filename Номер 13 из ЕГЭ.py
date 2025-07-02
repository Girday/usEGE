'13'

'№60255 c Решу ЕГЭ'

from ipaddress import ip_network

n = ip_network('192.168.32.160/255.255.255.240',
               strict=False)  # strict - учитывает и широковекщательный адрес и адрес сети


def ip_to_bin(x):
    s = [int(i) for i in x.split('.')]

    'Перевод из системы с основанием 256 в DEC потом в BIN'
    c = s[0] * 256 ** 3 + s[1] * 256 ** 2 + s[2] * 256 + s[3]
    return f"{c:b}"

    'Перевод сразу в 8BIT штуковину'
    c = ''
    for j in s:
        c += bin(j)[2:].rjust(8, '0')  # rjust - свободное простраство слева заполняет нулями (битовое пространство)
    return c


g = 0
for i in n:
    i = str(i)
    a = ip_to_bin(i)
    if a.count('1') % 2 == 0:
        g += 1

print(g)

'----------------------------------------------------------------'

'№ 7040 с Полякова'

from ipaddress import ip_network

n = ip_network('186.135.80.0/255.255.252.0', strict=False)


def ip_to_bin(x):
    x = str(x)
    s = [int(i) for i in x.split('.')]
    c = s[0] * 256 ** 3 + s[1] * 256 ** 2 + s[2] * 256 + s[3]
    return f"{c:b}"


g = 0

for j in n:
    a = ip_to_bin(j)
    a1 = a[:16]
    a2 = a[16:]
    if a1.count('1') > a2.count('1'):
        g += 1

print(g)

'----------------------------------------------------------------'

'№ 7038 с Полякова'

from ipaddress import ip_network

ac = [128]
l = 128
for i in range(6, -1, -1):
    ac.append(l + 2 ** i)
    l += 2 ** i

for i in ac:
    n = ip_network('92.52.42.0/255.255.255.' + str(i), strict=False)
    for x in n:
        if str(x) == '92.52.42.52':
            print(i)
