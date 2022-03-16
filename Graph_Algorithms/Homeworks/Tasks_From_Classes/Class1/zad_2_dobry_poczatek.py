"""Zadanie 2. (dobry początek) Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który
stwierdza czy dany graf zawiera dobry początek."""
def DFS(G):
    def DFS_visit(G, i):
        nonlocal time
        visited[i] = True
        for neigh in G[i]:
            if not visited[neigh]:
                parent[neigh] = i
                DFS_visit(G, neigh)
        visited[i] = time
        time += 1
    n = len(G)
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    time = 0
    for i in range(n):
        if not visited[i]:
            DFS_visit(G, i)
    check_index = -1
    for i in range(n):
        if visited[i] == time - 1:
            check_index = i
            break
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    DFS_visit(G, check_index)
    print(visited, check_index)
    for elem in visited:
        if not elem:
            return False
    return True




_G = [
    [2,1],
    [3],
    [3],
    [],
    [4]
]
a = DFS(_G)
print(a)
