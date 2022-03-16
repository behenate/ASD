from queue import Queue


def BFS(G, s):
    queue = Queue()
    n = len(G)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    degrees = [0 for _ in range(n)]
    queue.put(s)
    while not queue.empty():
        elem = queue.get()
        for neigh in G[elem]:
            if not visited[neigh][elem]:
                visited[neigh][elem] = True
                degrees[neigh] += 1
                queue.put(neigh)

    print(degrees)
    for i in range(len(degrees)):
        if degrees[i] != len(G[i]):
            return False
    return True


_G = [
    [1, 4],
    [4, 2, 0],
    [1, 3],
    [2, 4],
    [0, 1, 3]
]
_G2 = [
    [1],
    [2],
    [0]
]

print(BFS(_G2, 0))
