from queue import PriorityQueue
from math import inf
from copy import deepcopy


def dijkstra(G, s):
    n = len(G)
    visited = [0 for _ in range(n)]
    dist = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[s] = 0
    queue = PriorityQueue()
    queue.put((0, s))
    while queue.qsize() > 0:
        dist_to, i = queue.get()
        if visited[i]:
            continue
        visited[i] = 1
        for j in range(len(G[i])):
            if G[i][j] == -1 or G[i][j] == 0:
                continue
            elem, d = j, G[i][j]
            if visited[elem]:
                continue
            if dist_to + d < dist[elem]:
                dist[elem] = dist_to + d
                queue.put((dist[elem], elem))
                parent[elem] = i
    return dist,parent


G = [
    [0, 1, 5, 0, 0],
    [1, 0, 2, 8, 7],
    [5, 2, 0, 3, 0],
    [0, 8, 3, 0, 1],
    [0, 7, 0, 1, 0]
]

def min_cycle(G):
    n = len(G)
    min_cost = inf
    min_cycle = []

    processed = [0 for _ in range(n)]
    for v1 in range(n):
        for v2 in range(v1, n):
            if G[v1][v2] != -1 and G[v1][v2] != 0:
                cost = G[v1][v2]
                G[v1][v2] = -1
                G[v2][v1] = -1
                dist, parent = dijkstra(G, v1)
                f_d = dist[v2] + cost
                f_c = []
                p = v2
                while p != -1:
                    f_c.append(p)
                    p = parent[p]
                if f_d < min_cost:
                    min_cycle = f_c
                    min_cost = f_d

    print(min_cost, min_cycle)
    return min_cycle


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]
LEN = 7

GG = deepcopy(G)
cycle = min_cycle(GG)

print("Cykl :", cycle)

if cycle == []:
    print("Błąd (1): Spodziewano się cyklu!")
    exit(0)

L = 0
u = cycle[0]
for v in cycle[1:] + [u]:
    if G[u][v] == -1:
        print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
        exit(0)
    L += G[u][v]
    u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
    print("Błąd (3): Niezgodna długość")
else:
    print("OK")
