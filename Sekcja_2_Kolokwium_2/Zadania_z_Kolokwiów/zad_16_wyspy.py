from queue import Queue
from math import inf

G1 = [
    [0, 5, 1, 8, 0, 0, 0],
    [5, 0, 0, 1, 0, 8, 0],
    [1, 0, 0, 8, 0, 8, 0],
    [8, 1, 8, 0, 5, 0, 1],
    [0, 0, 0, 5, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 5],
    [0, 0, 8, 1, 0, 5, 0]
]


def c(i):
    if i == 1:
        return 0
    elif i == 5:
        return 1
    elif i == 8:
        return 2

def min_not_me(cost, idx, form):
    m_i = 0
    m = 1000000000
    for i in range(3):
        if i != form and m > cost[idx][i]:
            m_i = i
            m = cost[idx][i]
    return m_i


def islands(G, s, f):
    n = len(G)
    costs = [[inf, inf, inf] for _ in range(n)]
    costs[s] = [0, 0, 0]
    queue = Queue()
    queue.put(s)
    while not queue.empty():
        elem = queue.get()
        for i in range(n):
            cst = G[elem][i]
            if cst and costs[i][c(cst)] > cst + costs[elem][min_not_me(costs, elem, c(cst))]:
                costs[i][c(cst)] = cst + min(costs[elem])
                queue.put(i)
    print(costs)
    print(min(costs[f]))


islands(G1, 5, 2)
