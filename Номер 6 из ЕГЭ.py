from turtle import *
from math import tan, pi

k = 20
speed(0)
delay(0)

lt(90)

for i in range(7):
    fd(10 * k)
    rt(120)

penup()

for x in range(-3, 15):
    for y in range(-5, 15):
        goto(x * k, y * k)
        dot(3)

mainloop()

'Решение математикой'

count = 0

for x in range(1, 10):
    for y in range(1, 10):
        if -x / 3 ** 0.5 + 10 > y > x / 3 ** 0.5:
            count += 1

print(count)

'И через модуль math'

n = 0

for x in range(100):
    for y in range(100):
        if x > 0 and y < tan(-pi / 6) * x + 10 and y > tan(pi / 6) * x:
            n += 1
print(n)
