"""Zadanie 6. (dwóch kierowców) Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to
miasta a krawędzie to drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrachjako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V , zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy.
Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby
Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak najszybszy (ale przede wszystkim
poprawny). """

from math import inf
from queue import PriorityQueue


def alicja_bob(G, s):
    n = len(G)
    visited = [[0, 0] for _ in range(n)]
    dist = [[inf, inf] for _ in range(n)]
    parent = [[-1, -1] for _ in range(n)]
    dist[s] = [0, 0]
    queue = PriorityQueue()
    # 0 - kierował bob
    # 1 - kierowała alicja
    queue.put((0, s, 0))
    queue.put((0, s, 1))
    while queue.qsize() > 0:
        dist_to, i, driver = queue.get()
        next_driver = int(not bool(driver))
        if visited[i][driver]:
            continue
        visited[i][driver] = 1
        for e in G[i]:
            elem, d = e
            if visited[elem][next_driver]:
                continue
            if dist_to + (d*next_driver) < dist[elem][next_driver]:
                dist[elem][next_driver] = dist_to + d*next_driver
                queue.put((dist[elem][next_driver], elem, next_driver))
                parent[elem][next_driver] = i
    print(dist)


G = [
    [(1, 2), (2, 3)],
    [(0, 2), (2, 8), (3, 4)],
    [(0, 3), (1, 8), (3, 5), (4, 2)],
    [(1, 4), (5, 7), (2, 5)],
    [(2, 2), (6, 6), (5, 3)],
    [(3, 7), (4, 3), (6, 5), (7, 8)],
    [(4, 6), (5, 5), (7, 100)],
    [(5, 8), (6, 100)],
]
alicja_bob(G, 0)

