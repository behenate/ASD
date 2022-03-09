"""
Proszę zaproponować i zaimplementować algorytm, który mając na wejściu tablicę A zwraca
liczbę jej inwersji (t.j., liczbę par indeksów i < j takich, że A[i] > A[j].
"""
from math import inf


def merge(tab, p, q, r):
    left = tab[p:q+1]
    right = tab[q+1:r+1]
    left.append(inf)
    right.append(inf)
    i = 0
    j = 0
    inversions = 0
    for k in range(p, r+1):
        if left[i] <= right[j]:
            tab[k] = left[i]
            i += 1
        else:
            tab[k] = right[j]
            j += 1
            inversions += (q-i-p + 1)
    return inversions


def merge_sort(tab, p, r):
    inversions = 0
    center = (p+r)//2
    if p < r:
        inversions += merge_sort(tab, p, center)
        inversions += merge_sort(tab, center+1, r)
        inversions += merge(tab, p, center, r)
    return inversions


arr = [1, 20, 6, 4, 5, 1]
print(arr)
print(merge_sort(arr, 0, len(arr)-1))

