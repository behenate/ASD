def partition(tab, p, r):
    last = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= last:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r):
    if p < r:
        i = partition(tab, p, r)
        quicksort(tab, p, i - 1)
        quicksort(tab, i + 1, r)


def binary_search(arr, elem):
    p = 0
    r = len(arr) - 1
    while p < r:
        m = (p + r) // 2
        if arr[m] == elem:
            return m
        elif elem < arr[m]:
            r = m - 1
        else:
            p = m + 1
    return False


def overlap(arr_n, arr_m):
    n = len(arr_n)
    m = len(arr_m)
    quicksort(arr_n, 0, n-1)
    for elem in arr_m:
        if binary_search(arr_n, elem) != False:
            print("FOUNDDD!", elem)
            return True
    return False


arr_n = [8, 6, 9, 1, 2, 11, 14, 13, 5]
arr_m = [3, 7, 123, 123, 1]
print(overlap(arr_n, arr_m))