import numpy as np


def find_primes(n):
    A = np.ones(n + 1, dtype="int32")
    i = 2
    while i <= n ** 0.5:
        if A[i] == 1:
            j = i ** 2
            while j <= n:
                A[j] = 0
                j += i
        i += 1
    return np.where(A == 1)[0][2:]


n = 20
primes = find_primes(n)
m = 1
for prime in primes:
    power = int(np.log(n) // np.log(prime))
    m *= prime ** power

print(m)
