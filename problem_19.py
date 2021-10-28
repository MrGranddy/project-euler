# probably can be solved with python datetime real easily but yet
# here we are again

start_date = (1, 1, 1901)
end_date = (31, 12, 2000)


def month_days(x, y):
    leap_year = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
    if x == 12 and leap_year:
        return 29
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][x]


days = 0
cnt = 0

while start_date != (1, 1, 2001):

    days += month_days(start_date[1] - 1, start_date[2])
    start_date = (1, start_date[1] + 1, start_date[2])
    if start_date[1] == 13:
        start_date = (1, 1, start_date[2] + 1)

    days = days % 7
    if days == 0:
        cnt += 1

print(cnt)
