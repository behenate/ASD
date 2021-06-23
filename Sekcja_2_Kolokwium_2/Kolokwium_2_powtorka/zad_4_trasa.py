from math import inf
C = [[5, 4, 1, 0, 4], [3, 2, 1, 3, 2], [1, 2, 4, 5, 2], [5, 3, 2, 1, 4], [4, 1, 3, 2, 3]]
def find_path(C):
    n = len(C)
    m = len(C[0])
    F = [[inf for _ in range(m)] for _ in range(n)]
    F[0][0] = C[0][0]
    for i in range(1,n):
        F[i][0] = F[i - 1][0] + C[i][0]

    for i in range(1,m):
        F[0][i] = F[0][i-1] + C[0][i]
    for i in range(1,n):
        for j in range(1,m):
            F[i][j] = min(F[i-1][j], F[i][j-1]) + C[i][j]
    i = n-1
    j = m-1
    path = []
    path.append((i,j))
    while i != 0 or j != 0:
        if F[i][j] == F[i-1][j] + C[i][j]:
            path.append((i-1,j))
            i -= 1
        else:
            path.append((i, j-1))
            j -= 1
    for line in F:
        print(line)
    print(path)

find_path(C)