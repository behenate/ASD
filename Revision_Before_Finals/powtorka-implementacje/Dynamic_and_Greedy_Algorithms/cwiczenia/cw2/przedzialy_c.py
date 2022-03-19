from math import inf
def range_possible(A,max_amt, a, b):
    A = sorted(A)
    print(A)
    n = len(A)
    m = A[-1][-1]
    max_len = 0
    F = [[inf for _ in range(m + 1)] for _ in range(m + 1)]
    for i, ra in enumerate(A):
        F[ra[0]][ra[1]] = 1
    for i in range(m + 1):
        for j in range(m + 1):
            for k in range(i, j):
                r = F[i][k] + F[k][j]
                if r <= max_amt:
                    max_len = max(j-i + 1 , max_len)
                    F[i][j] = min(F[i][j], r)
    for line in F:
        print(line)
    print(max_len)


A = [(1, 5), (1, 4), (2, 5), (4, 9), (5, 7), (7, 10), (9, 12), (10, 13)]
P = [1, 100, 2, 3, 2, 3, 4, 5]
range_possible(A, 3, 1, 13)
