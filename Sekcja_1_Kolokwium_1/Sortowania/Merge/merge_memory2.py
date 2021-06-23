from math import inf


def merge(tab, p, q, r):
    left = tab[p:q + 1]
    right = tab[q + 1:r + 1]
    left.append(inf)
    right.append(inf)
    i = 0
    j = 0
    for k in range(p, r+1):
        if left[i] <= right[j]:
            tab[k] = left[i]
            i += 1
        else:
            tab[k] = right[j]
            j += 1


def mergesort(tab, p, r):
    if p < r:
        q = (p + r) // 2
        mergesort(tab, p, q)
        mergesort(tab, q + 1, r)
        merge(tab, p, q, r)


a = [1, 5, 3, 4, 8, 8, 5, 8, 4, 2, 3, 5, 7, 1]
mergesort(a, 0, len(a) - 1)
print(a)
