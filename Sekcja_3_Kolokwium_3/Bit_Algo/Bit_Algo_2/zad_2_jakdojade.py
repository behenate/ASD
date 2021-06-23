from math import inf
from queue import PriorityQueue



def jak_dojade(G, P, d, s, t):
    n = len(G)
    visited = [[0 for _ in range(d+1)] for _ in range(n)]
    dist = [[inf for _ in range(d+1)] for _ in range(n)]
    parent = [[-1 for _ in range(d+1)] for _ in range(n)]
    station = [i in P for i in range(n)]
    dist[s][d] = 0
    queue = PriorityQueue()
    queue.put((0, s, d))
    while queue.qsize() > 0:
        dist_to, i, fuel_left = queue.get()
        if station[i] and fuel_left != d:
            if dist_to < dist[i][d]:
                dist[i][d] = dist_to
                parent[i][d] = parent[i][fuel_left]
                queue.put((dist_to, i, d))
                continue
            else:
                continue
        if visited[i][fuel_left]:
            continue
        visited[i][fuel_left] = 1
        for j in range(n):
            if G[i][j] == -1:
                continue
            elem, w = j, G[i][j]
            if fuel_left - w < 0 or visited[elem][fuel_left-w]:
                continue
            if fuel_left >= w and dist_to + w < dist[elem][fuel_left-w]:
                dist[elem][fuel_left-w] = dist_to + w
                queue.put((dist[elem][fuel_left-w], elem, fuel_left-w))
                parent[elem][fuel_left-w] = (i, fuel_left)
    print(dist)
    for line in parent:
        print(line)
    min_cost = inf
    m_i = -1
    for i in range(d+1):
        if dist[t][i] < min_cost:
            min_cost = dist[t][i]
            m_i = i
    w = (t, m_i)
    while w != -1:
        print(w[0])
        w = parent[w[0]][w[1]]
    for line in dist:
        print(line)
    for line in parent:
        print(line)

_G = [
    [-1, 6, -1, 5, 2],
    [-1, -1, 1, 2, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, 4, -1, -1],
    [-1, -1, 8, - 1, -1]
]

_P = [0, 1, 3]

jak_dojade(_G, _P, 5, 0, 2)