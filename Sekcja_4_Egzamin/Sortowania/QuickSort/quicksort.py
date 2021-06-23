def partition(tab, p, r):
    pivot = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= pivot:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r):
    if p < r:
        q = partition(tab, p, r)
        quicksort(tab, p, q - 1)
        quicksort(tab, q + 1, r)
