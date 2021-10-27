def find(s):
    for a in range(s + 1):
        for b in range(a+1, s - a + 1):
            for c in range(b+1, s - a - b + 1):
                if( a+b+c == 1000 and a ** 2 + b ** 2 == c ** 2 ):
                    return a*b*c

print(find(1000))

