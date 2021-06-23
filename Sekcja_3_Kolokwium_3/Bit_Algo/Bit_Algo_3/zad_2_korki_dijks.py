from math import inf
from queue import PriorityQueue


def dijkstra(T, D, s):
    n = len(T)
    visited = [0 for _ in range(n)]
    time = [inf for _ in range(n)]
    dist = [inf for _ in range(n)]
    time[s] = 0
    dist[s] = 0
    queue = PriorityQueue()
    queue.put((0, 0, s))
    while queue.qsize() > 0:
        time_to, dist_to, i = queue.get()
        if visited[i]:
            continue
        visited[i] = 1
        for j in range(n):
            if T[i][j] == 0:
                continue
            elem, t, d = j, T[i][j], D[i][j]
            if visited[elem]:
                continue
            if time_to + t < time[elem] or (time_to+t == time[elem] and dist_to+d < dist[elem]):
                time[elem] = time_to + t
                dist[elem] = dist_to + d
                queue.put((time[elem], dist[elem], elem))

    return time, dist


def find_distances(T, D):
    n = len(T)
    times = []
    distances = []
    for i in range(n):
        t, d = dijkstra(T, D, i)
        times.append(t)
        distances.append(d)
    for line in times:
        print(line)
    print("")
    for line in distances:
        print(line)


_T = [
    [0, 3, 4, 0, 0, 0],
    [3, 0, 0, 5, 2, 0],
    [4, 0, 0, 0, 3, 0],
    [0, 5, 0, 0, 2, 2],
    [0, 2, 3, 2, 0, 1],
    [0, 0, 0, 2, 1, 0],
]

_D = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 2, 2, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 2, 0, 0, 2, 2],
    [0, 2, 1, 2, 0, 1],
    [0, 0, 0, 2, 1, 0],
]
find_distances(_T, _D)
