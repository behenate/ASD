from math import inf
from time import time
from random import randint

def merge(tab, p, q, r):
    left = tab[p:q+1]
    right = tab[q+1: r+1]
    left.append(inf)
    right.append(inf)
    i = 0
    j = 0
    for k in range(p, r ):
        if left[i] <= right[j]:
            tab[k] = left[i]
            i += 1
        else:
            tab[k] = right[j]
            j += 1

def find_series(tab):
    q = 0
    prev = -inf
    for elem in tab:
        if elem >= prev:
            prev = elem
            q += 1
        else:
            break
    return q

def merge_series(tab):
    p1=q1=p2=q2=0
    n = len(tab)
    while True:
        q1 = find_series(tab[p1:]) + p1
        p2 = q1
        if q1-p1 == n:
            break
        q2 = find_series(tab[p2:]) + p2
        merge(tab, p1, q1-1, q2)
        p1 = q2
        if q2 == n:
            p1=0
    return tab

start = time()
tab = merge_series([randint(1, 2) for _ in range(100)])
print(time()-start)
print(tab)
print(len(tab))

#  Wydajność gówniana ale nie chce mi się myślec nad lepszą  (☞ﾟヮﾟ)☞  ☜(ﾟヮﾟ☜)
