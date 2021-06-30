from math import inf
from zad3testy import runtests
def mile_jumps(G):
    n = len(G)
    H = [[0 for i in range(n)] for i in  range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]:
                for k in range(n):
                    if G[j][k] and k != i and (H[i][k] > max(G[i][j], G[j][k]) or H[i][k] ==0):
                        H[i][k] = max(G[i][j], G[j][k])

    return H
def jumper(G,s, t):
    H = mile_jumps(G)
    for line in H:
        print(line)
    n = len(G)
    dist = [[inf, inf] for _ in range(n)]
    visited = [[0,0] for _ in range(n)]
    dist[s][0] = 0
    dist[s][1] = 0
    for i in range(2*n):
        elem = -1
        min_dist = inf
        boots = 0
        for k in range(2):
            for j in range(n):
                if not visited[j][k] and dist[j][k] < min_dist:
                    min_dist = dist[j][k]
                    elem = j
                    boots = k
        visited[elem][boots] = True

        for j in range(n):
            if G[elem][j] > 0 and boots and not visited[j][0]:
                if dist[j][0] > dist[elem][boots] + G[elem][j]:
                    dist[j][0] = dist[elem][boots] + G[elem][j]
            if H[elem][j] > 0 and not boots:
                d = H[elem][j]
                if not visited[j][1] and dist[j][1] > dist[elem][boots] + d:
                    dist[j][1] = dist[elem][boots] + d
            if G[elem][j] > 0 and not boots:
                d = G[elem][j]
                if not visited[j][0] and dist[j][0] > dist[elem][boots] + d:
                    dist[j][0] = dist[elem][boots] + d
    return min(dist[t])
runtests(jumper)
