from math import inf


def always_refuel(p, s, l, target):
    n = len(s)
    F = [inf] * n
    F[0] = p[0] * s[0]
    lowest = inf
    for i in range(1, n):
        l_i = -1
        for k in range(i):
            dist = s[i] - s[k]
            if dist <= l:
                F[i] = min(F[k] + p[i] * dist, F[i])
        if target - s[i] < l:
            lowest = min(lowest, F[i])
    print(lowest)


p = [1, 2, 3, 4, 5, 6, 7]
s = [3, 6, 7, 9, 12, 13, 15]
always_refuel(p, s, 5, 15)
