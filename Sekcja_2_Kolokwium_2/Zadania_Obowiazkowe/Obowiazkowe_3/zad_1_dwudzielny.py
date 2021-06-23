from queue import Queue


def BFS(G, s):
    queue = Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    color = [None for _ in range(n)]
    visited[s] = True
    distance[s] = 0
    color[0] = 0
    queue.put(s)
    while not queue.empty():
        elem = queue.get()
        for neigh in G[elem]:
            if color[neigh] == color[elem]:
                return False
            if not visited[neigh]:
                visited[neigh] = True
                distance[neigh] = distance[elem] + 1
                color[neigh] = (color[elem] + 1) % 2
                queue.put(neigh)
    return True
    # return visited, distance, parent


_G = [[1], [2, 4, 0], [1, 3], [2, 4], [3, 1]]
_G1 = [[1, 3], [2], [3], [4], [], []]
_G2 = [[1], [2, 4, 0], [1, 3, 4], [2, 4], [3, 1]]
_G3 = [[3, 4], [4, 5], [3, 5], [0, 2], [0, 1], [1, 2]]
a = BFS(_G, 0)
b = BFS(_G1, 0)
c = BFS(_G2, 0)
d = BFS(_G3, 0)
print(a)
print(b)
print(c)
print(d)
