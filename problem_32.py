from itertools import permutations

perms = permutations([i for i in range(1, 10)])

s = set()
for perm in perms:
    perm = "".join(map(str, perm))
    
    a, b, c = int(perm[:3]), int(perm[3:5]), int(perm[5:])
    if a * b == c:
        s.add(c)
    a, b, c = int(perm[:4]), int(perm[4:5]), int(perm[5:])
    if a * b == c:
        s.add(c)

print(sum(s))
    