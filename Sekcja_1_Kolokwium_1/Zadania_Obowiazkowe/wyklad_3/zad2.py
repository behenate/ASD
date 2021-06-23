from random import seed, randint, choice
from time import time
from math import log2, floor, inf


def min(n1, n2):
    if n1 < n2:
        return n1
    return n2


def binary_search(tab, elem, p, r):
    # print("Looking for {}, p: {}, r: {}".format(elem,p,r))
    q = (p + r) // 2
    if p >= r and tab[p] != elem:
        return False
    if tab[q] == elem:
        return q
    elif elem < tab[q]:
        return binary_search(tab, elem, p, q - 1)
    else:
        return binary_search(tab, elem, q + 1, r)


def fast_sort(tab, n):
    unique = floor(log2(n))
    num_tab = [inf] * unique
    count_tab = [0] * unique

    for i in range(n):
        q = min(i, unique)

        index = binary_search(num_tab, tab[i], 0, q)
        if index is False:
            index = 0
            while num_tab[index] < tab[i]:
                index += 1
            for j in range(unique - 1, index - 1, -1):
                num_tab[j] = num_tab[j - 1]
                count_tab[j] = count_tab[j - 1]
            num_tab[index] = tab[i]
            count_tab[index] = 1
        else:
            count_tab[index] += 1

    c = 0
    j = 0
    i = 0
    while True:
        if count_tab[j] == 0:
            if j + 1 < unique:
                j += 1
                i += 1
            else:
                break
        tab[c] = num_tab[i]
        count_tab[j] -= 1
        c += 1


n = 20
seed(41)
arr = [choice([0, 12, 32, 13]) for _ in range(n)]
fast_sort(arr, n)
print(arr)
