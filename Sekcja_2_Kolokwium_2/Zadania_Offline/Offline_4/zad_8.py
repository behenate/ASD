from copy import deepcopy
import sys

# Z postaci macierzowej wytwórz listę sąsiedztwa wraz z listą wykorzystywaną przy usuwaniu indeksów
# O((n/2)^2), potencjalnie 2*O(n^2) pamięci dla grafu pełnego. Średnio znacznie mniej.
def matrix_to_adj(matrix):
    n = len(matrix)
    adj_g = [[] for _ in range(n)]
    rm_g = [[] for _ in range(n)]

    can_do = True
    for i in range(n-1, -1, -1):
        for j in range(i, -1, -1):
            if matrix[i][j]:
                rm_g[i].append(len(adj_g[j]))
                rm_g[j].append(len(adj_g[i]))
                adj_g[i].append(j)
                adj_g[j].append(i)
    degrees = [0 for _ in range(n)]
    for i in range(n):
        o = len(adj_g[i])
        degrees[i] = o
        if o % 2 != 0:
            can_do = False
    return adj_g, rm_g, degrees, can_do


def euler(G):
    def DFS_visit(G, i, f):
        if parent[i] != -1:
            degrees[i] -= 1
            degrees[parent[i]] -= 1
            a = parent[i]
            print("remove:", a, i)
            G[a][f] = -1
            G[i][r_g[a][f]] = -1
        stack.append(i)
        for k in range(len(G[i])-1, -1, -1):
            neigh = G[i][k]
            if neigh != -1:
                parent[neigh] = i
                DFS_visit(G, neigh, k)
        cycle.append(stack.pop())

    n_g, r_g, degrees, can_do = matrix_to_adj(G)
    print(n_g)
    print(r_g)
    if not can_do:
        return None
    n = len(G)
    parent = [-1 for _ in range(n)]
    stack = []
    cycle = []
    DFS_visit(n_g, 0, -1)
    return cycle


G1 = [[0,1,1,0,0,0],
     [1,0,1,1,0,1],
     [1,1,0,0,1,1],
     [0,1,0,0,0,1],
     [0,0,1,0,0,1],
     [0,1,1,1,1,0]]

# n = 201
# G1 = [[1 for _ in range(n)]for i in range(n)]
# for i in range(n):
#     G1[i][i] = 0

print(euler(G1))

GG = deepcopy(G1)
cycle = euler(G1)
print(cycle)
if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == False:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == True:
            print("Błąd (3)!")
            exit(0)

print("OK")


