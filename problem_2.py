x = (1, 1)
s = 0

while x[1] < 4e6:
    if x[1] % 2 == 0:
        s += x[1]
    x = ( x[1], x[0] + x[1] )

print(s)