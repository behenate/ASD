from zad3testy import runtests
from math import inf
# Zliczane są wielkości plam i wpisywane w pierwszy rząd macierzy.
# Następnie rekurencyjna funkcja f(i,j) - minimalna liczba tankowań by dojechać na j z i paliwa jest używana do
# Wypełnienia macierzy. Wynik znajduje się w ostatniej kolumnie macierzy.
# Następnie funkcja używająca informacji o tym na jakiej stacji ostatni raz tankowaliśmy na danej pozycji zwraca ciąg
# Stacji
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
    all_fuel = 0
    target = n-1
    tank = T[0]
    for i in range(n):
        all_fuel += tank[i]
    F = [[inf for _ in range(n)] for _ in range(all_fuel+1)]
    H = [[inf for _ in range(n)] for _ in range(all_fuel + 1)]
    F[tank[0]][0] = 1
    H[tank[0]][0] = 0
    min_cost_target = (inf, inf)
    for i in range(1, n):
        for j in range(1, all_fuel):
            min_cost = F[j+1][i-1]
            if min_cost < F[j][i]:
                H[j][i] = H[j + 1][i - 1]
            F[j][i] = min(F[j][i], min_cost)

            if tank[i] and min_cost != inf:
                for k in range(1, tank[i]+1):
                    if i+k < n:
                        F[j+tank[i]-k][i+k] = min(F[j+tank[i]-k][i+k], min_cost+1)
                        H[j+tank[i]-k][i+k] = i
    min_tanks = 99999999999999
    min_i = -1
    for i in range(all_fuel + 1):
        if F[i][n-1] < min_tanks:
            min_tanks = F[i][n-1]
            min_i = i
    # for line in H:
    #     print(line)
    # for line in F:
    #     print(line)
    i = min_i
    j = n-1
    st = H[i][j]
    res = []
    while st != inf:
        res.append(st)
        dist = j - st
        i = (i+dist) - tank[st]
        st = H[i][st]
        j = j-st
    # Na pewno tankowano na stacji 0
    res.append(0)
    res.reverse()
    return res


# print(plan(map))
runtests(plan)
