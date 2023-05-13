import itertools
from functools import reduce
import numpy as np

def digits_to_number(digits):
    return reduce(lambda acc, d: acc * 10 + d, digits, 0)

permutations = itertools.permutations(range(9, 0, -1)) # All 9 digit permutations starting from the largest

for permutation in permutations:

    first_num_digits = 2

    while first_num_digits < 5:

        multiples = [ str(digits_to_number(permutation[:first_num_digits]) * (it+1)) for it in range(9 // first_num_digits) ]
        trial_num = int("".join(multiples))
        num = digits_to_number(permutation)

        if num == trial_num:
            print(f"Solution: {num}")
            exit()

        first_num_digits += 1