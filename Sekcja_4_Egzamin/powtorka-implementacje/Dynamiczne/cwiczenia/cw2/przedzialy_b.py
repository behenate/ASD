from math import inf


def range_possible(A, P, a, b):
    A = sorted(A)
    print(A)
    n = len(A)
    m = A[-1][-1]
    F = [[inf for _ in range(m + 1)] for _ in range(m + 1)]
    for i, ra in enumerate(A):
        F[ra[0]][ra[1]] = P[i]
    for i in range(m + 1):
        for j in range(m + 1):
            for k in range(i, j):
                F[i][j] = min(F[i][j], F[i][k] + F[k][j])
    for line in F:
        print(line)
    print(F[a][b])


A = [(1, 5), (1, 13), (2, 5), (4, 9), (5, 7), (7, 10), (9, 12), (10, 13)]
P = [1, 100, 2, 3, 2, 3, 4, 5]
range_possible(A, P, 1, 13)
