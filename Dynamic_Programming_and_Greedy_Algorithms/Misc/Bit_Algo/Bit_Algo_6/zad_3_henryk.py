from math import dist
from queue import Queue
_islands = [
    [0, 0],
    [0.5, 0.5],
    [1, 1],
    [1, 2],
    [2, 1],
    [2.5, 2.5],
    [2.5, 4],
    [3.5, 2.5],
    [3, 4],
    [4, 3.5],
    [4, 4.5],
    [5, 4.5],
    [5, 5.5],
    [6, 5],
    [6, 5.5],
    [7, 6]
]
# _islands = [
#     [0, 1],
#     [1, 2],
#     [2, 1],
#     [3, 0],
#     [1, 3]
# ]


def islands_to_graph(islands, d):
    n = len(islands)
    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if dist(islands[i], islands[j]) <= d:
                G[i].append([j, 1, False])
            elif dist(islands[i], islands[j]) <= 2 * d:
                G[i].append([j, 2, False])
    return G


def henryk(islands, d, s, t):
    G = islands_to_graph(islands, d)
    queue = Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited[s] = True
    distance[s] = 0
    parent[s] = None
    queue.put(s)
    while not queue.empty():
        elem = queue.get()
        for i in range(len(G[elem])):
            neigh = G[elem][i][0]
            dist = G[elem][i][1]
            repeats = G[elem][i][2]
            if not visited[neigh]:
                if dist != 2 or neigh == t:
                    visited[neigh] = True
                    if not repeats:
                        distance[neigh] = distance[elem] + 1
                    else:
                        distance[neigh] = distance[elem] + 2
                    parent[neigh] = elem
                    queue.put(neigh)
                elif dist == 2:
                    queue.put(elem)
                    distance[neigh] = 1
                    G[elem][i][1] -= 1
                    G[elem][i][2] = True
    print(distance, distance[t])
    while parent[t] is not None:
        print(t)
        t = parent[t]
    print(t)
    return visited, distance, parent


print(henryk(_islands, 1.2, 0, 15))
