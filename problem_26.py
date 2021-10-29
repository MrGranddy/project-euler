import math

lim_d = 1000

max_rep = 0
max_d = None

for d in range(2, lim_d):

    n = 1
    digits = [0]
    pairs = {}
    idx = None

    while n != 0:

        if n in pairs:
            idx = pairs[n]
            break

        org_n = n
        n *= 10
        while n < d:
            n *= 10
            digits.append(0)
        digits.append(n // d)
        n = n % d
        pairs[org_n] = len(digits) - 1

    l = len(digits[idx:])
    if l > max_rep:
        max_rep = l
        max_d = d

print(max_d)
