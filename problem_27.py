import numpy as np

a_abs_lim = 1000
b_abs_lim = 1001

max_possible = int(1e6)


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


primes = set(find_primes(max_possible))
max_seq = 0
max_ab = None


for a in range(-a_abs_lim, a_abs_lim + 1):
    for b in range(-b_abs_lim, b_abs_lim + 1):

        n = 0
        while 1:
            v = n ** 2 + a * n + b
            if v not in primes:
                break
            n += 1

        if n > max_seq:
            max_seq = n
            max_ab = (a, b)

print(max_ab[0] * max_ab[1])
