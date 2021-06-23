from math import inf
def zbigniew(A):
    n = len(A)
    m = 0
    for i in range(n):
        m += A[i]
    F = [[inf for _ in range(m)] for _ in range(n)]
    F[0][A[0]] = 0
    for i in range(1, n):
        for j in range(m):
            for k in range(1, i+1):
                if 0 <= j+k-A[i] < m:
                    F[i][j] = min(F[i][j], F[i-k][j+k-A[i]] + 1)
    for line in F:
        print(line)
    print(min(F[n-1]))


A = [4,1,1,1,1]
zbigniew(A)
