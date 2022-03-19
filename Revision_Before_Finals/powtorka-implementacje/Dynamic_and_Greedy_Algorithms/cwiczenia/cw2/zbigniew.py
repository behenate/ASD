from math import inf
A = [5, 0, 0, 3, 0, 0, 0, 0, 1, 0]

def zbigniew(A):
    n = len(A)
    m = 0
    for i in range(n):
        m += A[i]
    F = [[inf for _ in range(m + 1)] for _ in range(n)]
    for i in range(1, A[0]):
        F[i][A[0]-i+A[i]] = 1
    F[0][A[0]] = 0
    for i in range(1,n):
        for j in range(m+1):
            for k in range(1, i):
                if m >= j+k-A[i] > 0:
                    F[i][j] = min(F[i][j], F[i-k][j+k-A[i]] + 1)
    for line in F:
        print(line)

zbigniew(A)