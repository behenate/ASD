from math import inf


def bellman_ford(G, s, t):
    n = len(G)
    dist = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    jump = [0 for _ in range(n)]
    dist[s] = 0
    for _ in range(n - 1):
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
                print(neigh)
                print("Ujemny cykl!")
                return False
    return dist, parent

def table_to_graph(table, m):
    n = table
    G = [[] for _ in range(m)]
    for elem in table:
        a, b, weight = elem[0], elem[1], elem[2]
        G[a].append((b, weight))
        # G[b].append((a, -weight))
    return G


def find_exchange(table, s, t, n):
    G = table_to_graph(table, n)
    for line in G:
        print(line)
    cost, parent = bellman_ford(G, s, t)
    print(cost, parent)

table = [
    (0, 1, 5),
    (0, 2, 5),
    (2, 3, 4),
    (3, 5, 10),
    (2, 4, 10),
    (4, 5, -15)
]

find_exchange(table,0,5,6)