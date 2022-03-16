from queue import Queue
from math import inf
# _G = [
#     [0, 4, 3, 0, 0, 0],
#     [0, 0, 2, 2, 0, 0],
#     [0, 0, 0, 2, 2, 0],
#     [0, 0, 0, 0, 0, 4],
#     [0, 0, 0, 0, 0, 5],
#     [0, 0, 0, 0, 0, 0],
# ]
# Tu ma być 6 ^^^^
_G = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

# Tu ma być 23 ^^^^^^^

def try_path(G, s, t):
    def DFS_visit(G, i, water_in):
        visited[i] = 1
        flowed = 0
        for j in range(n):
            if G[i][j] and not visited[j]:
                parent[j] = i
                r = DFS_visit(G, j, min(water_in-flowed, G[i][j]))
                if r:
                    flowed += r
        if flowed != 0 and parent[i] is not None:
            G[parent[i]][i] -= flowed
            G[i][parent[i]] += flowed
        if i == t:
            G[parent[i]][i] -= water_in
            G[i][parent[i]] += water_in
            visited[t] = 0
            return water_in
        return flowed
    n = len(G)
    visited = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    res = DFS_visit(G, s, 99999)
    result = res
    while res != 0:
        visited = [0 for _ in range(n)]
        parent = [None for _ in range(n)]
        res = DFS_visit(G, s, 99999)
        result += res
    print("Wynik", result)
    for line in G:
        print(line)
    return visited, parent

try_path(_G, 0, 5)

