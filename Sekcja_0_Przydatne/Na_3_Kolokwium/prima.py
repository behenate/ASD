from math import inf
from queue import PriorityQueue


def prima(G):
    n = len(G)
    visited = [0 for _ in range(n)]
    dist = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    s = 0
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
            if d < dist[elem]:
                dist[elem] = d
                queue.put((d, elem))
                parent[elem] = i
    print(parent)


_G = [
    [[1, 1], [2, 12]],
    [[0, 1], [2, 7], [3, 5]],
    [[0, 12], [1, 7], [3, 6], [4, 8]],
    [[1, 5], [2, 6], [4, 4], [5, 3000]],
    [[2, 8], [3, 4], [5, 9]],
    [[4, 9], [3, 3000]],
]
prima(_G)
