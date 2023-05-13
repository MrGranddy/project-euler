import numpy as np

# For this problem we will use the fact that there are only 11 such primes.
# So we will just increase the maximum number 

def find_primes(n):
    """Algorithm for the sieve of Eratosthenes

    Args:
        n (int): An arbitrary number (n)

    Returns:
        np.ndarray: Prime numbers smaller than n
    """

    A = np.ones((n + 1,), dtype=bool)

    for i in range(2, int(np.sqrt(n)) + 1):
        if A[i]:
            j = i ** 2
            while j <= n:
                A[j] = False
                j = j + i

    return np.where(A)[0][2:] # discard 0 and 1

def get_truncations(x):

    num_digits = int(np.log10(x)) + 1
    
    truncations = []

    for i in range(num_digits - 1):

        truncations.append( x % (10 ** (i + 1)) )
        truncations.append( x // (10 ** (i + 1)) )

    return truncations

primes = set(find_primes(10 ** 6))
solutions = []

for prime in primes:

    truncations = get_truncations(prime)
    is_truncatable = True

    for truncation in truncations:
        if truncation not in primes:
            is_truncatable = False
            break

    if is_truncatable:
        solutions.append(prime)

print(f"Solution: {sum(p for p in solutions if p > 10)}")