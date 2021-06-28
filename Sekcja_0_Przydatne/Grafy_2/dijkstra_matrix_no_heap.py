from queue import Queue
from math import inf


def dijkstra(G, s):
    n = len(G)
    dist = [inf for _ in range(n)]
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[s] = 0
    for i in range(n):
        elem = -1
        min_dist = inf
        for j in range(n):
            if not visited[j] and dist[j] < min_dist:
                min_dist = dist[j]
                elem = j
        visited[elem] = True
        for j in range(n):
            if G[elem][j] > 0 and not visited[j] and dist[j] > dist[elem] + G[elem][j]:
                dist[j] = dist[elem] + G[elem][j]
                parent[j] = elem
    print(dist)
    print(parent)


_G = [
    [0, 3, 5, 0, 0, 0],
    [3, 0, 2, 5, 8, 0],
    [5, 2, 0, 0, 1, 0],
    [0, 5, 0, 0, 1, 2],
    [0, 8, 1, 1, 0, 6],
    [0, 0, 0, 2, 6, 0]
]

dijkstra(_G, 0)
