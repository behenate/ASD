from queue import Queue
from math import inf
G = [
    [[1, 1], [2, 3]],
    [[0, 1], [3, 4]],
    [[0, 3], [4, 5]],
    [[1, 4], [5,2]],
    [[2, 5], [5, 1]],
    [[3, 2], [4, 1]],
]


def weighted_BFS(G, s):
    queue = Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0
    parent[s] = None
    queue.put((s, 1, 1))
    while not queue.empty():
        elem, d, t = queue.get()
        print(elem, d, t)
        if visited[elem]:
            continue
        if t < d:
            queue.put((elem, d, t+1))
            continue
        visited[elem] = True
        for neigh in G[elem]:
            d = neigh[1]
            neigh = neigh[0]
            if not visited[neigh] and distance[neigh] > distance[elem]+d:
                distance[neigh] = distance[elem] + d
                parent[neigh] = elem
                queue.put((neigh, d, 1))
    return visited, distance, parent

print(weighted_BFS(G, 0))