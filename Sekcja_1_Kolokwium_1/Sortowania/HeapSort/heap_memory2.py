from random import randint, seed
from time import time
import sys


def max_heapify(tab, i, heap_size):
    l = 2*i
    r = l+1
    largest = i
    if l < heap_size and tab[l] > tab[largest]:
        largest = l
    if r < heap_size and tab[r] > tab[largest]:
        largest = r

    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        max_heapify(tab, largest, heap_size)


def create_max_heap(tab):
    heap_size = len(tab)
    for i in range(heap_size//2, -1, -1):
        max_heapify(tab, i, heap_size)
    return heap_size


def heapsort(tab):
    heap_size = create_max_heap(tab)
    for i in range(heap_size-1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heap_size -= 1
        max_heapify(tab, 0, heap_size)


n = 1000
seed(420)
T = [randint(1, n) for i in range(n)]
# print("przed sortowaniem: T =", T)
start = time()
heapsort(T)
print(time() - start)
# print("po sortowaniu    : T =", T)
for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()
print("OK")