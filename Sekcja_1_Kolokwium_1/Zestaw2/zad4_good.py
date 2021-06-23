"""
Zadanie 4. (Pojemniki z wodą) Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami.
Pojemniki maja kształty prostokątów, rury nie maja objętości (powierzchni). Każdy pojemnik opisany jest
przez współrzędne lewego górnego rogu i prawego dolnego rogu.
Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda rurami spłynęła do najniźszych
pojemników). Proszę zaproponować algorytm Obliczający ile pojemników zostało w pełni zalanych.
"""


def partition_tuple(tab, p, r, idx):
    last = tab[r][idx]
    i = p - 1
    for j in range(p, r):
        if tab[j][idx] <= last:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort_tuple(tab, p, r, idx):
    if p < r:
        i = partition_tuple(tab, p, r, idx)
        quicksort_tuple(tab, p, i - 1, idx)
        quicksort_tuple(tab, i + 1, r, idx)


def fill_containers(containers, water):
    n = len(containers)
    start = [containers[i] for i in range(n)]
    end = [containers[i] for i in range(n)]
    quicksort_tuple(start, 0, n-1, 0)
    quicksort_tuple(end, 0, n-1, 1)
    for ctr in end:
        _water = water
        i = 0

cts = [(2, 7, 3), (0, 3, 1), (3, 6, 2), (1, 3, 2)]
fill_containers(cts)

