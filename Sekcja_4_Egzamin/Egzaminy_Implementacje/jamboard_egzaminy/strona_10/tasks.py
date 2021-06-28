

def tasks(T):
    n = len(T)
    for i in range(n):
        for j in range(n):
            if T[i][j] != 1:
                T[i][j] = 0
    def DFS_visit(G, i):
        visited[i] = 1
        for j in range(n):
            if G[i][j] and not visited[j]:
                DFS_visit(G, j)
        top_order.append(i)
    visited = [0 for _ in range(n)]
    top_order = []
    for i in range(n):
        if not visited[i]:
            DFS_visit(T, i)
    top_order.reverse()
    print(top_order)


T = [[0, 2, 1, 1], [1, 0, 1, 1], [2, 2, 0, 1], [2, 2, 2, 0]]
tasks(T)