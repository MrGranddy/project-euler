import math

mem = {}

def fibo(x):

    if x < 3:
        return 1
    if x in mem:
        return mem[x]

    mem[x] = fibo(x-1) + fibo(x-2)
    return mem[x]

d = 1000

for i in range(1, 10000):
    n = fibo(i)
    if math.log10(n) >= d - 1:
        print(i)
        break