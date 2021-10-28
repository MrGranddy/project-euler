mem = {}


def fact(x):
    if x == 1:
        return 1
    if x in mem:
        return mem[x]
    mem[x] = fact(x - 1) * x
    return mem[x]


n = 100
print(sum(map(int, str(fact(n)))))
