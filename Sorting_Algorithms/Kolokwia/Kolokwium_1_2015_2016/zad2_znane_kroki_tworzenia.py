"""
    Dana jest n elementowa tablica A zawierająca liczby naturalne (potencjalnie bardzo duże).
    Wiadomo, że tablica A powstała w dwóch krokach. Najpierw wygenerowano losowo (z nieznanym
    rozkładem) n różnych liczn nieparzystych i posortowano je rosnąco. Następnie wybrano losowo
    dlog ne elementów powstałej tablicy i zamieniono je na losowo wybrane liczby parzyste. Proszę
    zaproponować (bez implementacji!) algorytm sortowania tak powstałych danych. Algorytm
    powinien być możliwie jak najszybszy. Proszę oszacować i podać jego złożoność czasową
"""
from random import randint, seed
from math import log2, ceil, floor
from time import time


def partition(tab, p, r):
    last = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= last:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r):
    if p < r:
        i = partition(tab, p, r)
        quicksort(tab, p, i - 1)
        quicksort(tab, i + 1, r)


def merge(original, a, b):
    a_i = 0
    b_i = 0
    i = 0
    while a_i < len(a) and b_i < len(b):
        if a[a_i] <= b[b_i]:
            original[i] = a[a_i]
            a_i += 1
        else:
            original[i] = b[b_i]
            b_i += 1
        i+= 1
    while a_i < len(a):
        original[i] = a[a_i]
        a_i += 1
        i += 1
    while b_i < len(b):
        original[i] = b[b_i]
        b_i += 1
        i += 1


def sort(arr, n):
    even = [0] * (ceil(log2(n)))
    odd = [0] * (len(arr) - ceil(log2(n)))
    e_i = 0
    o_i = 0
    for elem in arr:
        if elem % 2 == 0:
            even[e_i] = elem
            e_i += 1
        else:
            odd[o_i] = elem
            o_i += 1
    quicksort(even, 0, len(even)-1)
    merge(arr, even, odd)


seed(420)
n = 10000000
arr = [randint(0, n // 2) * 2 + 1 for _ in range(n)]
arr = sorted(arr)
for i in range(ceil(log2(n))):
    arr[i * floor(log2(n))] = randint(0, (n // 2)) * 2
print(arr)
print("starting!")
start = time()
sort(arr, n)
print(time()-start)
