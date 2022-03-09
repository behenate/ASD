from random import random, seed
from time import time


def insertion_sort(tab):
    for j in range(1, len(tab)):
        key = tab[j]
        i = j-1
        while i >= 0 and tab[i] > key:
            tab[i+1] = tab[i]
            i -= 1
        tab[i + 1] = key


def bucket_sort(tab):
    n = len(tab)
    b = [[] for _ in range(n)]
    print(b)
    for i in range(n):
        b[int(n*tab[i])].append(tab[i])

    for bucket in b:
        insertion_sort(bucket)
    k = 0
    for i in range(n):
        for elem in b[i]:
            tab[k] = elem
            k+=1


seed(420)
n = 100
test_tab = [random() for _ in range(n)]

# print(test_tab)
start = time()
bucket_sort(test_tab)
print(test_tab)
print(time()-start)
