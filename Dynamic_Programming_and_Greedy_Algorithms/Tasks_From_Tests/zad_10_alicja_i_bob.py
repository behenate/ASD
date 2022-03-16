"""
Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to
drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba
naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V ,
zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje kto
prowadzi pierwszy. Proszę zaproponować algorytm, który wskazuje taką trasę (oraz osobę, która
ma prowadzić pierwsza), żeby Alicja przejechała jak najmniej kilometrów. Algorytm powinien
być jak najszybszy (ale przede wszystkim poprawny). Proszę oszacować złożoność
zaproponowanego algorytmu, zakładając, że graf jest reprezentowany macierzowo"""
from queue import Queue
from math import inf


def BFS(G, s):
    queue = Queue()
    n = len(G)
    distances = [
        [inf for _ in range(n)],
        [inf for _ in range(n)]
    ]
    paths = [
        [inf for _ in range(n)],
        [inf for _ in range(n)]
    ]
    distances[0][0] = 0
    distances[1][0] = 0
    # index, czy alicja jedzie następna
    # queue.put((s, True))
    queue.put((s, 0))
    while not queue.empty():
        elem, driver = queue.get()
        driver_in_next = not driver
        for i in range(n):
            neigh = i
            ile_alicja = G[elem][neigh] * driver
            if G[elem][i] and distances[driver][elem] + ile_alicja < distances[driver_in_next][neigh]:
                paths[driver_in_next][neigh] = (elem, driver)
                distances[driver_in_next][neigh] = distances[driver][elem] + ile_alicja
                queue.put((neigh, driver_in_next))
    print(distances)
    print(paths)


_G = [
    [0, 10, 0, 0, 10, 0, 0, 0],
    [10, 0, 15, 0, 0, 0, 0, 0],
    [0, 15, 0, 20, 0, 10, 15, 0],
    [0, 0, 20, 0, 0, 0, 0, 10],
    [10, 0, 0, 0, 0, 5, 0, 0],
    [0, 0, 10, 0, 5, 0, 20, 0],
    [0, 0, 15, 0, 0, 20, 0, 30],
    [0, 0, 0, 10, 0, 0, 30, 0]
]
BFS(_G, 0)
