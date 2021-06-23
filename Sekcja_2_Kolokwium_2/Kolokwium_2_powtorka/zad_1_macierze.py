from math import inf


def optymalny_koszt(macierze):
    n = len(macierze)
    F = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i] = 0
    for h in range(1, n):
        for i in range(n - h):
            j = i + h
            for k in range(i, j):
                F[i][j] = min(F[i][k] + F[k + 1][j] + macierze[i][0] * macierze[k][1] * macierze[j][1], F[i][j])
    for line in F:
        print(line)


_macierze = [[30, 35], [35, 15], [15, 5], [5, 10], [10, 20], [20, 25]]
optymalny_koszt(_macierze)
