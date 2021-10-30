s = set()

for a in range(2, 100 + 1):
    for b in range(2, 100 + 1):
        s.add(a ** b)

print(len(s))
