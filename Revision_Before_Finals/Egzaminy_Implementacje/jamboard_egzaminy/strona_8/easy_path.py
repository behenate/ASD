from queue import PriorityQueue
from math import inf


def dijkstra(G, s):
    n = len(G)
    visited = [0 for _ in range(n)]
    dist = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    deg = [len(G[i]) for i in range(n)]
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
            if visited[elem] or deg[elem] > 2:
                continue
            if dist_to + d < dist[elem]:
                dist[elem] = dist_to + d
                queue.put((dist[elem], elem))
                parent[elem] = i
    print(dist)

G = [
    [[1, 1], [2, 5]],
    [[0, 1], [3, 1], [4, 1]],
    [[0, 5], [5, 10]],
    [[1, 1], [3, 4]],
    [[3, 3], [1, 1], [6, 4]],
    [[2, 10], [6, 15]],
    [[4, 4], [5, 15]],
]
dijkstra(G, 0)