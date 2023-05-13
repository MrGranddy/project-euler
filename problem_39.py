max_p = 1000

perimeter_count = {p: 0 for p in range(4, max_p+1)}

for p in range(4, max_p+1):
    for a in range(1, p//2):
            
        b = (p ** 2 - 2 * a * p) / (2 * (p - a))

        if b % 1 == 0:
            perimeter_count[p] += 1

print(f"Solution: {max(perimeter_count, key=lambda x: perimeter_count[x])}")