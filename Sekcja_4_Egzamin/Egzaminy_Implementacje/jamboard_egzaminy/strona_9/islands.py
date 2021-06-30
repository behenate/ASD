from math import inf


def dijkstra(G, s, t):
    n = len(G)
    dist = [[inf, inf, inf] for _ in range(n)]
    visited = [[0, 0, 0] for _ in range(n)]
    parent = [[-1, -1, -1] for _ in range(n)]
    dist[s][0] = 0
    dist[s][1] = 0
    dist[s][2] = 0
    for bla in range(3):
        for i in range(n):
            elem = -1
            min_dist = inf
            way = -1
            for k in range(3):
                for j in range(n):
                    if not visited[j][k] and dist[j][k] < min_dist:
                        min_dist = dist[j][k]
                        elem = j
                        way = k
            visited[elem][way] = True
            print(elem, way, min_dist, dist[elem][way])
            for j in range(n):
                if (G[elem][j] == 1 and way == 0) or (G[elem][j] == 5 and way == 1) or (G[elem][j] == 8 and way == 2)\
                        or not G[elem][j]:
                    continue
                if G[elem][j] == 1 and not visited[j][0] and dist[j][0] > dist[elem][way] + G[elem][j]:
                    print(G[elem], j)
                    dist[j][0] = dist[elem][way] + G[elem][j]
                    parent[j][0] = (elem, way)

                if G[elem][j] == 5 and not visited[j][1] and dist[j][1] > dist[elem][way] + G[elem][j]:
                    print(G[elem], j)
                    dist[j][1] = dist[elem][way] + G[elem][j]
                    parent[j][1] = (elem, way)

                if G[elem][j] == 8 and not visited[j][2] and dist[j][2] > dist[elem][way] + G[elem][j]:
                    print(G[elem], j)
                    dist[j][2] = dist[elem][way] + G[elem][j]
                    parent[j][2] = (elem, way)

    """[[14, 12, 14], [7, 19, inf], [13, inf, 13], [6, 6, 20], [1, 11, inf], [0, 0, 0], [7, 5, inf]]"""
    print(dist)
    print(parent)
    print(dist[t])


G = [
    [0, 5, 1, 8, 0, 0, 0],
    [5, 0, 0, 1, 0, 8, 0],
    [1, 0, 0, 8, 0, 0, 8],
    [8, 1, 8, 0, 5, 0, 1],
    [0, 0, 0, 5, 0, 1, 0],
    [0, 8, 0, 0, 1, 0, 5],
    [0, 0, 8, 1, 0, 5, 0],
]
dijkstra(G, 5, 2)
