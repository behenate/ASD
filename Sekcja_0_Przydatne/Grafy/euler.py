def euler(G):
    def DFS_visit(G, i):
        nonlocal time
        time += 1
        stack.append(i)
        for j in range(n):
            if G[i][j]:
                G[i][j] = 0
                G[j][i] = 0
                DFS_visit(G, j)
        cycle.append(stack.pop())
    n = len(G)
    stack = []
    cycle = []
    time = 0
    DFS_visit(G, 0)
    print(cycle)


_G = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
]
euler(_G)