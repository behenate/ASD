from math import inf
class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    # Próba połączenia dwóch elementów z tego samego zbioru
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal_hub(G, num_v):
    G = sorted(G, key=lambda x: x[2])
    res = inf
    r_i = 0
    for i in range(num_v):
        r = kruskal(G, i, num_v)
        if r < res:
            res = r
            r_i = i
    print(res)


def kruskal(G, start, num_v):
    n = len(G)
    A = [Node(i) for i in range(num_v)]
    solved = [0 for _ in range(num_v)]
    mn = None
    mx = None
    for i in range(start, n):
        x = G[i][0]
        y = G[i][1]
        val = G[i][2]
        if mn is None:
            mn = val
        if find(A[y]) != find(A[x]):
            mx = val
            solved[x] = 1
            solved[y] = 1
            union(A[x], A[y])

    for i in range(num_v):
        if not solved[i]:
            return inf
    return mx-mn


A = [(10, 10), (15, 25), (20, 20), (30, 40)]
# G = [
#     (0, 5, 1),
#     (0, 2, 4),
#     (0, 1, 12),
#     (0, 4, 8),
#     (5, 4, 7),
#     (4, 3, 2),
#     (3, 2, 5),
#     (4, 1, 3),
#     (1, 2, 6)
# ]
G = [
    (0,1,5),
    (0,2,1),
    (0,3,8),
    (0,4,10),
    (1,0,5),
    (1,2,2),
    (1,3,4),
    (1,4,11),
    (2,0,4),
    (2,1,2),
    (2,3,6),
    (2,4,9),
    (3,0,8),
    (3,1,4),
    (3,2,6),
    (3,4,7),
    (4,0,10),
    (4,1,11),
    (4,2,9),
    (4,3,7)
]
kruskal_hub(G, 5)