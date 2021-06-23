def partition(tab, p, r):
    last = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] < last:
            i += 1
            tab[j], tab[i] = tab[i], tab[j]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r):
    while p < r:
        q = partition(tab, p, r)
        if q - p < r - q:
            quicksort(tab, p, q-1)
            p = q+1
        else:
            quicksort(tab, q+1, r)
            r = q - 1

        # quicksort(tab, p, q - 1)
        # p = q+1


tab = [10, 7, 5, 2, 4, 3, 2, 2]
quicksort(tab, 0, len(tab)-1)
print(tab)
