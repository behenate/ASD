import numpy as np
def dist(P, i, j):
    return np.sqrt((P[i][1] - P[j][1]) ** 2 + (P[i][2] - P[j][2]) ** 2)


def BTSP(P):
    P = sorted(P, key=lambda x: x[1])
    n = len(P)
    D = np.ones((n, n)) * np.inf
    path = np.ones((n, n), dtype=int) * (-1)
    D[n - 2, n - 1] = dist(P, n - 2, n - 1)
    path[n - 2, n - 1] = n - 1
    for i in range(n - 3, -1, -1):
        m = np.inf
        for k in range(i + 2, n):
            if m > D[i + 1, k] + dist(P, i, k):
                m, mk = D[i + 1, k] + dist(P, i, k), k
        D[i, i + 1] = m
        path[i, i + 1] = mk
        for j in range(i + 2, n):
            D[i, j] = D[i + 1, j] + dist(P, i, i + 1)
            path[i, j] = i + 1
    D[0, 0] = D[0, 1] + dist(P, 0, 1)
    path[0, 0] = 1
    for line in path:
        print(line)
    r = (get_tsp_path(path,1, 2, n))
    for elem in r:
        print(P[elem][0], end="")
    return D, path


def get_tsp_path(path, i, j, n):
    if n < 0:
        return []
    if i <= j:
        k = path[i, j]
        return [k] + get_tsp_path(path, k, j, n - 1)
    else:
        k = path[j, i]
        return get_tsp_path(path, i, k, n - 1) + [k]
C8 = [['s', 9, 24], ['e', 11, 2], ['y', -5, 26], ['a', 28, -17], ['i', 23, 11], ['W', -24, -24], ['h', 29, 24],
     ['*', -25, 27], ['U', 22, -16], ['b', 5, 2], ['j', 15, -25], ['s', 24, -10], ['i', -9, 9], ['k', 18, 4],
     ['e', -19, 10], ['t', 16, -3], ['W', 30, 10], ['c', 26, 11], ['s', -20, -17], ['z', -17, 27]]

BTSP(C8)