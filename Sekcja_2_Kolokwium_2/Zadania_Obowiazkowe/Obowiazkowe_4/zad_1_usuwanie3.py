def DFS(G):
    def DFS_visit(G, i):
        nonlocal time
        times[i] = (time, i)
        time += 1
        visited[i] = True
        for neigh in G[i]:
            if not visited[neigh]:
                parent[neigh] = i
                DFS_visit(G, neigh)
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    times = [0 for _ in range(n)]
    time = 0
    DFS_visit(G, 0)
    times = sorted(times)
    print(times)
    for i in range(n-1, -1, -1):
        print(times[i][1])
    return visited, parent, time


_G = [
    [1, 4],
    [0, 2],
    [1, 4, 3],
    [2, 6, 5],
    [0, 2, 7],
    [6, 3],
    [5, 3],
    [4]
]
a, b, c = DFS(_G)

