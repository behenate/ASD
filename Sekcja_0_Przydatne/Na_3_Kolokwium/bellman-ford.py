from queue import PriorityQueue
from math import inf
_G = [
    [[1, 1], [2, 1]],
    [[2, 1], [6, -2]],
    [[5, 1], [3, 2]],
    [[4, -2]],
    [[5, -2]],
    [[7, 1]],
    [[8, 5]],
    [[6, 1], [8, 1]],
    [],
]

def bellman_ford(G, s, t):
    n = len(G)
    dist = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    jump = [0 for _ in range(n)]
    dist[s] = 0
    for _ in range(n-1):
        for i in range(n):
            vertex = G[i]
            for tup in vertex:
                neigh, d = tup
                if dist[i] + d < dist[neigh]:
                    dist[neigh] = dist[i] + d
                    jump[neigh] = d
                    parent[neigh] = i
    print(parent)
    print(dist)
    print(jump)

    w = t
    for i in range(n):
        vertex = G[i]
        for tup in vertex:
            neigh, d = tup
            if dist[neigh] > dist[i] + d:
                print("Ujemny cykl!")
                return False
    print(w)

bellman_ford(_G, 0, 8)



