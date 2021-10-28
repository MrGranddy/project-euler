def sum_of_proper_primes(x):
    i = 2
    s = 0

    while i <= x ** 0.5:

        if x % i == 0:
            if i == x // i:
                s += i
            else:
                s += i + x // i

        i += 1

    return s + 1


mem = {}

for i in range(1, 10000):
    if i not in mem:
        x = sum_of_proper_primes(i)
        y = sum_of_proper_primes(x)

        if i == y and i != x:
            mem[i] = x
            mem[x] = y


print(sum(mem.keys()))
