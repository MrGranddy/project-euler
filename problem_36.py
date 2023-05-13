def is_palindrome(s):
    curr = s
    while len(curr) > 1:
        if curr[0] != curr[-1]:
            return False
        curr = curr[1:-1]
    return True

N = 10 ** 6
solution = 0

for n in range(N):

    base10 = str(n)
    base2 = format(n, 'b')

    if is_palindrome(base10) and is_palindrome(base2):
        solution += n

print(f"The solution is: {solution}")