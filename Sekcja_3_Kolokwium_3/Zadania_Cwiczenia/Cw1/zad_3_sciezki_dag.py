from math import inf


def top_sort(G):
    def DFS_visit(G, i):
        visited[i] = True
        for neigh in G[i]:
            if not visited[neigh]:
                parent[neigh] = i
                DFS_visit(G, neigh)
        top_order.append(i)

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    top_order = []

    for i in range(n):
        if not visited[i]:
            DFS_visit(G, i)
    top_order.reverse()
    return visited, parent, top_order


def find_shortest(G, weight):
    n = len(G)
    sorted = top_sort(G)[2]
    dist = [inf for _ in range(n)]
    dist[sorted[0]] = 0

    for i in range(n-1):
        for j in range(len(G[sorted[i]])):
            neigh = G[sorted[i]][j]
            dist[neigh] = min(dist[neigh], dist[sorted[i]] + weight[sorted[i]][j])
    print(dist)


_G = [
    [1],
    [2],
    [3, 4],
    [4, ],
    [5, 6],
    [],
    [7],
    [5]
]

_weight = [
    [1],
    [2],
    [1, 4],
    [1],
    [2, 1],
    [],
    [1],
    [1],
]
find_shortest(_G, _weight)
