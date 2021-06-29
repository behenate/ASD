from math import inf
ranges = [
    [0, 4],
    [2, 5],
    [6, 12],
    [7, 9],
    [10, 12],
    [8, 14],
    [18, 23]
]


def pick_plan(A,t):
    n = len(A)
    A = sorted(A, key=lambda x: x[1])
    print(A)
    F = [[inf for _ in range(t)] for _ in range(n)]
    for i in range(n):
        F[i][0] = 0

    for j in range(1, t):
        for i in range(n):
            for k in range(i):
                print(i,k)
                d = A[i][0] - A[k][1]
                if d >=0 and i-k >=0 and j-1 >= 0:
                    F[i][j] = min(F[k][j-1] + d, F[i][j])
    for line in F:
        print(line)


pick_plan(ranges, 3)


