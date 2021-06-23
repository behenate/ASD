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
        print(i, dist_to)
        if visited[i]:
            continue
        visited[i] = 1
        for j in range(n):
            if G[i][j] == -1:
                continue
            elem, d = j, G[i][j]
            if visited[elem]:
                continue
            if dist_to + d < dist[elem]:
                dist[elem] = dist_to + d
                queue.put((dist[elem], elem))
                parent[elem] = i

    print(parent)
    print(dist)

dijkstra(_G, 0)
