from math import inf, log2


def bellman_ford(G, s, t):
    n = len(G)
    dist = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    dist[s] = 0
    for _ in range(n - 1):
        for i in range(n):
            vertex = G[i]
            for tup in vertex:
                neigh, d = tup
                d = log2(d)
                if dist[i] + d < dist[neigh]:
                    dist[neigh] = dist[i] + d
                    parent[neigh] = i

    for i in range(n):
        vertex = G[i]
        for tup in vertex:
            neigh, d = tup
            d = log2(d)
            if dist[neigh] > dist[i] + d:
                print("Ujemny cykl!")
                return False

    w = t
    path = []
    while w != s:
        path.append(w)
        if parent[w] is not None:
            w = parent[w]
        else:
            w = s
    path.append(w)
    path.reverse()
    print(path)
    print(dist[t])
    print(parent)


_G = [
    [[1, 5], [2, 2]],
    [[3, 1]],
    [[1, 1], [4, 2]],
    [[5, 3], [4, 1]],
    [[5, 2], [2, 0.5]],
    []
]
bellman_ford(_G, 0, 5)
