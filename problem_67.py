class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None


with open("problem_67.txt", "r") as f:
    pyramid = f.read()
pyramid = [
    [int(x) for x in line.strip().split()] for line in pyramid.strip().splitlines()
]

for i in range(1, len(pyramid)):

    pyramid[i][0] += pyramid[i - 1][0]
    pyramid[i][-1] += pyramid[i - 1][-1]

    for j in range(1, len(pyramid[i]) - 1):

        l = pyramid[i - 1][j - 1]
        r = pyramid[i - 1][j]

        pyramid[i][j] += max([l, r])

print(max(pyramid[-1]))
