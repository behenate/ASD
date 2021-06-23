def DFS_matrix(G):
    def DFS_visit(G, i):
        nonlocal time
        visited[i] = 1
        for j in range(n):
            if G[i][j] and not visited[j]:
                DFS_visit(G, j)
        times[i] = time
        time += 1

    def DFS_reverse(G, i, cnt):
        visited[i] = cnt
        for j in range(n):
            if G[j][i] and not visited[j]:
                DFS_reverse(G, j, cnt)

    n = len(G)
    visited = [0 for _ in range(n)]
    time = 0
    times = [-1 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            DFS_visit(G, i)

    visited = [0 for _ in range(n)]
    cnt = 1
    for i in range(n):
        s_i = -1
        m_v = -1
        for j in range(n):
            if times[j] > m_v and not visited[j]:
                m_v = times[j]
                s_i = j

        if s_i != -1:
            DFS_reverse(G, s_i, cnt)
            cnt += 1
    print(visited)
    return visited, time


_G = [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0],
]
_G1 = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

]
DFS_matrix(_G)
DFS_matrix(_G1)
