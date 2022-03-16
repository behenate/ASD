# Zakładając strukturę grafu jak poniżej
skoki = [[1, 2, 3, 4], [3], [3, 4], [4], []]


def longest_path(jumps):
    n = len(jumps)
    F = [0] * n
    for i in range(n):
        path_recur(i, jumps, F)
    return max(F)


def path_recur(index, jumps, F):
    if len(jumps[index]) == 0:
        return 1
    if F[index] != 0:
        return F[index]
    F[index] = 1

    for jump in jumps[index]:
        F[index] = max(F[index], path_recur(jump, jumps, F)+1)
    return F[index]
print(longest_path(skoki))