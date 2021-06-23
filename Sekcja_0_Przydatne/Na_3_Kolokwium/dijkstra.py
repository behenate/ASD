from math import inf
from queue import PriorityQueue


def dijkstra(G, s):
    n = len(G)
    visited = [0 for _ in range(n)]
    dist = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[s] = 0
    queue = PriorityQueue()
    queue.put((0, s))
    while queue.qsize() > 0:
        dist_to, i = queue.get()
        if visited[i]:
            continue
        visited[i] = 1
        for e in G[i]:
            elem, d = e
            if visited[elem]:
                continue
            if dist_to + d < dist[elem]:
                dist[elem] = dist_to + d
                queue.put((dist[elem], elem))
                parent[elem] = i

    print(parent)
    print(dist)
_G = [
    [(1, 1), (2, 5)],
    [(0, 1), (2, 2), (4, 7)],
    [(0, 5), (1, 2), (3, 3)],
    [(1, 8), (2, 3), (4, 1)],
    [(1, 7), (3, 1)]
]
dijkstra(_G, 0)
