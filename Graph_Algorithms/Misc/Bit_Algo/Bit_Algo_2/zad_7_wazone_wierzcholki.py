from math import inf
from queue import PriorityQueue

_vertex_cost = [5, 4, 2, 1, 2]
_G = [
    [[1, 6], [4, 3]],
    [[2, 5], [0, 6]],
    [[3, 2], [1, 5]],
    [[2, 2], [4, 4]],
    [[3, 4], [0, 3]],
]


def dijkstra(G, vertex_cost, s):
    n = len(G)
    convert_graph(G, vertex_cost)
    for line in G:
        print(line)
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
        for e in G[i]:
            elem, d = e
            if visited[elem]:
                continue
            if dist_to + d < dist[elem]:
                dist[elem] = dist_to + d
                queue.put((dist[elem], elem))
                parent[elem] = i
    print(dist)
def convert_graph(G, cost):
    n = len(G)
    for i in range(n):
        for neigh in G[i]:
            neigh[1] += cost[neigh[0]]

dijkstra(_G, _vertex_cost, 0)