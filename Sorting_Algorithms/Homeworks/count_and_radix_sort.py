"""
Algorytm wykorzystujący do sortowania radix sort po wcześniejszym częściowym sortowaniu countsotem
"""

from random import randint, seed
from time import time


def count_sort(tab, iteration=0):
    n = len(tab)
    b = [0]*n
    c = [0]*n
    for i in range(n):
        if iteration == 0:
            c[tab[i] % n] += 1
        else:
            c[tab[i] // n] += 1
    for i in range(1, n):
        c[i] += c[i-1]
    for i in range(n-1, -1,-1):
        if iteration == 0:
            c[tab[i] % n] -= 1
            b[c[tab[i] % n]] = tab[i]

        else:
            c[tab[i] // n] -= 1
            b[c[tab[i] //n]] = tab[i]

    return b


def sort_radix(tab):
    return count_sort(count_sort(tab,0),1)


seed(420)
n = 1000000

to_sort = [randint(0, n**2-1) for _ in range(n)]
start = time()
sorted = sort_radix(to_sort)
print(time()-start)
print(sorted[0:1000])
