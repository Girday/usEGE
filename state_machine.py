VOWELS = set('EYUIOA')


def solve(s: str) -> int:
    state = 0  # 0 - initial, 1 - sha budut glasnye
    saved_digit = -1
    length = 0
    max_length = 0
    for c in s:
        if state == 0:
            if c.isdigit() and int(c) % 2 == 1:
                state = 1
                saved_digit = int(c)
        elif state == 1:
            if c in VOWELS:
                length += 1
            elif c.isdigit() and int(c) == saved_digit:
                max_length = max(max_length, length)
                length = 0
                saved_digit = -1
                state = 0
            else:
                length = 0
                saved_digit = -1
                state = 0
    return max_length


# print(solve("GHGGFKLJEOI7IOEUOEIYOU75ABCDFE"))

with open('24.txt') as f:
    print(solve(f.read()))
