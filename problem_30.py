p = 5

ns = set()
for i in range(10, int(10 ** (p + 1))):

    s = sum(x ** p for x in map(int, str(i)))
    if s == i:
        ns.add(i)

print(sum(ns))
