def insertion_sort(tab):
    for j in range(1, len(tab)):
        key = tab[j]
        i = j-1
        while i >= 0 and tab[i] > key:
            tab[i+1] = tab[i]
            i -= 1
        tab[i + 1] = key


def bucket_sort(tab):
    n = len(tab)
    b = [[] for _ in range(n)]
    for i in range(n):
        b[int(n*tab[i])].append(tab[i])
    for bucket in b:
        insertion_sort(bucket)
    k = 0
    for i in range(n):
        for elem in b[i]:
            tab[k] = elem
            k += 1
