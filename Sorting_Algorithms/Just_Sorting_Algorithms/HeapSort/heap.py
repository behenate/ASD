from random import randint, seed
from time import  time


def max_heapify(tab, i, heap_size):
    l = i * 2 + 1
    r = l + 1
    largest = i
    if l < heap_size and tab[i] < tab[l]:
        largest = l
    if r < heap_size and tab[largest] < tab[r]:
        largest = r
    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        max_heapify(tab, largest, heap_size)


def build_max_heap(tab):
    n = len(tab)
    for i in range(n//2+1, -1, -1):
        max_heapify(tab, i, n)


def heapsort(tab):
    build_max_heap(tab)
    for i in range(len(tab)-1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        max_heapify(tab, 0, i)


seed(420)
n = 10000
test_tab = [randint(1, 10000) for _ in range(n)]

start = time()
heapsort(test_tab)
print(time()-start)
print(test_tab)
