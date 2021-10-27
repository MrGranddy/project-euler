def factors(n):
    p = 2
    factors = {}

    while n >= p * p:
        if n % p == 0:
            n = n // p
            if p in factors:
                factors[p] += 1
            else:
                factors[p] = 1
        else:
            p = p + 1

    if n > 1:
        if n in factors:
            factors[n] += 1
        else:
            factors[n] = 1

    return factors


n = 1
lim = 500
while 1:
    t = n * (n + 1) // 2
    f = factors(t)
    m = 1
    for _, val in f.items():
        m *= val + 1

    if m > lim:
        print(t)
        break

    n += 1
