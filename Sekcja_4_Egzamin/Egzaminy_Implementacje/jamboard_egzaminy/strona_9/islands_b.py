from math import inf
def dijkstra(G, s):
    n = len(G)
    #za 1, za 5, za 8
    d = [[inf,inf,inf] for _ in range(n)]
    visited = [[False,False,False] for _ in range(n)]
    d[s][0] = 0
    d[s][1] = 0
    d[s][2] = 0
    for ctr in range(3*n):
        u = -1
        najkrotsza = inf
        for k in range(3):
            for i in range(n):
                if visited[i][k] == False and d[i][k] < najkrotsza:
                    najkrotsza = d[i][k]
                    u = i
                    typ = k
        visited[u][typ] = True
        for i in range(n):
            x = option_reverse(G[u][i])
            "Tu poniżej zamiana x na typ w dwóch miejscach i działa :))))"
            if G[u][i] != 0 and G[u][i] != option(typ) and visited[i][x] == False and d[i][x] > d[u][typ] + G[u][i]:
                d[i][x] = d[u][typ] + G[u][i]
    return d
def option(a):
    if a == 0:return 1
    if a == 1:return 5
    if a == 2:return 8
def option_reverse(a):
    if a == 1:return 0
    if a == 5:return 1
    if a == 8:return 2
G = [[0, 5, 1, 8, 0, 0, 0],
    [5, 0, 0, 1, 0, 8, 0],
    [1, 0, 0, 8, 0, 0, 8],
    [8, 1, 8, 0, 5, 0, 1],
    [0, 0, 0, 5, 0, 1, 0],
    [0, 8, 0, 0, 1, 0, 5],
    [0, 0, 8, 1, 0, 5, 0]]
print(dijkstra(G,5))