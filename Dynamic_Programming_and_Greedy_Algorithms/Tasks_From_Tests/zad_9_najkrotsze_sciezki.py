from math import inf
from queue import Queue
def BFS(G, s, t):
    queue = Queue()
    n = len(G)
    distance = [inf for _ in range(n)]
    path_count = [0 for _ in range(n)]
    distance[s] = 0
    path_count[s] = 1
    queue.put(s)
    while not queue.empty():
        elem = queue.get()
        if elem == t:
            break
        for neigh in G[elem]:
            if distance[elem] + 1 < distance[neigh]:
                queue.put(neigh)
            if distance[elem]+1 <= distance[neigh]:
                distance[neigh] = distance[elem] + 1
                path_count[neigh] += path_count[elem]

    print(path_count)
    print(path_count[t])
    return distance

_G=[
    [1,2],
    [0,3,4],
    [0,3,4],
    [1,4,5],
    [2,3,5],
    [3,4]
]
_G1 = [
    [1,2],
    [0,3],
    [0,3,4],
    [1,5,4,2],
    [2,3,6],
    [3,7],
    [4,7],
    [5,6]
]
BFS(_G, 0, 5)
BFS(_G1, 0, 5)