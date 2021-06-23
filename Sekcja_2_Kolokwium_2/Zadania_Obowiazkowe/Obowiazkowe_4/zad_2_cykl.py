from queue import Queue

_G = [
    [1],
    [0, 2],
    [1, 8, 3],
    [2, 5, 4],
    [3, 6, 5],
    [3, 4, 6, 7],
    [4, 5, 7],
    [5, 6, 9],
    [2, 9],
    [8, 7]
]

def mini_BFS(G, s, idx_parent):
    queue = Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    parent[s] = idx_parent
    visited[s] = True
    distance[s] = 0
    parent[s] = None
    queue.put(s)
    _G.append([n-2])
    while not queue.empty():
        elem = queue.get()
        if distance[elem] < 2:
            for neigh in G[elem]:
                if visited[neigh] and neigh != parent[elem] and distance[elem] + distance[neigh] + 1 == 4 :
                    print("Found!", distance[elem], distance[neigh], s)
                    return True
                if not visited[neigh]:
                    visited[neigh] = True
                    distance[neigh] = distance[elem] + 1
                    parent[neigh] = elem
                    queue.put(neigh)
    return False

def DFS(G):
    def DFS_visit(G, i):
        visited[i] = True
        if len(G[i]) > 2:
            if mini_BFS(G,i, parent[i]):
                return True
            print("mini BFS for:{}!". format(i))
        for neigh in G[i]:
            if not visited[neigh]:
                parent[neigh] = i
                DFS_visit(G, neigh)
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            if DFS_visit(G, i):
                return True
    return False


print(DFS(_G))

