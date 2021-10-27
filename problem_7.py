import numpy as np


def find_nth_prime(idx):
    n = 999999
    A = np.ones(n + 1, dtype="int32")
    i = 2
    cnt = 0
    while i <= n ** 0.5:
        if A[i] == 1:
            j = i ** 2
            while j <= n:
                A[j] = 0
                j += i
            cnt += 1
        if cnt == idx:
            break
        i += 1
    return np.where(A == 1)[0][1 + idx]


print(find_nth_prime(10001))
