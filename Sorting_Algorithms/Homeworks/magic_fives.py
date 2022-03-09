'''
    Komentarz: Algorytm jest zmodyfikowaną funkcją select(), za każdym rekurencyjnym wywołaniem select, na podanym
    zakresie znajdowana jest mediana median, za pomocą algorytmu "magiczne piątki" która pozwala na optymalny wybór
    punktu podziału w partition, dzięki czemu szanse na przypadek pesymistyczny w podziale znacznie maleją.
    Każdy z pięcio-elementowych podzbiorów jest sortowany algorytmem instertion sort, ponieważ pomimo złożoności n^2
    ma niską stałą dzięki czemu jest wydajny na małych zbiorach liczb.
'''
from random import randint, shuffle, seed


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


# Funkcja partition wykorzystująca podany index jako pivot
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


# Rekurencyjna funkcja znajdowania mediany median
def find_median(tab, p, q):
    sections = 0

    for i in range(p, q+1, 5):
        section_end = custom_min(q, i + 4)
        insertion_sort(tab, i, section_end)
        median_index = i+(section_end-i)//2
        tab[p + ((i - p) // 5)], tab[median_index] = tab[median_index], tab[p + ((i - p) // 5)]
        sections += 1
    # Jeżeli znaleziono więcej niż 5 median to wywołaj rekurencyjnie medianę median
    if sections > 5:
        return find_median(tab, p, p + sections - 1)
    # W przeciwnym wypadku znajdź medianę median
    insertion_sort(tab, p, p + sections - 1)
    pivot_index = p + (sections // 2)
    return pivot_index


# funkcja select() zmodyfikowana o wyszukiwanie punktu podziału dla funkcji partition
def linearselect(A, k, p=None, r=None):
    if p is None:
        p = 0
        r = len(A) - 1

    if p == r:
        return A[p]

    pivot_index = find_median(A, p, r)
    q = partition(A, p, r, pivot_index)

    if q == k:
        return A[q]
    elif q > k:
        return linearselect(A, k, p, q - 1)
    else:
        return linearselect(A, k, q + 1, r)



n = 11
for i in range(n):
    A = list(range(n))
    shuffle(A)
    print(A)
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")

