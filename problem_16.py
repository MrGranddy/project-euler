# python can handle 2 ** 1000 but let's assume it can not

exp = 1000

n = [1]

for i in range(exp):

    new_n = []

    r = 0
    for j in range(len(n)):
        s = 2 * n[-1 - j] + r
        r = s // 10
        new_n.append(s % 10)

    if r > 0:
        n = [int(x) for x in str(r)] + new_n[::-1]
    else:
        n = new_n[::-1]

print(sum(n))
