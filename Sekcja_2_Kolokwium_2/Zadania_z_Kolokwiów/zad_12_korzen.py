_G = [
    [2],
    [2],
    [0, 1, 3],
    [2, 4],
    [3, 5, 6],
    [4],
    [4]
]


def DFS(G):
    def DFS_visit(G, i, dist):
        nonlocal m_d_i
        visited[i] = True
        if dist > m_d:
            m_d_i = i
        for neigh in G[i]:
            if not visited[neigh]:
                parent[neigh] = i
                DFS_visit(G, neigh, dist+1)

    n = len(G)
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    m_d = 0
    m_d_i = 0
    DFS_visit(G, 0, 0)
    start = m_d_i
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    m_d = 0
    DFS_visit(G, start, 0)
    end = m_d
    path = []

    while end != start:
        path.append(end)
        end = parent[end]
    path.append(start)
    print(path[len(path)//2])
DFS(_G)
