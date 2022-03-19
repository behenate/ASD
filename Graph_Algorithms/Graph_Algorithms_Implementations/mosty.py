def DFS_mosty(G, s):
    def DFS_visit(G, i):
        nonlocal time
        time += 1
        times[i] = time
        lows[i] = time
        visited[i] = True
        for neigh in G[i]:
            if visited[neigh] and neigh != parent[i] and parent[i] != -1:
                if lows[i] > lows[neigh]:
                    lows[i] = lows[neigh]
            if not visited[neigh]:
                parent[neigh] = i
                DFS_visit(G, neigh)
        if lows[parent[i]] > lows[i] and parent[i] != -1:
            lows[parent[i]] = lows[i]
        if lows[i] == times[i] and parent[i] != -1:
            bridges[parent[i]] = True
            bridges[i] = True

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    bridges = [False for _ in range(n)]
    times = [0 for _ in range(n)]
    lows = [0 for _ in range(n)]
    time = 0
    DFS_visit(G, s)
    return bridges
_G = [
    [1, 2],
    [0, 2],
    [1, 0, 3],
    [2, 4],
    [3, 5, 6, 7],
    [4, 7, 6],
    [4, 5, 7],
    [4, 5, 6, 8],
    [7, 9, 10, 11],
    [8, 11],
    [8, 11],
    [8, 9, 10]
]
print(DFS_mosty(_G, 6))