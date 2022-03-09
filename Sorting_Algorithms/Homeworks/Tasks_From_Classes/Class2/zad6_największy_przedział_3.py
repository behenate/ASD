"""
Zadanie 6 (największy przedział). Dany jest ciąg przedziałów domkniętych [a1, b1], . . . ,[an, bn]. Proszę
zaproponować algorytm, który znajduje taki przedział [at, bt], w którym w całości zawiera się jak najwięcej
innych przedziałów
"""


def partition_tuple(tab, p, r, idx):
    last = tab[r][idx]
    i = p - 1
    for j in range(p, r):
        if tab[j][idx] <= last:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort_tuple(tab, p, r, idx):
    if p < r:
        i = partition_tuple(tab, p, r, idx)
        quicksort_tuple(tab, p, i - 1, idx)
        quicksort_tuple(tab, i + 1, r, idx)


def binary_search_tuple(tab, value, idx):
    p = 0
    r = len(tab) - 1
    while p <= r:
        q = (p + r) // 2
        if tab[q][idx] == value:
            while q + 1 < len(tab) and tab[q + 1][idx] == value:
                q += 1
            return q
        elif tab[q][idx] < value:
            p = q + 1
        else:
            r = q - 1


def find_biggest(ranges):
    n = len(ranges)
    rng_a = [ranges[i] for i in range(n)]
    rng_b = [ranges[i] for i in range(n)]

    quicksort_tuple(rng_a, 0, n - 1, 0)
    quicksort_tuple(rng_b, 0, n - 1, 1)
    print(rng_a)
    print(rng_b)
    max_found = 0
    max_index = 0
    for i in range(n):
        rng = rng_a[i]
        _i = i
        while _i > 0 and rng_a[_i-1][0]==rng[0]:
            _i -= 1
        how_many_end_before = binary_search_tuple(rng_b, rng[1], 1)
        # print(rng, how_many_end_before - i)
        if how_many_end_before - _i > max_found:
            print(rng, how_many_end_before - _i)
            max_found = how_many_end_before - _i
            max_index = i
    print(rng_a[max_index])


r = [[1, 3], [1, 2],[1, 2],[1, 2],[1, 2], [5, 8], [6, 7], [6, 8], [2, 5], [2, 3], [1, 4],[6,7],[6,7],[6,7],[6,7],[6,7],[6,7],[6,7],[6,7],[6,7],[6,7], [7, 8], [1, 2]]
find_biggest(r)
