from random import randint, seed
from time import time
import sys


def partition(tab, p, r):
    i = randint(p, r)
    tab[r], tab[i] = tab[i], tab[r]
    last = tab[r]
    i = p-1
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

n = 100000
seed(420)
T = [randint(1, 10) for i in range(n)]
# print("przed sortowaniem: T =", T)
start = time()
quicksort(T, 0, len(T) - 1)
print(time() - start)
# print("po sortowaniu    : T =", T)
for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()
print("OK")
