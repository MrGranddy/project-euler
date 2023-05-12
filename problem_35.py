import numpy as np

# Let's implement Sieve of Eratostheses to find all the prime numbers
# smaller than 1 million!

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

primes = find_primes(10 ** 6)
prime_dict = {p: True for p in primes}
circulars = []

for prime in prime_dict:

    if not prime_dict[prime]:
        continue
    
    num_digits = int(np.log10(prime)) + 1 # Integer logarithms will not occur since 10^k not prime

    curr = prime
    circles = [curr]

    for i in range(num_digits - 1):
        first_digit = curr // (10 ** (num_digits - 1))
        rest = curr % (10 ** (num_digits - 1))
        curr = rest * 10 + first_digit

        if curr in primes:
            circles.append(curr)

    if len(circles) == num_digits:
        for circle in circles:
            prime_dict[circle] = False
            circulars += circles

circulars = set(circulars)

print(f"Number of circular primes: {len(circulars)}")