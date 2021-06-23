from zad2testy import runtests
from queue import Queue
# Wojciech Dróżdż
# Funkcja wykonuje BFS uzyskjąc najkrótszą ścieżkę. Zapisuje znalezioną ścieżkę. Następnie próbuje usunąć każdą po kolei
# krawędź z tej ścieżki. BFS uruchamiany jest ponownie, jeżeli znaleziona ścieżka jest dłuższa, to zwracana jest krotka
# z wynikiem. Jeżeli nie, przywracana jest krawędź, i usuwana inna.
# To że nie znaleziono ścieżki nic nie znaczy. Jeżeli sprawdzono wszystkie usunięcia i nie znaleziono
# dłuższej to znaczy że takowa nie istnieje, zwracana jest wartość none.
# Złożoność pesymistyczna (cały graf to najdłuższa ścieżka): O(V+E)*V


def BFS(G, s):
    queue = Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited[s] = True
    distance[s] = 0
    parent[s] = None
    queue.put(s)
    while not queue.empty():
        elem = queue.get()
        for neigh in G[elem]:
            if not visited[neigh]:
                visited[neigh] = True
                distance[neigh] = distance[elem] + 1
                parent[neigh] = elem
                queue.put(neigh)

    return visited, distance, parent


def remove_krawedz(G, i, j):
    # i <--> j
    idx_i = -1
    idx_j = -1
    for k in range(len(G[i])):
        if G[i][k] == j:
            idx_i = k

    for k in range(len(G[j])):
        if G[j][k] == i:
            idx_j = k
    G[i].pop(idx_i)
    G[j].pop(idx_j)


def enlarge(G, s, t):
    visited, distance, parent = BFS(G, s)
    line = []
    i = t

    while parent[i] is not None:
        line.append(i)
        i = parent[i]
    line.append(i)
    line.reverse()
    if distance[t] == -1:
        return None
    for i in range(len(line) - 1):
        # Tymczasowo usuń krawędź
        remove_krawedz(G, line[i], line[i + 1])
        v1, d1, p1 = BFS(G, s)
        if d1[t] > distance[t]:
            return (line[i], line[i + 1])
        # przywróć krawędź
        G[line[i]].append(line[i + 1])
        G[line[i + 1]].append(line[i])
    # Jeżeli nie zwrócono wcześniej, zwróć none
    return None


runtests( enlarge )

