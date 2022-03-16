# Znajdowanie spójnych składowych i przypisanie nr. spójnej do każdego z wierzchołków
def SCC(G):
    def DFS_visit(G, i):
        nonlocal time
        visited[i] = 1
        for j in range(n):
            if G[i][j] and not visited[j]:
                DFS_visit(G, j)
        times[i] = time
        time += 1

    def DFS_reverse(G, i, cnt):
        visited[i] = cnt
        for j in range(n):
            if G[j][i] and not visited[j]:
                DFS_reverse(G, j, cnt)

    n = len(G)
    visited = [0 for _ in range(n)]
    time = 0
    times = [-1 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            DFS_visit(G, i)

    visited = [0 for _ in range(n)]
    cnt = 1
    for i in range(n):
        s_i = -1
        m_v = -1
        for j in range(n):
            if times[j] > m_v and not visited[j]:
                m_v = times[j]
                s_i = j

        if s_i != -1:
            DFS_reverse(G, s_i, cnt)
            cnt += 1
    for i in range(n):
        visited[i] -= 1
    return visited, cnt - 1


def find_connections(G):
    def recur_connection(vertex):
        # Sprawdzenie czy liczenie jest konieczne
        if recur_visited[vertex]:
            return
        # Wybieram wszystkie składowe połączone ze składową w argumencie
        # Wywołuję dla nich funkcję rekurencyjnie, aby w tablicy res_g miały one już poprawny wynik
        for neigh in cps_G[vertex]:
            recur_connection(neigh)
            # Wybieram połączenia dla dowolnego wierzchołka z danej spójnej składowej i dopisuję je do
            # istniejących połączeń w każdym z wierzchołków spójnej składowej podanej jako argument
            rep = res_g[cps[neigh][0]]
            for i in range(n):
                for elem in cps[vertex]:
                    res_g[elem][i] = rep[i] or res_g[elem][i]
        recur_visited[vertex] = 1

    n = len(G)
    cps_belong, num_cps = SCC(G)  # Lista przynależności każdego z wierzchołków do spójnych składowych
    cps = [[] for _ in range(num_cps)]  # Lista wierzchołków należących do danej spójnej
    cps_G = [[] for _ in range(num_cps)]  # Graf połączeń między spójnymi składowymi
    res_g = [[0 for _ in range(n)] for _ in range(n)]  # wynikowy graf
    recur_visited = [0 for _ in range(num_cps)]
    for i in range(n):
        cps[cps_belong[i]].append(i)
    for i in range(n):
        for j in range(n):
            if G[i][j] and cps_belong[i] != cps_belong[j]:
                cps_G[cps_belong[i]].append(cps_belong[j])
    # Wypełniam połączenia wewnętrzne miedzy spójnymi. Żadne połączenie nie zostanie wpisane więcej niż raz, więc
    # maksymalna złożoność to O(V^2)
    for tup in cps:
        for i in range(len(tup)):
            for j in range(i, len(tup)):
                a = tup[i]
                b = tup[j]
                res_g[a][b] = 1
                res_g[b][a] = 1
    # Wypełniam połączenia zewnętrzne między spójnymi. Algorytm jest dynamiczny więc każde pole obliczy tylko raz
    # O(V^2)
    for i in range(num_cps):
        recur_connection(i)
    # Implementacja staje się dużo prostsza jeżeli założymy że z każdego wierzchołka w spójnej składowej można dotrzeć
    # do samego siebie. Jest to prawdą dla każdej spójnej składowej oprócz takiej o 1 wierzchołku. Dlatego teraz
    # Znajduję takie spójne i usuwam w nich połączenia wierzchołka do samego siebie, chyba że istniało ono w grafie
    # wejściowym
    for group in cps:
        if len(group) == 1:
            if not G[group[0]][group[0]]:
                res_g[group[0]][group[0]] = 0
    print("Graf wynikowy: ")
    for line in res_g:
        print(line)
    return res_g


# Kilka spójnych składowych, rysunek: https://i.imgur.com/1yyyRgt.png
test1 = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]
# Pojedyncze wierzchołki
test2 = [
    [0, 0],
    [1, 0]
]
# Cykl
test3 = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
]
# DAG, rysunek: https://i.imgur.com/YIv4dK4.png
test4 = [
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
# Rozłączne ścieżki
test5 = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
print("TEST1: ")
# Rysunek grafu dla testu 1: https://i.imgur.com/1yyyRgt.png
find_connections(test1)
print("TEST2: ")
find_connections(test2)
print("TEST3: ")
find_connections(test3)
# Rysunek grafu dla testu 4 https://i.imgur.com/YIv4dK4.png
print("TEST4: ")
find_connections(test4)
print("TEST4: ")
find_connections(test5)
