import numpy as np


def proper_primes(x):
    i = 2
    l = []

    while i <= x ** 0.5:

        if x % i == 0:
            l.append(i)
            if i != x // i:
                l.append(x // i)

        i += 1

    l.append(1)
    return l


abundants = []

for n in range(1, 28123 + 1):
    if sum(proper_primes(n)) > n:
        abundants.append(n)

two_factors = np.zeros((28123 + 1,), dtype="uint8")

for i in range(len(abundants)):
    for j in range(i + 1):

        s = abundants[i] + abundants[j]

        if s > 28123:
            break

        two_factors[s] = True

print(np.sum(np.where(two_factors == 0)[0][1:]))
