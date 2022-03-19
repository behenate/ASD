def range_possible(A, a, b):
    A = sorted(A)
    n = len(A)
    m = A[-1][-1]
    F = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
    for ra in A:
        F[ra[0]][ra[1]] = 1
    for i in range(m + 1):
        for j in range(m + 1):
            if F[i][j] == 0:
                for k in range(i, j):
                    F[i][j] = F[i][j] or (F[i][k] and F[k][j])
    for line in F:
        print(line)
    print(F[a][b])


A = [(1, 5), (2, 5), (4, 9), (5, 7), (7, 10), (9, 12), (10, 13)]

range_possible(A, 4,9)
