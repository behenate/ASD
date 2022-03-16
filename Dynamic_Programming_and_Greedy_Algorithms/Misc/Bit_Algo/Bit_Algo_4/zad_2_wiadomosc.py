from queue import Queue


def BFS(to_convert, n):
    s = 0
    G = [[] for _ in range(n)]
    for p in to_convert:
        G[p[0]].append(p[1])
        G[p[1]].append(p[0])
    queue = Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    passed = [0 for _ in range(n)]
    visited[s] = True
    distance[s] = 0
    queue.put(s)
    while not queue.empty():
        elem = queue.get()
        for neigh in G[elem]:
            if not visited[neigh]:
                visited[neigh] = True
                distance[neigh] = distance[elem] + 1
                passed[distance[neigh]] += 1
                queue.put(neigh)
    m = max(passed)
    for i in range(n):
        if passed[i] == m:
            return i, passed[i]
    # return visited, distance


meh = [[0, 2], [0, 1], [0, 3], [1, 3], [1, 5], [1, 2], [2, 4]]
meh1 = [[0, 1], [1, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 7], [4, 7], [4, 8], [5, 8], [5, 9], [6, 9], [7, 10],
        [8, 10], [9, 10]]

a = BFS(meh, 6)
b = BFS(meh1, 11)
print(a)
print(b)
