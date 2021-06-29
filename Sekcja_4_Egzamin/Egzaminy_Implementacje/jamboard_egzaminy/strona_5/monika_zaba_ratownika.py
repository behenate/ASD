from queue import Queue
from math import inf, dist


def monika(points, l):
    n = len(points)
    G = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if dist(points[i], points[j]) <= l / 2:
                G[i][j] = 0.5
            elif dist(points[i], points[j]) <= l:
                G[i][j] = 1
            elif dist(points[i], points[j]) <= 2 * l:
                G[i][j] = 2

    queue = Queue()
    n = len(G)
    visited = [[False, False] for _ in range(n)]
    distance = [[inf, inf] for _ in range(n)]
    parent = [[-1, -1] for _ in range(n)]
    distance[0][0] = 0
    distance[0][1] = 0
    queue.put((0, 0))
    while not queue.empty():
        elem, last = queue.get()
        if visited[elem][last]:
            continue
        visited[elem][last] = 1
        for i in range(n):
            if G[elem][i] == 2 and last == 0 and distance[i][1] > distance[elem][0] + 1:
                distance[i][1] = distance[elem][0] + 1
                parent[i][1] = (elem,last)
                queue.put((i, 1))
            elif 0 < G[elem][i] < 2 and last == 0 and distance[i][0] > distance[elem][0] + 1:
                distance[i][0] = distance[elem][0] + 1
                parent[i][0] = (elem,last)
                queue.put((i, 0))
            elif 0 < G[elem][i] < 1 and last == 1 and distance[i][0] > distance[elem][0] + 1:
                distance[i][0] = distance[elem][1] + 1
                parent[i][0] = (elem,last)
                queue.put((i, 0))
    print(distance)
    si = 0
    if distance[-1][0] > distance[-1][1]:
        si = 1
    p = parent[-1][si]
    print(n-1, " long" if si==1 else " short", end=" ")
    while p != -1:
        print(p[0], " long" if p[1]==1 else " short", end=" ")
        p = parent[p[0]][p[1]]
    print("")
    print(distance)


points = [
    [0, 0],
    [1, 1],
    [2, 1],
    [3, 1],
    [4, 1],
    [6, 1],
    [6, 2],
    [3, 3],
    [3, 4],
    [3, 5],
    [5, 5],
    [7, 5],
    [8, 6],
]
monika(points, 2)
