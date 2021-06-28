from math import dist, inf


def max_heapify(tab, i, heap_size, D):
    l = i * 2 + 1
    r = l + 1
    largest = i
    if l < heap_size and D[i] < D[l]:
        largest = l
    if r < heap_size and D[largest] < D[r]:
        largest = r
    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        D[i], D[largest] = D[largest], D[i]
        max_heapify(tab, largest, heap_size, D)


def build_max_heap(tab, D):
    n = len(tab)
    for i in range(n // 2 + 1, -1, -1):
        max_heapify(tab, i, n, D)


def heapsort(tab, D):
    build_max_heap(tab, D)
    for i in range(len(tab) - 1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        D[0], D[i] = D[i], D[0]
        max_heapify(tab, 0, i, D)


def sort_points(P):
    n = len(P)
    indxs = [_ for _ in range(n)]
    D = [inf for _ in range(n)]

    for i in range(n):
        D[i] = dist((0, 0), P[i])
    heapsort(indxs, D)
    res = [P[indxs[i]] for i in range(n)]
    print(res)
points = [
    [1, 5],
    [1, 1],
    [5, 4],
    [4, 4],
    [4, 1],
    [8, 8],
]

sort_points(points)
