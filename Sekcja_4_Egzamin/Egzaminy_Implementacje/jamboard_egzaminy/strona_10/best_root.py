from queue import Queue
def BFS(G, s):
    queue = Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited[s] = True
    distance[s] = 0
    parent[s] = None
    queue.put(s)
    while not queue.empty():
        elem = queue.get()
        for neigh in G[elem]:
            if not visited[neigh]:
                visited[neigh] = True
                distance[neigh] = distance[elem] + 1
                parent[neigh] = elem
                queue.put(neigh)
    return distance, parent


def best_root(G):
    d1, p1= BFS(G, 0)
    m_d = 0
    m_d_i = -1
    for i in range(len(d1)):
        if d1[i] > m_d:
            m_d = d1[i]
            m_d_i = i
    d2, p2 = BFS(G, m_d_i)
    m_d = 0
    m_d_i = -1
    for i in range(len(d2)):
        if d2[i] > m_d:
            m_d = d2[i]
            m_d_i = i
    res = m_d_i
    for i in range(m_d // 2):
        res = p2[res]
    print(res)


_G = [
    [2],
    [2],
    [0, 1, 3],
    [2, 4],
    [3, 5, 6],
    [4, ],
    [4],
]
best_root(_G)