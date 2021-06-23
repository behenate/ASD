from random import randint, seed
from time import time


def max_heapify(tab, i, heap_size):
    l = i*2
    r = l+1
    largest = i
    if l <= heap_size and tab[l] > tab[largest]:
        largest = l
    if r <= heap_size and tab[r] > tab[largest]:
        largest = r

    if largest != i:
        tab[largest], tab[i] = tab[i], tab[largest]
        max_heapify(tab, largest, heap_size)


def build_max_heap(tab):
    heap_size = len(tab) - 1
    for i in range(heap_size//2, -1, -1):
        max_heapify(tab, i, heap_size)
    return heap_size


def heapsort(tab):
    heap_size = build_max_heap(tab)
    for i in range(heap_size, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heap_size -= 1
        max_heapify(tab, 0, heap_size)


seed(420)
n = 10
test_tab = [randint(1, 10) for _ in range(n)]
print(test_tab)
start = time()
heapsort(test_tab)
print(time()-start)
print(test_tab)