fact_mem = {}

def fact(x):
    if x == 0:
        return 1
    if x in fact_mem:
        return fact_mem[x]
    fact_mem[x] = fact(x - 1) * x
    return fact_mem[x]


def find(n, digits, acc):

    if len(digits) == 0:
        return acc[::-1]

    d = n // fact(len(digits) - 1)
    return find(
        n - d * fact(len(digits) - 1), digits[:d] + digits[d + 1 :], [digits[d]] + acc
    )

n = int(1e6)
num_d = 10
digits = [i for i in range(num_d)]

print("".join(str(x) for x in find(n-1, digits, [])))
