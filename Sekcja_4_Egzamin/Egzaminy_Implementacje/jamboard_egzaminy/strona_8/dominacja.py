
def dominate_set(P):
    n = len(P)
    idx_x = [i for i in range(n)]
    idx_x = sorted(idx_x, key=lambda x: P[x][0])
    idx_y = range(n)
    idx_y = sorted(idx_y, key=lambda y: P[y][1])
    idx_xa = [0 for _ in range(n)]
    idx_ya = [0 for _ in range(n)]
    for i in range(n):
        idx_xa[idx_x[i]] = i
        idx_ya[idx_y[i]] = i
    px = sorted(P, key=lambda x:x[0])
    to_dominate = n
    dominated = [False for _ in range(n)]
    while to_dominate > 0:
        dominator = px[-1]
        if dominated[idx_x[len(px)-1]]:
            break
        px.pop()
        mx = len(px)-1
        while dominator[0] == px[mx] and mx > 0:
            mx -= 1
        idx_in_unsorted = idx_x[mx]
        idx_in_sorty = idx_ya[idx_in_unsorted]
        for i in range(idx_in_sorty):
            idx_in_unsorted = idx_y[i]
            dominated[idx_in_unsorted] = 1
        print(dominator)
    pass


P = [
    [6, 4],
    [1, 1],
    [1, 2],
    [3, 2],
    [2, 5],
    [5, 1],
    [5, 3]

]
dominate_set(P)