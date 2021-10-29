with open("problem_22.txt", "r") as f:
    names = f.read().strip()
    names = [name[1:-1] for name in names.split(",")]

names = sorted(names)


def chr2val(x):
    return ord(x) - 64


scores = [sum(chr2val(x) * (idx + 1) for x in name) for idx, name in enumerate(names)]

print(sum(scores))
