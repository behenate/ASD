"""
Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta
przyjmuje na wejściu dwie n
2
-elementowe tablice (A i B) i zapisuje w tablicy B taką permutację
elementów z A, że:
Sumy grup elementów tablicy po n elementów są posortowane 
Proszę zaimplementować funkcję SumSort tak, by działała możliwie jak najszybciej. Proszę
oszacować i podać jej złożoność czasową.
"""

from random import randint, seed


def partition(tab, p, r):
    pivot = tab[r][0]
    i = p-1
    for j in range(p, r):
        if tab[j][0] < pivot:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[r], tab[i+1] = tab[i+1], tab[r]
    return i+1

def quicksort(tab, p, r):
    if p < r:
        q = partition(tab, p, r)
        quicksort(tab, p, q-1)
        quicksort(tab, q+1, r)

def sum_sort(tab_a, tab_b, n):
    n_sq = len(tab_a)
    sum_insert_index = n_sq-1
    for i in range(0, n_sq, n):
        s = 0
        for j in range(i, i+n):
            s += tab_a[j]
        tab_b[sum_insert_index] = (s, i)
        sum_insert_index -= 1
    sum_insert_index += 1
    quicksort(tab_b, sum_insert_index,n_sq-1)

    c = 0
    print(tab_b)
    for i in range(sum_insert_index, n_sq):
        for j in range(n):
            tab_b[c] = tab_a[tab_b[i][1] + j]
            c += 1
    print(tab_b)


seed(42)
s_n = 5
t1 = [randint(1, 10) for _ in range(s_n**2)]
t2 = [0 for _ in range(s_n**2)]

sum_sort(t1, t2, s_n)
print(t2)
