from math import ceil

luggage = [1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, ]


def pack(luggage):
    n = len(luggage)
    w = sum(luggage) / 2
    if w % 1 != 0:
        return False
    w = int(w)
    F = [[0 for _ in range(w + 1)] for _ in range(n)]
    F[0][luggage[0]] = 1
    parent = [[None for _ in range(w + 1)] for _ in range(n)]
    for i in range(n):
        for j in range(w + 1):
            if j == luggage[i]:
                F[i][j] = 1
                continue
            if F[i - 1][j]:
                F[i][j] = F[i - 1][j]
                parent[i][j] = (i - 1, j, 0)
                continue
            if j - luggage[i] >= 0 and F[i - 1][j - luggage[i]]:
                F[i][j] = F[i - 1][j - luggage[i]]
                parent[i][j] = (i - 1, j - luggage[i], 1)
    for line in parent:
        print(line)
    for line in F:
        print(line)

    i = n - 1
    j = w


    while parent[i][j] is not None:
        p = parent[i][j]
        if p[2]:
            print(p[0] + 1)
        i = p[0]
        j = p[1]
    print(i)


pack(luggage)
