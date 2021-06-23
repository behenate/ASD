from queue import PriorityQueue
from math import inf
_G = [
    [(1, 3), (2, 5)],
    [(0, 3), (4, 6)],
    [(0, 5), (3, 1)],
    [(2, 1), (4, 1)],
    [(3, 1), (1, 6)],
]
_prices = [3, 1, 2, 1, 5]


def find_path(G, prices, d, s,t):
    n = len(G)
    queue = PriorityQueue()
    costs = [[inf for _ in range(d+1)] for _ in range(n)]
    visited = [[0 for _ in range(d+1)] for _ in range(n)]
    costs[s][0] = 0
    queue.put((0, s, 0))
    while not queue.empty():
        cost, i, j = queue.get()
        if visited[i][j]:
            continue
        visited[i][j] = 1
        costs[i][j] = cost
        if j+1 <= d and costs[i][j] + prices[i] < costs[i][j+1]:
            queue.put((costs[i][j]+prices[i], i, j+1))
            costs[i][j+1] = costs[i][j]+prices[i]
        for tup in G[i]:
            neigh, dist = tup
            if j >= dist and not visited[neigh][j-dist] and costs[i][j] < costs[neigh][j-dist]:
                costs[neigh][j - dist] = costs[i][j]
                queue.put((costs[i][j], neigh, j-dist))
    print(costs)

find_path(_G, _prices, 6, 0, 4)