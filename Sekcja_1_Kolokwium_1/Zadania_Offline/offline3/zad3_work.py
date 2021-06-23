from random import randint, shuffle, seed
from time import time


# Żeby nie używać min(), nie jestem pewien czy jest dozwolony czy nie ¯\_(ツ)_/¯
def custom_min(a, b):
    if a < b:
        return a
    return b


def insertion_sort(tab, p, r):
    for j in range(p+1, r+1):
        key = tab[j]
        i = j-1
        while i >= p and tab[i] > key:
            tab[i+1] = tab[i]
            i -= 1
        tab[i+1] = key


def partition(tab, p, r, custom_pivot=None):
    if custom_pivot is not None:
        tab[r], tab[custom_pivot] = tab[custom_pivot], tab[r]
    pivot = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] < pivot:
            i = i + 1
            tab[j], tab[i] = tab[i], tab[j]
    tab[r], tab[i + 1] = tab[i + 1], tab[r]
    return i + 1


def find_median(tab, p, q):
    sections = 0

    for i in range(p, q, 5):
        section_end = custom_min(q, i + 4)
        insertion_sort(tab, i, section_end)
        median_index = i+(section_end-i)//2
        tab[p + ((i - p) // 5)], tab[median_index] = tab[median_index], tab[p + ((i - p) // 5)]
        sections += 1

    if sections > 5:
        return find_median(tab, p, p + sections - 1)

    insertion_sort(tab, p, p + sections - 1)
    pivot_index = p + (sections // 2)
    return pivot_index


def linearselect(tab, k, p=None, r=None):
    if p is None:
        p = 0
        r = len(tab) - 1
    if p == r:
        return tab[p]
    pivot_index = find_median(tab, p, r)
    q = partition(tab, p, r, pivot_index)
    if q == k:
        return tab[q]
    elif q > k:
        return linearselect(tab, k, p, q - 1)
    else:
        return linearselect(tab, k, q + 1, r)


seed(42)
n=11
start = time()
for i in range(n):
    A = list(range(n))
    shuffle(A)
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i, "Wynik: ", x)
        exit(0)
print(time() - start)
print("OK")
