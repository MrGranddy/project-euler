n = 600851475143
p = 2
factors = set()

while n >= p * p:
    if n % p == 0:
        n = n // p
        factors.add(p)
    else:
        p = p + 1

factors.add(n)
print(max(factors))