"""Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć grupę K turystów z
miasta A do miasta B. Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o
różnej pojemności. Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
jeździ autobus o pojemności c pasażerów.
Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
(najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
dostali się z A do B."""
from queue import PriorityQueue
from math import inf
def highest_bandwidth(G, s, t):
    n = len(_G)
    bandwidth = [0 for _ in range(n)]
    visited = [0 for _ in range(n)]
    queue = PriorityQueue()
    queue.put((-inf, s))
    while not queue.empty():
        bw, elem = queue.get()
        if visited[elem]:
            continue
        bw = -bw
        bandwidth[elem] = bw
        visited[elem] = 1
        print(visited)
        for tup in G[elem]:
            neigh, weight = tup
            bw_cand = min(weight, bw)
            if not visited[neigh] and bw_cand > bandwidth[neigh]:
                queue.put((-bw_cand, neigh))
                bandwidth[neigh] = bw_cand
    print(bandwidth[t])
#     Tablica parentów, podzielić ilość ludzi przez przepustowość ...

_G = [
    [(1, 10), (2, 12)],
    [(0, 10), (3, 5), (4, 4)],
    [(0, 12), (5, 8), ],
    [(1, 10), (4, 3), (5, 5)],
    [(1, 10), (3, 3), (6, 6)],
    [(2, 8), (3, 5), (6, 5)],
    [(5, 8), (4, 6)]
]
highest_bandwidth(_G, 0, 6)

