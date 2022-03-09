from random import randint, seed
from math import inf


def merge(tab, p, q, r):
    left = tab[p:q + 1]
    right = tab[q + 1:r + 1]
    # Dodanie wartownika na koniec listy
    left.append(inf)
    right.append(inf)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            tab[k] = left[i]
            i += 1
        else:
            tab[k] = right[j]
            j += 1


def mergesort(T, p=0, r=None):
    if r is None:
        r = len(T) - 1
    if p < r:
        center = (p + r) // 2
        mergesort(T, p, center)
        mergesort(T, center + 1, r)
        merge(T, p, center, r)
    return T
