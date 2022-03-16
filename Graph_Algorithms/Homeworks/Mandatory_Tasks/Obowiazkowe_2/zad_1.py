from queue import PriorityQueue
from math import inf

_G = [
    [[1, 2], [2, 5]],
    [[0, 2], [4, 7], [3, 3]],
    [[0, 5], [3, 4]],
    [[2, 4], [1, 3], [4, 2], [5, 2]],
    [[1, 7], [3, 2], [5, 1]],
    [[3, 2], [4, 1]],
]


def dijkstra(G, s, t):
    n = len(G)
    for i in range(n):
        G[i] = sorted(G[i], key=lambda x: x[1])
    visited = [[inf for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]
    visited[s][s] = 0
    queue = PriorityQueue()
    queue.put((0, inf, s, -1))
    while queue.qsize() > 0:
        dist_to, size, i, fr = queue.get()
        if fr != -1:
            if visited[fr][i] == True:
                continue
            visited[fr][i] = True
            visited[i][fr] = True

        if i == t:
            tmp = visited[i][i]
            visited[i][i] = min(visited[i][i], dist_to)
            if tmp != visited[i][i]:
                parent[i][i] = (fr, i)
            continue
        for e in G[i]:
            elem, d = e
            if visited[i][elem] == True or visited[i][elem] < dist_to + d or d >= size:
                continue
            visited[i][elem] = dist_to + d
            visited[elem][i] = dist_to + d
            parent[i][elem] = (fr, i)
            queue.put((dist_to + d, d, elem, i))

    p = parent[t][t]
    while p != None:
        print(p[1])
        p = parent[p[0]][p[1]]


# TURBO MALA:

# def dijkstra(G, s, t):
#     n = len(G)
#     queue = PriorityQueue()
#     queue.put((0, inf, s, -1, -1))
#     parent = [[None for _ in range(n)] for _ in range(n)]
#     start_parent = None
#     result = inf
#     while queue.qsize() > 0:
#         dist_to, size, i, fr, p = queue.get()
#         par = (p, fr)
#         print(dist_to, fr, i, ",", p, fr)
#
#         if fr != -1 and parent[fr][i] == None:
#             parent[fr][i] = par
#         #  p ->> fr - >> i
#         if i == t:
#             if dist_to < result:
#                 result = dist_to
#                 start_parent = (fr, i)
#         for e in G[i]:
#             elem, d = e
#             if d < size:
#                 queue.put((dist_to + d, d, elem, i, fr))
#     print(result)
#     p = start_parent
#     for line in parent:
#         print(line)
#     print(start_parent)
#     while p != None:
#         print(p[1])
#         p = parent[p[0]][p[1]]

_G = [
    [[1, 7], [2, 8]],
    [[0, 7], [3, 6]],
    [[0, 8], [3, 7]],
    [[1, 6], [2, 7], [4, 6], [5, 5]],
    [[3, 6], [9, 1]],
    [[3, 5], [6, 4]],
    [[5, 4], [7, 3]],
    [[6, 3], [8, 2]],
    [[7, 2], [9, 1]],
    [[8, 1], [4, 1]]
]
# dijkstra(_G, 0, 9)
# G = [
#     [0,7,8,0,0,0,0,0,0,0],
#     [7,0,0,6,0,0,0,0,0,0],
#     [8,0,0,7,0,0,0,0,0,0],
#     [0,6,7,0,6,5,0,0,0,0],
#     [0,0,0,6,0,0,0,0,0,1],
#     [0,0,0,5,0,0,4,0,0,0],
#     [0,0,0,0,0,4,0,3,0,0],
#     [0,0,0,0,0,0,3,0,2,0],
#     [0,0,0,0,0,0,0,2,0,1],
#     [0,0,0,0,1,0,0,0,1,0],
# ]
# _GG = [
#     [[1, 10], [2, 11]],
#     [[0, 10], [4, 9]],
#     [[0, 11], [3, 7]],
#     [[2, 7], [5, 6]],
#     [[1, 9], [5, 1]],
#     [[4, 1], [3, 6]]
# ]
dijkstra(_G, 0, 5)