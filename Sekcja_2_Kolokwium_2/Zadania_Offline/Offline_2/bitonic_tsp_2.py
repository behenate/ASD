from math import *


def euclidean_tsp(C):
    C = sorted(C, key=lambda x: x[1])
    print(C)
    n = len(C)
    D = [[0 for _ in range(n)] for _ in range(n)]
    F = [[inf for _ in range(n)] for _ in range(n)]
    G = [[-1 for _ in range(n)] for _ in range(n)]
    F[n - 2][n - 1] = D[n - 2][n - 1]
    G[n - 2][n - 1] = n - 1
    for i in range(n - 3, -1, -1):
        low = inf
        low_k = -1
        for k in range(i + 1, n):
            if F[i + 1][k] + D[i][k] < low:
                low = F
                low_k = k
        F[i][i + 1] = low
        G[i][i + 1] = low_k
        for j in range(i + 1, n):
            F[i][j] = F[i + 1][j] + D[i][i + 1]
            G[i][j] = i + 1
    F[0][0] = F[0][1] + D[0][1]
    for i in range(n):
        for j in range(i, n):
            D[i][j] = dist((C[i][1], C[i][2]), (C[j][1], C[j][2]))
    F[0][1] = D[0][1]
    G[0][0] = 1
    for line in G:
        print(line)
    print_path(G, 0, 0, C, n)


def print_path(G, i, j, C, n):
    if n == 0:
        return
    if i <= j:
        k = G[i][j]
        print(k)
        print(C[k][0])
        print_path(G, k, j, C, n - 1)
    else:
        k = G[j][i]
        print_path(G, i, k, C, n - 1)
        print(C[k][0])
C8 = [['s', 9, 24], ['e', 11, 2], ['y', -5, 26], ['a', 28, -17], ['i', 23, 11], ['W', -24, -24], ['h', 29, 24],
     ['*', -25, 27], ['U', 22, -16], ['b', 5, 2], ['j', 15, -25], ['s', 24, -10], ['i', -9, 9], ['k', 18, 4],
     ['e', -19, 10], ['t', 16, -3], ['W', 30, 10], ['c', 26, 11], ['s', -20, -17], ['z', -17, 27]]
euclidean_tsp(C8)