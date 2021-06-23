from math import *
def euclidean_tsp(C):
    C = sorted(C, key=lambda x: x[1])
    print(C)
    n = len(C)
    D = [[0 for _ in range(n)] for _ in range(n)]
    F = [[inf for _ in range(n)] for _ in range(n)]
    G = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            D[i][j] = dist((C[i][1], C[i][2]), (C[j][1], C[j][2]))
    F[0][1] = D[0][1]
    for j in range(2, n):
        for i in range(j-1):
            F[i][j] = F[i][j-1] + D[j-1][j]
            G[i][j] = j-1
        F[j-1][j] = inf
        for k in range(j-1):
            best = F[k][j-1] + D[k][j]
            if best < F[j-1][j]:
                F[j-1][j] = best
                G[j-1][j] = k
    F[n-1][n-1] = F[n-2][n-1] + D[n-2][n-1]

    for line in F:
        print(line)
    for line in G:
        print(line)
    print_tour(C,G,n)
    print(F[n - 1][n - 1])

def print_tour(C, r, n):
    print (C[n-1][0])
    print(C[n-2][0])
    k = r[n-2][n-1]
    print_path_1(r,k,n-2, C)
    print(C[k][0])


def print_path_1(r,i,j,C):
    if i<j:
        k = r[i][j]
        if k != i:
            print(C[k][0])
        if k > 0:
            print_path_1(r,i,k,C)
    else:
        k = r[j][i]
        if k > 0:
            print_path_1(r,k,j,C)
            print(C[k][0])
C8 = [['s', 9, 24], ['e', 11, 2], ['y', -5, 26], ['a', 28, -17], ['i', 23, 11], ['W', -24, -24], ['h', 29, 24],
     ['*', -25, 27], ['U', 22, -16], ['b', 5, 2], ['j', 15, -25], ['s', 24, -10], ['i', -9, 9], ['k', 18, 4],
     ['e', -19, 10], ['t', 16, -3], ['W', 30, 10], ['c', 26, 11], ['s', -20, -17], ['z', -17, 27]]
euclidean_tsp(C8)