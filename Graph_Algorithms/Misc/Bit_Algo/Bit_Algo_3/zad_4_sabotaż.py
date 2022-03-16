from math import inf


def DFS_matrix2(G, s):
    def DFS_visit(G, i):
        nonlocal time
        time += 1
        visited[i] = 1
        for j in range(n):
            if G[i][j] and not visited[j]:
                parent[j] = i
                DFS_visit(G, j)
        time += 1

    n = len(G)
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    time = 0

    DFS_visit(G, s)
    return visited


def DFS_matrix(G, s, t, find_paths=False):
    def DFS_visit(G, i, amount):
        visited[i] = 1
        success = 0
        if i == t:
            success = amount
        for j in range(n):
            if G[i][j] and not visited[j] and success == 0:
                parent[j] = i
                success = DFS_visit(G, j, min(amount, G[i][j]))
        if parent[i] != -1:
            G[parent[i]][i] -= success
            G[i][parent[i]] += success
        return success

    n = len(G)
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    res = DFS_visit(G, s, inf)
    if find_paths:
        return visited
    return res


def ford_fulkerson(G, s, t):
    res = 0
    n = len(G)
    org_g = [[G[i][j] for j in range(n)] for i in range(n)]
    while True:
        r = DFS_matrix(G, s, t)
        if r == 0:
            break
        res += r

    S = DFS_matrix2(G, s)
    for i in range(n):
        for j in range(n):
            if org_g[i][j]:
                if S[i] != S[j]:
                    print("Usuń krawędź: ", i, j)


_G = [
    [0, 8, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 6],
    [0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
ford_fulkerson(_G, 0, 7)
