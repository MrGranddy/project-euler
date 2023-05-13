from functools import cache, reduce
import itertools

@cache
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)

# Find maximum number of digits for this to be possible
num_digit = 2
max_num = 99
print("This is possible for numbers with #digits:", end=" ")
while True:
    if max_num <= num_digit * fact(9):
        print(num_digit, end=" ")
    else:
        break
    num_digit +=1
    max_num = max_num * 10 + 9
print()

# Solve the problem

# Create all possible numbers as digits,
# because going other way around might be less efficient
digits = [list(range(10))] * 6
numbers = list(itertools.product(*digits))

# List of curious numbers found
solutions = []

for number in numbers:

    # Remove leading zeros
    curr = number
    while len(curr) and curr[0] == 0:
        curr = curr[1:]

    # These do not count
    if len(curr) < 2:
        continue
    
    # Convert list of digits into the number
    numeric = reduce(lambda acc, d: acc * 10 + d, curr, 0)

    # Check condition
    if sum([fact(d) for d in curr]) == numeric:
        solutions.append(numeric)

print(f"Solution: {sum(solutions)}")