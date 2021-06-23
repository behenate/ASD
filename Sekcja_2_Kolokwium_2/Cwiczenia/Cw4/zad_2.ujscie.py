_G = [
    [0, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
]


def DFS_matrix(G):
    def DFS_visit(G, i):
        visited[i] = 1
        c = 0
        for j in range(n):
            if G[i][j] and not visited[j]:
                c += 1
                parent[j] = i
                r = DFS_visit(G, j)
                if r is not None:
                    return r
        if c == 0:
            return i

    n = len(G)
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    cand = DFS_visit(G, 0)
    ok = True
    for i in range(n):
        if G[i][cand] != 1 and i != cand:
            ok = False
        if G[cand][i] == 1:
            ok = False
    print(ok)
    # return visited, parent, time

DFS_matrix(_G)