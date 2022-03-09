"""
Znajdź zakres w jakim dana liczba znajduje się w tablicy po posortowaniu
"""
from random import randint, seed
def binary_search_range(arr,x, p, r):
    while p<r:
        c = (p+r)//2
        if arr[c]==x:
            return c
        elif arr[c] is None or arr[c] > x:
            r = c-1
        else:
            p = c+1

def find_range(arr, x):
    idx_check = 1
    while arr[idx_check] is not None and arr[idx_check] < x:
        idx_check *= 2
    print(binary_search_range(arr, x, idx_check//2, idx_check))


seed("Dojciech Wróżdż")
arr = [None]*10000
n = 500
for i in range(n):
    arr[i] = randint(i, i+1)
print(arr)
find_range(arr, 0)
