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
            new_d = max(dist_to , d)
            if new_d < dist[elem]:
                dist[elem] = new_d
                queue.put((dist[elem], elem))
                parent[elem] = i
    print(dist)

_G = [
    [[1, 60], [2, 120]],
    [[0, 60], [3, 80]],
    [[0, 120], [4, 150]],
    [[1, 80], [4, 70]],
    [[2, 150], [3, 70]]
]

dijkstra(_G, 0)