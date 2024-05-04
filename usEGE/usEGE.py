from ipaddress import ip_network


def trio(n: int) -> str:
    s = ''
    while n:
        s += str(n % 3)
        n //= 3
    return s[::-1]


def de(n: int, m: int) -> bool:
    return n % m == 0


def IP(ad: str, mask: str) -> list:
    a = []
    ip = [list(map(int, str(x).split('.'))) for x in ip_network(f'{ad}/{mask}')]
    for i in ip:
        s = ''
        for j in i:
            s += f'{j:08b}'
        a.append(s)
    return a


def pref_sum(a: list) -> list:
    b = [0] * (len(a) + 1)
    for i in range(1, len(b)):
        b[i] = b[i - 1] + a[i - 1]
    return b
