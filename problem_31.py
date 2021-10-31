possible_moves = [1, 2, 5, 10, 20, 50, 100, 200][::-1]

mem = {}


def count_moves(x, moves):
    if x == 0:
        return 1
    if (x, moves[0]) in mem:
        return mem[(x, moves[0])]
    s = 0
    for idx, move in enumerate(moves):
        if x >= move:
            s += count_moves(x - move, moves[idx:])
    mem[(x, moves[0])] = s
    return mem[(x, moves[0])]


print(count_moves(200, possible_moves))
