mem = {}


def recursive_chain(x):
    if x == 1:
        return 1
    if x in mem:
        return mem[x]
    if x % 2 == 0:
        mem[x] = 1 + recursive_chain(x // 2)
    else:
        mem[x] = 1 + recursive_chain(3 * x + 1)
    return mem[x]


m = (0, None)
for i in range(1, int(1e6)):
    c = recursive_chain(i)
    if c > m[0]:
        m = (c, i)

print(m[1])
