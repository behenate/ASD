"""
Zadanie 6. Dana jest tablica A zawierająca n parami różnych liczb. Proszę zaproponować algorytm, który
znajduje takie dwie liczby x i y z A, że y −x jest jak największa oraz w tablicy nie ma żadnej liczby z takiej,
że x < y < z (innymi słowy, po posortowaniu tablicy A rosnąco wynikiem byłyby liczby A[i] oraz A[i+1] dla
których A[i + 1] − A[i] jest największe).
"""

from random import randint, seed
from math import floor

def insertion_sort(tab):
    if len(tab) == 0:
        return
    for j in range(1, len(tab)):
        key = tab[j]
        i = j-1
        while i >= 0 and tab[i] > key:
            tab[i+1] = tab[i]
            i -= 1
        tab[i+1] = key


def max_diff(arr, min, max):
    n = len(arr)
    max_x = 0
    max_y = 0
    buckets = [[] for _ in range(n)]
    for elem in arr:
        buckets[floor(((elem-min)/(max-min))*n)].append(elem)

    for bucket in buckets:
        insertion_sort(bucket)
    print(buckets)
    i = 0
    j = 1
    while j < n:
        while j <n-1 and len(buckets[j]) == 0:
            j += 1
        b1 = buckets[i]
        b2 = buckets[j]
        if j==n-1 and len(buckets[n-1]) ==0:
            break
        x_1 = b1[len(b1)-1]
        y_1 = b2[len(b2)-1]
        if y_1 - x_1 > max_y-max_x:
            max_x = x_1
            max_y = y_1
            print(max_x, max_y)
        i = j
        # print(i, j)
        j += 1

min = 0
max = 20
n = 10
seed("Dasia Boncer")
tab = [randint(min, max-1) for _ in range(n)]
print(tab)
max_diff(tab, min, max)
print(sorted(tab))
tab = sorted(tab)
max = 0
for i in range(1,n):
    if (tab[i]-tab[i-1]) > max:
        max = tab[i]-tab[i-1]
print(max)