G = [
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 0]
]

def DFS(G, s_x, s_y):
    def DFS_visit(G, x, y):
        nonlocal time
        time += 1
        G[x][y] = 0
        print(x, y )
        if x - 1 >= 0 and G[x - 1][y]:
            DFS_visit(G, x - 1, y)
        if x + 1 < n and G[x + 1][y]:
            DFS_visit(G, x + 1, y)
        if y - 1 >= 0 and G[x][y - 1]:
            DFS_visit(G, x, y - 1)
        if y + 1 < n and G[x][y + 1]:
            DFS_visit(G, x, y + 1)
    n = len(G)
    time = 0

    DFS_visit(G, s_x, s_y)
    print(time)
    return time
DFS(G, 3, 3)