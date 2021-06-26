def palindrom(t):
    n = len(t)
    F = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        if t[i-1] == t[i]:
            F[i-1][i] = 1
    for i in range(n):
        F[i][i] = 1
    max_len = 0
    for j1 in range(2,n):
        for i in range(n-j1):
            j = i + j1

            F[i][j] = int(bool(F[i+1][j-1]) and t[i] == t[j])
            if F[i][j]:
                max_len = max(max_len,j-i+1)
    for line in F:
        print(line)
    print(max_len)


palindrom("sfaabaadds")