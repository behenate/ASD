"""
Zadanie 4. (min/max) Proszę zaimplementować funkcję, która mając na wejściu tablicę n elementów
oblicza jednocześnie jej największy i najmniejszy element wykonując 1.5n porównań.
"""

from math import inf
def min_max(arr):
    add = 0 if len(arr)%2==0 else 1
    min_arr = [inf] * (len(arr)//2 + add)
    max_arr = [-inf] * (len(arr)//2 + add)
    for i in range(0, len(arr)-add, 2):
        if arr[i] > arr[i+1]:
            min_arr[i//2] = arr[i+1]
            max_arr[i//2] = arr[i]
        else:
            min_arr[i // 2] = arr[i]
            max_arr[i // 2] = arr[i+1]
    if add:
        min_arr[-1] = arr[-1]
    smol = min_arr[0]
    big = max_arr[0]
    for i in range(len(max_arr)):
        if min_arr[i] < smol:
            smol = min_arr[i]
        if max_arr[i] > big:
            big = max_arr[i]
    return smol, big


arr = [10,10,10,1]
print(min_max(arr))
