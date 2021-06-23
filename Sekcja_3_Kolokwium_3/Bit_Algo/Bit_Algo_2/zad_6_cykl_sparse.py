from math import inf
from queue import PriorityQueue


def dijkstra(G, s, s_i):
    n = len(G)
    visited = [0 for _ in range(n)]
    dist = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[s] = 0
    queue = PriorityQueue()
    starting = True
    queue.put((0, s))
    while queue.qsize() > 0:
        dist_to, i = queue.get()
        if visited[i]:
            continue
        visited[i] = 1
        if starting:
            elem, d = G[i][s_i]
            if dist_to + d < dist[elem]:
                dist[elem] = dist_to + d
                queue.put((dist[elem], elem))
                parent[elem] = s
                starting = False
                dist[s] = inf
                visited[s] = False
                continue
        for e in G[i]:
            elem, d = e
            print(elem, parent[i])
            if visited[elem] or parent[i] == elem:
                continue
            if dist_to + d < dist[elem]:
                dist[elem] = dist_to + d
                queue.put((dist[elem], elem))
                parent[elem] = i

    print(parent)
    print(dist)


_G = [
    [[1, 2]],
    [[0, 2], [3, 3], [2, 1]],
    [[1, 1], [4, 1]],
    [[1, 3], [4, 3], [6, 1]],
    [[3, 3], [2, 1], [5, 2]],
    [[6, 1], [4, 2]],
    [[3, 1], [5, 1]],
]
dijkstra(_G, 1, 2)
