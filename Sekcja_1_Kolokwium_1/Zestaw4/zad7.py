"""
Zadanie 7. Dana jest tablica A zawierająca n elementów, z których każdy ma jeden z k kolorów.
Proszę podać możliwie jak najszybszy algorytm, który znajduje indeksy i oraz j takie, że wsród elementów
A[i], A[i + 1], . . . , A[j] występują wszystkie k kolorów oraz wartość j − i jest minimalna (innymi słowy,
szukamy najkrótszego przedziału z wszystkimi kolorami).
"""
from random import randint, seed


def find_series(arr, k):
    i = 0
    j = 1
    min_i = 0
    min_j = len(arr)
    found_colors = [0] * k
    found_colors[arr[i]] += 1
    unique = 1
    while j < len(arr):
        if found_colors[arr[j]] == 0:
            unique += 1
        found_colors[arr[j]] += 1

        if unique == k:
            while found_colors[arr[i]] > 1:
                found_colors[arr[i]] -= 1
                i += 1
            if j-i < min_j-min_i:
                min_i = i
                min_j = j
            found_colors[arr[i]] -= 1
            unique -= 1
        j += 1
    print(min_i, min_j)



k = 5
n = 20
seed(3)
colors = [randint(0, k - 1) for _ in range(n)]
find_series(colors, k)
print(colors)
