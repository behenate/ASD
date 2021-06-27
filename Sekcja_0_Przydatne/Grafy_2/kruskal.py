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


def kruskal(G, num_v):
    G = sorted(G, key=lambda x: x[2])
    n = len(G)
    A = [Node(i) for i in range(num_v)]
    for i in range(n):
        x = G[i][0]
        y = G[i][1]
        val = G[i][2]

        if find(A[y]) != find(A[x]):
            union(A[x], A[y])
            print("used", val)
    print(G)


G = [
    (0, 5, 1),
    (0, 2, 4),
    (0, 1, 12),
    (0, 4, 8),
    (5, 4, 7),
    (4, 3, 2),
    (3, 2, 5),
    (4, 1, 3),
    (1, 2, 6)
]
kruskal(G, 6)