for n in range(1, 10 ** 5):
    for m in range(1, 10 ** 5):
        if n * m == 2023:
            a = n * (n + m)
            b = m * (m + n)
            if all(x % 23 == 0 for x in [a, b]):
                print(a, b)
