from zad3testy import runtests
from math import inf
def sum_fuel(G):
    def DFS_visit(G, i, j):
        nonlocal total
        total += G[i][j]
        G[i][j] = 0
        if i-1 >= 0  and G[i-1][j]:
            DFS_visit(G, i-1, j)
        if i+1 < n  and G[i+1][j]:
            DFS_visit(G, i+1, j)
        if j - 1 >= 0 and  G[i][j-1]:
            DFS_visit(G, i, j-1)
        if j + 1 < m and G[i][j + 1]:
            DFS_visit(G, i, j + 1)

    n = len(G)
    m = len(G[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
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
    n = len(T[0])
    possibilities = [[] for _ in range(n)]
    target = n-1
    tank = T[0]
    possibilities[0].append((tank[0], 1))
    prev_found = -1
    for i in range(n):
        print(tank[i])
        if tank[i]:
            min_tank_to_reach = inf
            fuel_to_reach = target - i
            if prev_found != -1:
                for possibility in possibilities[prev_found]:
                    fuel_left = possibility[0] - (i-prev_found)
                    if fuel_left >= 0:
                        possibilities[i].append((fuel_left, possibility[1]))
                        possibilities[i].append((fuel_left+tank[i], possibility[1]+1))
                        if fuel_left+tank[i] >= fuel_to_reach:
                            min_tank_to_reach = min(possibility[1]+1, min_tank_to_reach)
            if min_tank_to_reach != inf:
                print(min_tank_to_reach, "co")
                # return min_tank_to_reach
            prev_found = i
    print(possibilities)
    return min_tank_to_reach

print(plan(map))
# runtests(plan)
