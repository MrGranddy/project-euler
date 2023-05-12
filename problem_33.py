from functools import cache

@cache
def gcd(a, b):
    if b:
        return gcd(b, a % b)
    return a

N1 = 1
N2 = 1

for a in range(1, 10):
    for b in range(a+1, 10):
        for c in range(1, 10):

            if (9 * a + b) * c == 10 * a * b:

                n1 = 10 * a + b
                n2 = 10 * b + c

                numer = n1//gcd(n1, n2)
                denum = n2//gcd(n1, n2)

                #print( f"{n1}/{n2} = {numer}/{denum}" )

                N1 *= numer
                N2 *= denum

print(f"{N1//gcd(N1, N2)}/{N2//gcd(N1, N2)}")