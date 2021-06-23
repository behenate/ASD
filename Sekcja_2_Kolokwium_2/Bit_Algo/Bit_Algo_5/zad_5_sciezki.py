from queue import Queue


def BFS(G, s, t):
    queue = Queue()
    n = len(G)
    parent = [None for _ in range(n)]
    values = [0 for _ in range(n)]
    values[0] = 1
    parent[s] = None
    queue.put(s)
    while not queue.empty():
        elem = queue.get()
        if elem != t:
            for neigh in G[elem]:
                parent[neigh] = elem
                values[neigh] += values[elem]
                queue.put(neigh)
            values[elem] = 0
    print(values)
    return values[t]


_G = [
    [1, 2, 3],
    [3],
    [3, 4, ],
    [5],
    [3, 5],
    [],
]
BFS(_G, 0, 5)
