def DFS(G):
    def DFS_visit(G, i):
        visited[i] = True
        for neigh in G[i]:
            if not visited[neigh]:
                parent[neigh] = i
                DFS_visit(G, neigh)
        top_order.append(i)
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    top_order = []

    for i in range(n):
        if not visited[i]:
            DFS_visit(G, i)
    top_order.reverse()
    return visited, parent, top_order


_G = [
    [1],
    [2],
    [3,4],
    [4,],
    [5, 6],
    [],
    [7],
    [5]
]
a, b, d = DFS(_G)
print(a, b, d)
