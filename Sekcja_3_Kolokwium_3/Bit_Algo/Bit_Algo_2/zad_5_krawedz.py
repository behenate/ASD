from math import inf
from queue import PriorityQueue


# 0 bez dodatkowej, 1 - z dodatkowa
def dijkstra(G, A_G, s, t):
    n = len(G)
    visited = [[0, 0] for _ in range(n)]
    dist = [[inf, inf] for _ in range(n)]
    shorted_edge = [-1 for _ in range(n)]
    dist[s][0] = 0
    queue = PriorityQueue()
    queue.put((0, s, 0, -1))
    while queue.qsize() > 0:
        dist_to, i, f_a, s_i = queue.get()
        if visited[i][f_a]:
            continue
        visited[i][f_a] = 1
        if f_a:
            shorted_edge[i] = shorted_edge[s_i]
        for e in G[i]:
            elem, d = e
            if visited[elem][f_a]:
                continue
            if dist_to + d < dist[elem][f_a]:
                dist[elem][f_a] = dist_to + d
                queue.put((dist[elem][f_a], elem, f_a, s_i))
        if f_a == 0:
            cnt = -1
            for e in A_G[i]:
                cnt += 1
                elem, d = e
                if visited[elem][1]:
                    continue
                if dist_to + d < dist[elem][1]:
                    dist[elem][1] = dist_to + d
                    shorted_edge[elem] = (i, elem)
                    queue.put((dist[elem][1], elem, 1, elem))
    for line in dist:
        print(line)
    print(shorted_edge)


_G = [
    [[1, 1], [2, 2]],
    [[0, 1], [3, 3], [4, 5]],
    [[0, 2], [3, 2], [5, 1]],
    [[1, 3], [2, 2], [5, 1], [4, 2]],
    [[1, 5], [3, 2]],
    [[2, 5], [3, 1]]
]

_A_G = [
    [],
    [[2, 1]],
    [[1, 1], [4, 1]],
    [],
    [[2, 1]],
    [[4, 1]]
]

dijkstra(_G, _A_G, 0, 4)
