from queue import Queue

def find_path(G, s, t):
    queue = Queue()
    n = len(G)
    for vertex in G:
        for pair in vertex:
            pair.append(0)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited[s] = True
    distance[s] = 0
    parent[s] = None
    queue.put(s)
    while not queue.empty():
        elem = queue.get()
        for i in range(len(G[elem])):
            neigh = G[elem][i][0]
            dist = G[elem][i][1]
            if not visited[neigh] and dist == 1:
                visited[neigh] = True
                distance[neigh] = distance[elem] + 1 + G[elem][i][2]
                parent[neigh] = elem
                queue.put(neigh)
            elif dist > 1:
                G[elem][i][2] += 1
                G[elem][i][1] -= 1
                queue.put(elem)
    print(distance[t])
    print(distance, parent)
    return visited, distance, parent


_G = [[[1, 4], [2, 3]], [[0, 4], [3, 2]], [[0, 3], [4, 4]], [[1, 2], [5, 1]], [[2, 4], [5, 1]], [[4, 1], [3, 1]]]
find_path(_G, 0, 5)



