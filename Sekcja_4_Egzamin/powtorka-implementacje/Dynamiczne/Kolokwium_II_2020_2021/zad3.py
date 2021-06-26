from zad3testy import runtests
from queue import PriorityQueue
def sum_fuel(G):
    def DFS_visit(G, i, j):
        nonlocal total
        total += G[i][j]
        G[i][j] = 0
        if i-1 >= 0 and G[i-1][j]:
            DFS_visit(G, i-1, j)
        if i+1 < n and G[i+1][j]:
            DFS_visit(G, i+1, j)
        if j - 1 >= 0 and G[i][j-1]:
            DFS_visit(G, i, j-1)
        if j + 1 < m and G[i][j + 1]:
            DFS_visit(G, i, j + 1)

    n = len(G)
    m = len(G[0])
    total = 0
    for start in range(m):
        if G[0][start]:
            DFS_visit(G, 0, start)
            G[0][start] = total
            total = 0



map = [
    [3, 0, 0, 1, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0]
]


def plan(T):

    sum_fuel(T)
    T = T[0]
    n = len(T)
    fuel = 0
    queue = PriorityQueue()
    queue.put((-T[0],0))
    tank_at = []
    while (not queue.empty()) and fuel < n-1:
        to_add, index = queue.get()
        to_add = -to_add
        for i in range(fuel+1, min(fuel+to_add+1, n)):
            if T[i] != 0:
                queue.put((-T[i], i))
        fuel += to_add
        tank_at.append(index)
    return sorted(tank_at)



runtests(plan)
plan(map)