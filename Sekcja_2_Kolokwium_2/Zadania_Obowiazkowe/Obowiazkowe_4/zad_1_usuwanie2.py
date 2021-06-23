def DFS(G):
    def DFS_visit(G, i):
        nonlocal time
        time += 1
        visited[i] = True
        for neigh in G[i]:
            if not visited[neigh]:
                parent[neigh] = i
                DFS_visit(G, neigh)
        time += 1
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    time = 0
    for i in range(n):
        if not visited[i]:
            DFS_visit(G, i)
    return visited, parent, time

