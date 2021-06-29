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
    max_dist = 0
    mdi = -1
    while queue.qsize() > 0:
        dist_to, i = queue.get()
        if visited[i]:
            continue
        if dist_to > max_dist:
            max_dist = dist_to
            print(i)
            mdi = i
        visited[i] = 1
        for e in G[i]:
            elem, d = e
            if visited[elem]:
                continue
            if dist_to + d < dist[elem]:
                dist[elem] = dist_to + d
                queue.put((dist[elem], elem))
                parent[elem] = i
    return max_dist, parent,mdi


def diagonal(G):
    n = len(G)
    max_dist = 0
    max_parent = None
    mdi = -1
    for i in range(n):
        dist, parent, i = dijkstra(G, i)
        if dist > max_dist:
            mdi= i
            max_dist = dist
            max_parent = parent
    print("Przekątna: ", end="")
    while mdi != -1:
        print(mdi, end=" ")
        mdi = max_parent[mdi]
    print()
    print("Odległość: ", max_dist)

G = [
    [[1, 8], [3, 5]],
    [[0, 8], [2, 4]],
    [[1, 4], [3, 2]],
    [[0, 5], [2, 2], [4, 6]],
    [[3, 6], [5, 4]],
    [[4, 4], [6, 3]],
    [[5, 3]],
]
diagonal(G)