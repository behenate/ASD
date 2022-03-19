from math import log, pow
import random


def insertion_sort(tab, a):
    for j in range(1, len(tab)):
        key = tab[j]
        i = j - 1
        while i >= 0 and log(tab[i], a) > log(key, a):
            tab[i + 1] = tab[i]
            i -= 1
        tab[i + 1] = key


def fast_sort(tab, a):
    n = len(tab)
    b = [[] for _ in range(n)]
    for i in range(n):
        bucket = int(n * log(tab[i], a))
        if bucket == n:
            bucket = n-1
        b[bucket].append(tab[i])
    for bucket in b:
        insertion_sort(bucket, a)
    k = 0
    for i in range(n):
        for elem in b[i]:
            tab[k] = elem
            k += 1
    return tab

from math import pow
import random
def gen_test(a):
    T = [pow(a, random.uniform(0,1)) for _ in range(1000)]
    print(T)
    res = fast_sort(T, a)
    print(res)
    for i in range(1, 1000):
        if res[i-1] > res[i]:
            print("Błąd")
            exit()
    print("OK")
gen_test(2)