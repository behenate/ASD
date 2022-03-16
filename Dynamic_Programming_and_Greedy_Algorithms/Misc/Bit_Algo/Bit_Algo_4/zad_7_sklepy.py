from queue import Queue


def BFS(G, shops):
    queue = Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    for shop in shops:
        visited[shop] = True
        distance[shop] = 0
        parent[shop] = None
        queue.put(shop)
    while not queue.empty():
        elem = queue.get()
        for neigh in G[elem]:
            if not visited[neigh]:
                visited[neigh] = True
                distance[neigh] = distance[elem] + 1
                parent[neigh] = elem
                queue.put(neigh)
    return visited, distance, parent


_G = [
    [1, 5],
    [5, 4, 2],
    [3, 1],
    [2, 4, 10],
    [8, 5, 1, 3],
    [0, 1, 4, 8, 7],
    [7, 11],
    [5, 8, 12, 6],
    [4, 5, 7, 12, 9],
    [8, 10, 13],
    [3, 9, 14],
    [6],
    [7, 8, 13],
    [12, 9, 14],
    [10, 13, 15],
    [14, 16],
    [15, 17],
    [16]
]

_shops = [7, 3, 16]

a,b,c = BFS(_G, _shops)
print(a,b,c)