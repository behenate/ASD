from math import ceil

luggage = [1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1]


def pack(luggage):
    n = len(luggage)
    w = sum(luggage) / 2
    if w % 1 != 0:
        return False
    w = int(w)
    F = [[0 for _ in range(w + 1)] for _ in range(n)]
    F[0][luggage[0]] = 1
    for i in range(n):
        for j in range(w + 1):
            if j == luggage[i]:
                F[i][j] = 1
                continue
            if F[i - 1][j]:
                F[i][j] = F[i - 1][j]
                continue
            if j - luggage[i] >= 0 and F[i - 1][j - luggage[i]]:
                F[i][j] = F[i - 1][j - luggage[i]]

    i = n - 1
    j = w
    for line in F:
        print(line)
    while i > 0:
        if F[i-1][j] == 1:
            i = i-1
        elif F[i-1][j-luggage[i]] == 1:
            print(i)
            j = j - luggage[i]
            i = i-1
        else:
            break


pack(luggage)
