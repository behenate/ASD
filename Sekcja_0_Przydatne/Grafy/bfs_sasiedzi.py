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
    return visited, distance, parent

_G = [[1,3], [2], [3], [4], [], []]
a, b, c = BFS(_G, 0)
print(a, b, c)
