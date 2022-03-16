_G = [
    [0, 2, 3, 0, 0, 0, 0, 0],
    [2, 0, 4, 0, 6, 0, 0, 0],
    [3, 4, 0, 5, 0, 0, 0, 0],
    [0, 0, 5, 0, 3, 0, 0, 0],
    [0, 6, 0, 3, 0, 8, 5, 2],
    [0, 0, 0, 0, 8, 0, 7, 0],
    [0, 0, 0, 0, 5, 7, 0, 11],
    [0, 0, 0, 0, 2, 0, 11, 0]
]


def airplane(G, t, target):
    def DFS_visit(G, i, alt, l_a, h_a):
        if alt + t < h_a:
            h_a = alt + t
        if alt - t > l_a:
            l_a = alt - t
        if i == target:
            print(l_a, h_a)
            return True
        r = False
        visited[i] = 1
        for j in range(n):
            if G[i][j] and not visited[j] and G[i][j] - t <= h_a and G[i][j] + t >= l_a:
                parent[j] = i
                r = DFS_visit(G, j, G[i][j], l_a, h_a) or r
        return r

    n = len(G)
    found = False
    for i in range(n):
        if G[0][i]:
            l_a = G[0][i] - t
            h_a = G[0][i] + t
            visited = [0 for _ in range(n)]
            parent = [-1 for _ in range(n)]
            found = found or DFS_visit(G, i, G[0][i], l_a, h_a)

    print(found)

airplane(_G, 1, 3)
