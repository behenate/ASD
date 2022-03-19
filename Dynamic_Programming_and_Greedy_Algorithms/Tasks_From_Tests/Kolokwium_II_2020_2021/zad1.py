from zad1testy import runtests


def prev(T, build):
    for j in range(build, -1, -1):
        if T[j][2] < T[build][1]:
            return j
    return -1


def select_buildings(T, p):
    def price(building):
        return T[building][3]

    def a(building):
        return T[building][1]

    def b(building):
        return T[building][2]

    def height(building):
        return T[building][0]

    def capacity(building):
        return (b(building) - a(building)) * height(building)

    n = len(T)
    before_sort = sorted(range(n), key=lambda k: T[k][2])
    T = sorted(T, key=lambda x: x[2])

    F = [[0 for _ in range(p + 1)] for _ in range(n)]
    for i in range(p + 1):
        if price(0) < i:
            F[0][i] = capacity(0)

    for i in range(1, n):
        for j in range(1, p + 1):
            F[i][j] = F[i - 1][j]
            if prev(T, i) != -1 and j - price(i) > 0:
                F[i][j] = max(F[i][j], F[prev(T, i)][j - price(i)] + capacity(i))

    def get_res(i, j, last_built):
        if j == 0:
            return
        if i == 0 and j > price(0) and (b(0) < a(last_built) or last_built == -1):
            return [0]
        elif i == 0:
            return []
        if j - price(i) > 0 and F[i - 1][j - price(i)] + capacity(i) == F[i][j]:
            return get_res(i - 1, j - price(i), i) + [i]
        else:
            return get_res(i - 1, j, last_built)

    r = get_res(n - 1, p, -1)
    for i in range(len(r)):
        r[i] = before_sort[r[i]]
    return sorted(r)

T = [
    [2, 1, 5, 3],
    [3, 7, 9, 2],
    [100, 10, 11, 1],
]
select_buildings(T, 100)
runtests( select_buildings )
