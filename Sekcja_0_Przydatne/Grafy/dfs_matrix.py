def DFS_matrix(G):
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
    for i in range(n):
        if not visited[i]:
            DFS_visit(G, i)
    return visited, parent, time

_G = [[0, 1, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 0],
      [0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0]
      ]
a, b, c = DFS_matrix(_G)
print(a, b, c)