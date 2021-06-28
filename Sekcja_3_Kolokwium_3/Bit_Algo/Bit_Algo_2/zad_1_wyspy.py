from math import inf
from queue import PriorityQueue


def t(n):
    if n == 0:
        print("Cos zle jest")
    if n == 1:
        return 0
    elif n == 5:
        return 1
    else:
        return 2


def dijkstra(G, s):
    n = len(G)
    visited = [[0, 0, 0] for _ in range(n)]
    dist = [[inf, inf, inf] for _ in range(n)]
    parent = [[-1, -1, -1] for _ in range(n)]
    dist[s] = [0, 0, 0]
    queue = PriorityQueue()
    queue.put((0, s, 0))
    queue.put((0, s, 1))
    queue.put((0, s, 2))
    while queue.qsize() > 0:
        dist_to, i, transport = queue.get()
        print(i, dist_to)
        if visited[i][transport]:
            continue
        visited[i][transport] = 1
        for j in range(n):
            if G[i][j] == 0:
                continue
            elem, d = j, G[i][j]
            if t(d) == transport:
                continue
            if visited[elem][t(d)]:
                continue
            if dist_to + d < dist[elem][t(d)]:
                dist[elem][t(d)] = dist_to + d
                queue.put((dist[elem][t(d)], elem, t(d)))
                parent[elem][t(d)] = [i, transport]

    for line in dist:
        print(line)
    print(dist)

_G = [
    [0, 5, 1, 8, 0, 0, 0],
    [5, 0, 0, 1, 0, 8, 0],
    [1, 0, 0, 8, 0, 0, 8],
    [8, 1, 8, 0, 5, 0, 1],
    [0, 0, 0, 5, 0, 1, 0],
    [0, 8, 0, 0, 1, 0, 5],
    [0, 0, 8, 1, 0, 5, 0]
]
dijkstra(_G, 5)
