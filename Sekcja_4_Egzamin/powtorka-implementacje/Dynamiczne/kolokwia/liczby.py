from math import inf
from queue import PriorityQueue



def dijkstra(G, s):
    n = len(G)
    visited = [0 for _ in range(n)]
    dist = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[s] = 0
    queue = PriorityQueue()
    queue.put((0, s))
    while queue.qsize() > 0:
        dist_to, i = queue.get()
        if visited[i]:
            continue
        visited[i] = 1
        for e in G[i]:
            elem, d = e
            if visited[elem]:
                continue
            if dist_to + d < dist[elem]:
                dist[elem] = dist_to + d
                queue.put((dist[elem], elem))
                parent[elem] = i

    return dist


def find(T, min_idx, max_idx):
    n = len(T)
    T[min_idx], T[0] = T[0], T[min_idx]
    T[max_idx], T[-1] = T[-1], T[max_idx]
    common_digits = [[] for _ in range(10)]
    D = [[] for _ in range(n)]
    for i, num in enumerate(T):
        while num > 0:
            found = [0 for _ in range(10)]
            digit = num % 10
            num //= 10
            if not found[digit]:
                common_digits[digit].append((T[i], i))
    for arr in common_digits:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                d = abs(arr[i][0] - arr[j][0])
                D[arr[i][1]].append((arr[j][1], d))
                D[arr[j][1]].append((arr[i][1], d))
    for line in D:
        print(line)
    distances = dijkstra(D, 0)
    print(distances)


T = [132, 246, 257, 587, 688, 990]
find(T, 0, 5)
