mem = {}

def fact(x):
    if x == 1:
        return 1
    if x in mem:
        return mem[x]
    mem[x] = x * fact(x-1)
    return mem[x]

h, w = (20, 20)

print( fact(h+w) // (fact(h) * fact(w)) )