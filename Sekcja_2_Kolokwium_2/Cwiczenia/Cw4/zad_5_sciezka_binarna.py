from collections import deque
from math import inf
_G = [
    [(1, 0), (4, 1)],
    [(0, 0), (3, 0), (2, 1)],
    [(1, 1), (3, 0), (5, 1)],
    [(1, 0), (2, 1)],
    [(0, 1), (5, 1)],
    [(4, 1), (2, 1)]
]

from queue import Queue
def BFS(G, s, target):
    queue = deque()
    n = len(G)
    distance = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0
    parent[s] = None
    queue.append(s)
    while len(queue) > 0:
        elem = queue.popleft()
        for neigh in G[elem]:
            if distance[elem] + neigh[1] < distance[neigh[0]]:
                distance[neigh[0]] = distance[elem] + neigh[1]
                parent[neigh[0]] = elem
                if neigh[1] == 0:
                    queue.appendleft(neigh[0])
                else:
                    queue.append(neigh[0])

    if elem == target:
        return distance, parent
print(BFS(_G, 0, 5))