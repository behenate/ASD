from random import randint, seed
from time import time


def count_sort(tab, k):
    n = len(tab)
    b = [0]*n
    c = [0]*k

    for elem in tab:
        c[elem] = c[elem]+1
    for i in range(1, k):
        c[i] = c[i] + c[i-1]

    # print(c)
    for k in range(n-1, -1, -1):
        b[c[tab[k]]-1] = tab[k]
        c[tab[k]] = c[tab[k]] - 1
    return b

seed(420)
n = 1000000000

test_tab = [randint(0, n-1) for _ in range(n)]

start = time()
test_tab = count_sort(test_tab, n)
print(time()-start)

