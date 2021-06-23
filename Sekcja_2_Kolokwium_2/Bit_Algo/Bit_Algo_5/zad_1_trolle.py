def DFS_mosty(G, hideout):
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
            bridges[i] = True

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    bridges = [False for _ in range(n)]
    times = [0 for _ in range(n)]
    lows = [0 for _ in range(n)]
    time = 0
    DFS_visit(G, hideout)
    return bridges


def DFS_count(G, start, blocker, trolls):
    def DFS_visit(G, i):
        nonlocal troll_count
        troll_count += trolls[i]
        visited[i] = True
        for neigh in G[i]:
            if not visited[neigh]:
                DFS_visit(G, neigh)
    n = len(G)
    troll_count = 0
    visited = [False for _ in range(n)]
    visited[blocker] = True
    DFS_visit(G, start)
    return troll_count


def trolle(G, trolls, hideout):
    def DFS_visit(G, i):
        if bridges[i]:
            s = (DFS_count(G, i, parent[i], trolls))
            candidates.append((s, (i, parent[i])))
        else:
            visited[i] = True
            for neigh in G[i]:
                if not visited[neigh]:
                    parent[neigh] = i
                    DFS_visit(G, neigh)

    bridges = DFS_mosty(G, hideout)
    print(bridges)
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    candidates = []
    DFS_visit(G, hideout)
    candidates = sorted(candidates)
    print(candidates[-1][1])


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
# Kryjówka na 6 indexie
trolls = [300, 5, 6, 2, 1, 3, 0, 100, 15, 1, 3, 2]
trolle(_G, trolls, 6)
