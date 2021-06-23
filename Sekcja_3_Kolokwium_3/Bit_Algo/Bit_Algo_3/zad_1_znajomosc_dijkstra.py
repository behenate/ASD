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
    m_d = 0
    m_d_i = 0
    while queue.qsize() > 0:
        dist_to, i = queue.get()
        if visited[i]:
            continue
        visited[i] = 1
        if dist_to > m_d:
            m_d = dist_to
            m_d_i = i
        for j in range(n):
            if G[i][j] == 0:
                continue
            elem, d = j, G[i][j]
            if visited[elem]:
                continue
            if dist_to + d < dist[elem]:
                dist[elem] = dist_to + d
                queue.put((dist[elem], elem))
                parent[elem] = i

    return m_d, m_d_i
def max_dist(G):
    n = len(G)
    m = 0
    f = 0
    t = 0
    for i in range(n):
        r, to = dijkstra(G, i)
        if r > m:
            m = r
            f = i
            t = to
    print(m, "z: ",f,"do: ", t)


_G = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
]

max_dist(_G)

