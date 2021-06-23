def znajdz_przedzial(przedzialy, a, b):
    def DFS_visit(G, i):
        visited[i] = True
        for neigh in G[i]:
            print(neigh, G)
            if not visited[neigh]:
                DFS_visit(G, neigh)
    n = len(przedzialy)
    m_val = 0

    for i in range(n):
        m_val = max(m_val, przedzialy[i][1])
    visited = [False for _ in range(m_val+1)]
    G = [[] for _ in range(m_val+1)]
    for i in range(n):
        G[przedzialy[i][0]].append(przedzialy[i][1])
    DFS_visit(G, a)
    return visited[b]



przedzialy = [[0, 1], [0, 3], [2, 4], [4, 5], [1, 6], [3, 7], [5, 6]]
print(znajdz_przedzial(przedzialy, 1, 7))
