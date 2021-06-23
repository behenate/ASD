from queue import Queue


def BFS_matrix(G, s):
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
        for i in range(n):
            if G[elem][i] and not visited[i]:
                visited[i] = True
                distance[i] = distance[elem] + 1
                parent[i] = elem
                queue.put(i)
    return visited, distance, parent


_G = [[False, True, False, True, False, False],
      [False, False, True, False, False, False],
      [False, False, False, True, False, False],
      [False, False, False, False, True, False],
      [False, False, False, False, False, False],
      [False, False, False, False, False, False]
      ]
a, b, c = BFS_matrix(_G, 0)
print(a, b, c)
