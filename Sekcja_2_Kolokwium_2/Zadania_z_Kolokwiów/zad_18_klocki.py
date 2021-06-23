from math import inf


def tower(A):
    n = len(A)
    F = [1 for _ in range(n)]
    for i in range(1, n):
        for k in range(i):
            if A[k][0] <= A[i][0] and A[k][1] >= A[i][1]:
                F[i] = max(F[i], F[k] + 1)
    print(F)


_A = [
    (1, 4),
    (0, 5),
    (1, 5),
    (2, 6),
    (2, 4)
]
tower(_A)
_A = [
    [10, 15],
    [8, 14],
    [1, 6],
    [3, 10],
    [8, 11],
    [6, 15]
]
tower(_A)
