from math import inf
def opt_sum(T):
    n = len(T)
    sums = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        sums[i][i] = T[i]
    for i in range(n):
        for j in range(i, n):
            sums[i][j] = sums[i][j - 1] + T[j]
    for i in range(n):
        for j in range(i, n):
            sums[i][j] = abs(sums[i][j])
    F = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i] = 0
    for j1 in range(1, n):
        for i in range(n-j1):
            j = j1+i
            for k in range(i, j):
                print(i,j,k, F[i][k], F[k+1][j])
                F[i][j] = min(F[i][j], max(F[i][k], F[k+1][j]))
            if F[i][j] == inf:
                F[i][j] = sums[i][j]
            F[i][j] = max(F[i][j], sums[i][j])
    for line in F:
        print(line)
T = [1, -5, 2, -3]

opt_sum(T)