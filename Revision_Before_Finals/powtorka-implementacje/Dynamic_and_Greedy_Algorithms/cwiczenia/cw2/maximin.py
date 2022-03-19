def subset(A, s):
    n = len(A)
    F = [[0 for _ in range(s + 1)] for _ in range(n + 1)]
    S = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0, n):
        S[i][i] = A[i]
    for i in range(n):
        for j in range(i, n):
            S[i][j] = S[i][j-1] + A[j]
    for line in S:
        print(line)
    g_s = 0
    for i in range(1, n+1):
        g_s += A[i - 1]
        F[i][1] = g_s
    for i in range(n+1):
        for j in range(2, s+1):
            if i < j:
                continue
            for k in range(1, i-j+2):
                su = 0
                for l in range(i, i-k, -1):
                    su += A[l-1]
                su = S[i-k][i-1]
                F[i][j] = max(F[i][j], min(F[i-k][j-1],su ))
    for line in F:
        print(line)


A = [1, 1, 1, 2, 1, 3]
subset(A, 3)
