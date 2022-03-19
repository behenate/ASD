from math import inf


def DFS_matrix(G, s, t):
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
    return res


def ford_fulkerson(G, s, t):
    res = 0
    while True:
        r = DFS_matrix(G, s, t)
        if r == 0:
            break
        res += r
    print(res)


_G = [
    [0, 4, 3, 0, 0, 0],
    [0, 0, 2, 2, 0, 0],
    [0, 0, 0, 2, 2, 0],
    [0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0],
]
_G1 = [
    [0, 7, 5, 0, 0, 0],
    [0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 10, 0],
    [0, 0, 6, 0, 0, 7],
    [0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0],
]
ford_fulkerson(_G, 0, 5)
ford_fulkerson(_G1, 0, 5)
