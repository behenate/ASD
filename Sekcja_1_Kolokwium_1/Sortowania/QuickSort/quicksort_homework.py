from random import randint, seed
from time import time
import sys


def median(e1,i1,e2,i2,e3,i3):
    if e1 < e2 < e3 or e3 < e2 < e1:
        return i2
    elif e2 < e1 < e3 or e3 < e1 < e2:
        return i1
    else:
        return i3

def partition(tab, p, r):
    p_i = median(tab[p], p, tab[(p+r)//2], (p+r)//2, tab[r], r)
    print(tab[p:r])
    tab[p_i], tab[r] = tab[r], tab[p_i]
    pivot = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= pivot:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r):
    while p < r:
        q = partition(tab, p, r)
        if q - p < r - q:
            quicksort(tab, p, q - 1)
            p = q + 1
        else:
            quicksort(tab, q + 1, r)
            r = q - 1


n = 1000000
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
