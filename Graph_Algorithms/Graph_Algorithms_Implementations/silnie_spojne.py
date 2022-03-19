_G = [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0]
]


def DFS_matrix(G):
    def DFS_visit(G, i):
        nonlocal time
        visited[i] = 1
        for j in range(n):
            if G[i][j] and not visited[j]:
                DFS_visit(G, j)
        time += 1
        times[i] = time

    def DFS_visit_reverse(G, i):
        nonlocal time
        visited[i] = 1
        belongs_to[i] = skladowe_cnt
        times[i] = -1
        nonlocal visited_cnt
        visited_cnt += 1
        for j in range(n):
            if G[j][i] and not visited[j]:
                DFS_visit_reverse(G, j)

    n = len(G)
    visited = [0 for _ in range(n)]
    times = [-1 for _ in range(n)]
    time = 0
    DFS_visit(G, 0)
    visited = [0 for _ in range(n)]
    m_t = -1
    m_i = -1
    visited_cnt = 0
    skladowe_cnt = 0
    belongs_to = [-1 for _ in range(n)]
    while visited_cnt < n:
        for i in range(n):
            if times[i] > m_t:
                m_t = times[i]
                m_i = i
        m_t = -1
        DFS_visit_reverse(G, m_i)
        skladowe_cnt += 1
    print(belongs_to)
    return belongs_to, skladowe_cnt


def skladowe_graf(G, belongs_to, m):
    def DFS_visit(G, i):
        visited[i] = 1
        for j in range(n):
            if G[i][j] and not visited[j]:
                if belongs_to[i] != belongs_to[j]:
                    n_g[belongs_to[i]].append(belongs_to[j])
                    n_rev[belongs_to[j]].append(belongs_to[i])
                DFS_visit(G, j)

    visited = [0 for _ in range(len(G))]
    n = len(G)
    starters = [0 for _ in range(m)]
    n_g = [[] for _ in range(m)]
    n_rev = [[] for _ in range(m)]
    for i in range(n):
        starters[belongs_to[i]] = i
    for starter in starters:
        print(starter)
        DFS_visit(G, starter)
    to_push = 2
    push_cnt = 0
    for i in range(m):
        if len(n_g[i]) == 0:
            push_cnt += 1
            to_push -= 1
            to_push -= len(n_rev[i])
    print(n_g)
    print(n_rev)
    print(push_cnt)


belongs_to, number = DFS_matrix(_G)
g = skladowe_graf(_G, belongs_to, number)
