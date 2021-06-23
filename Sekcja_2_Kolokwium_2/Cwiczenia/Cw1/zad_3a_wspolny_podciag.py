def longest_common_subsequence(a,b):
    n = len(a)
    F = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        if a[0] == b[i]:
            F[0][i] = 1
            for j in range(i, n):
                F[0][j] = 1
            break
    for i in range(1, n):
        if a[i] == b[0]:
            F[i][0] = 1
            for j in range(i+1, n):
                F[j][0] = 1
            break
    for line in F:
        print(line)
    for i in range(1, n):
        for j in range(1, n):
            F[i][j] = max(F[i][j-1], F[i-1][j])
            if a[i] == b[j]:
                F[i][j] = max(F[i][j], F[i-1][j-1] + 1)

    for line in F:
        print(line)


a = [7, 8, 2, 3, 4]
b = [2, 3, 5, 6, 7]

longest_common_subsequence(a,b)