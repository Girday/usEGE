'16'

'№33095 с Решу ЕГЭ'
def f(n):
    if n == 1:
        return 1
    elif n % 2 != 0 and n > 1:
        return n + f(n - 2)
    elif n % 2 == 0:
        return n * f(n - 1)


print(f(40))
