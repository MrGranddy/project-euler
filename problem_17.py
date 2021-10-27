# with all respect I think this problem makes no sense at all

start = 1
end = 999

c = {
    1: 3, 2: 3, 3: 5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,
    11:6, 12:6, 13:8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19:8,
    20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90:6, 100: 7,
    1000: 11
}

s = 0

for i in range(start, end+1):

    n = i

    if n > 99:
        first_digit = n // 100
        n = n % 100
        if n != 0:
            s += 3
        s += c[first_digit]
        s += c[100]

    if n > 9:
        if n in c:
            s += c[n]
            n = 0
        else:
            tens = n // 10
            s += c[tens * 10]
            n = n % 10

    if n > 0:
        s += c[n]


s += c[1000]


print(s)