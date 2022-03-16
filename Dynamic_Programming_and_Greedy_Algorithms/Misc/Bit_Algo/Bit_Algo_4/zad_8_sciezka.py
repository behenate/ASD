def list_to_neigh(edges, directional=False):
    n = len(edges)
    max_e = edges[0][1]
    for i in range(n):
        max_e = max(max_e, edges[i][1])
    neigh = [[] for _ in range(max_e+1)]
    for i in range(n):
        neigh[edges[i][0]].append(edges[i][1])
        if not directional:
            neigh[edges[i][1]].append(edges[i][0])
    return neigh


def DFS(G, s_i):
    def DFS_visit(G, i):
        visited[i] = True
        for neigh in G[i]:
            if not visited[neigh]:
                dist[neigh] = dist[i] + 1
                DFS_visit(G, neigh)
    n = len(G)
    dist = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    DFS_visit(G, s_i)
    return dist


def find_longest(G):
    n = len(G)
    dist = DFS(G, 0)
    m_d = 0
    m_d_i = 0
    for i in range(n):
        if dist[i] > m_d:
            m_d = dist[i]
            m_d_i = i
    dist = DFS(G, m_d_i)
    print(max(dist))
tree = [
    [0, 1],
    [0, 2],
    [0, 3],
    [3, 4],
    [3, 5],
    [5, 7],
    [7, 9],
    [7, 10],
    [4, 6],
    [6, 8]
]

_G = list_to_neigh(tree)
find_longest(_G)