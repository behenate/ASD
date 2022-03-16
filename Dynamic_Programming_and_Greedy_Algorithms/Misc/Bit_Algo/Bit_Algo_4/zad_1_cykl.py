from queue import Queue


def BFS_cykl(G, s):
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
            if visited[neigh] and neigh != parent[elem]:
                return True
            if not visited[neigh]:
                visited[neigh] = True
                distance[neigh] = distance[elem] + 1
                parent[neigh] = elem
                queue.put(neigh)
    return False


def DFS_cykl(G):
    def DFS_visit(G, i):
        nonlocal time
        time += 1
        visited[i] = True
        for neigh in G[i]:
            if visited[neigh] and parent[i] != neigh:
                return True
            if not visited[neigh]:
                parent[neigh] = i
                DFS_visit(G, neigh)
        time += 1
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    time = 0
    for i in range(n):
        if not visited[i]:
            if DFS_visit(G, i):
                return True
    return False



_G = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5, 6], [0, 4], [4, 7], [6]]
_G2 = [[1],[0,2],[1,3],[2]]
a = BFS_cykl(_G, 0)
b = BFS_cykl(_G2, 0)
c = DFS_cykl(_G)
d = DFS_cykl(_G2)
print(a)
print(b)
print(c)
print(d)
