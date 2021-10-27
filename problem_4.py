def check_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return check_palindrome(s[1:-1])
    else:
        return False

n1 = 999
n2 = 999
c = 0

palindromes = set()

for n1 in range(999, 99, -1):
    for n2 in range(999, 99, -1):
        n = n1 * n2
        if check_palindrome(str(n)):
            palindromes.add(n)

print(max(palindromes))    