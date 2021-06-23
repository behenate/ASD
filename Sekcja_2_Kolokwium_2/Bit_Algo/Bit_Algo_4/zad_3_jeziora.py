from queue import Queue


def DFS_map(G):
    def DFS_visit(map, i, j, bfs_iter):
        map[i][j] = bfs_iter
        size = 1
        if i - 1 >= 0 and map[i - 1][j] == 0:
            size += DFS_visit(map, i - 1, j, bfs_iter)
        if i + 1 < n and map[i + 1][j] == 0:
            size += DFS_visit(map, i + 1, j, bfs_iter)
        if j - 1 >= 0 and map[i][j - 1] == 0:
            size += DFS_visit(map, i, j - 1, bfs_iter)
        if j + 1 < n and map[i][j + 1] == 0:
            size += DFS_visit(map, i, j + 1, bfs_iter)
        return size

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    time = 0
    lake_cnt = 0
    sizes = []
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                lake_cnt += 1
                sizes.append(DFS_visit(map, i, j, lake_cnt))
    print(max(sizes))
    for line in map:
        print(line)
    return visited, parent, time


def BFS_map(G, s):
    queue = Queue()
    n = len(G)
    parent = [[0 for _ in range(n)] for _ in range(n)]
    parent[0][0] = 0
    queue.put((0, 0))
    map[0][0] = 0
    while not queue.empty():
        elem = queue.get()
        i, j = elem[0], elem[1]
        if i - 1 >= 0 and map[i - 1][j] == -1:
            map[i - 1][j] = map[i][j] + 1
            queue.put((i - 1, j))
        if i + 1 < n and map[i + 1][j] == -1:
            map[i + 1][j] = map[i][j] + 1
            queue.put((i + 1, j))
        if j - 1 >= 0 and map[i][j - 1] == -1:
            map[i][j - 1] = map[i][j] + 1
            queue.put((i, j - 1))
        if j + 1 < n and map[i][j + 1] == -1:
            map[i][j + 1] = map[i][j] + 1
            queue.put((i, j + 1))
    map[0][0] = 0
    for line in parent:
        print(line)
    p = map[n - 1][n - 1]
    path = []
    i = n - 1
    j = n - 1
    for line in map:
        print(line)

    while p != 0:
        path.append((i,j))
        # print(p, i, j)
        if i - 1 >= 0 and map[i - 1][j] == p - 1:
            p = map[i - 1][j]
            i -= 1
        if i + 1 < n and map[i + 1][j] == p - 1:
            p = map[i + 1][j]
            i += 1
        if j - 1 >= 0 and map[i][j - 1] == p - 1:
            p = map[i][j - 1]
            j -= 1
        if j + 1 < n and map[i][j + 1] == p - 1:
            p = map[i][j + 1]
            j += 1
    print((0,0))
    for i in range(len(path)):
        print(path[len(path) - i - 1])
    # while


map = [
    [-1, 0, -1, -1, -1, -1, -1, -1],
    [-1, 0, -1, 0, 0, -1, -1, -1],
    [-1, -1, -1, 0, 0, -1, 0, -1],
    [-1, 0, 0, 0, 0, -1, 0, -1],
    [-1, -1, 0, 0, -1, -1, -1, -1],
    [-1, 0, -1, -1, -1, -1, 0, 0],
    [0, 0, -1, 0, 0, -1, 0, -1],
    [-1, -1, -1, 0, -1, -1, -1, -1],
]
DFS_map(map)
print("")
print("")
print("")
for i in range(len(map)):
    for j in range(len(map)):
        if map[i][j] != -1:
            map[i][j] = -1000
BFS_map(map, 0)
