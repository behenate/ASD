from queue import Queue


def mini_BFS(G, s):
    queue = Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited[s] = True
    distance[s] = 0
    queue.put(s)
    while not queue.empty():
        elem = queue.get()
        if distance[elem] < 2:
            for neigh in range(n):
                if not G[elem][neigh]:
                    continue
                if visited[neigh] and neigh != parent[elem] and distance[elem] + distance[neigh] + 1 == 4:
                    print("Found!", distance[elem], distance[neigh], s, parent, neigh)
                    print(elem, neigh, parent[elem], parent[neigh])
                    return True
                if not visited[neigh]:
                    visited[neigh] = True
                    distance[neigh] = distance[elem] + 1
                    parent[neigh] = elem
                    queue.put(neigh)
    return False


def DFS(G):
    n = len(G)
    for i in range(n):
        if mini_BFS(G, i):
            return True
    return False


_G = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0]
]

print(DFS(_G))
