from random import randint, seed

def merge(tab, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)
    for i in range(n1):
        left[i] = tab[p + i]
    for j in range(n2):
        right[j] = tab[q + j + 1]
    left[-1] = 999999
    right[-1] = 999999

    i = 0
    j = 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            tab[k] = left[i]
            i += 1
        else:
            tab[k] = right[j]
            j += 1


def merge_sort(tab, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(tab, p, q)
        merge_sort(tab, q + 1, r)
        merge(tab, p, q, r)


seed(100)
a = [randint(0, 100) for _ in range(100)]
print(a)
print(merge_sort(a))