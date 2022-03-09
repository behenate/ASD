from random import shuffle
def partition(tab, p, r):
    last = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= last:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1

def select(tab, p, r, k):
    if p == r:
        return tab[p]
    q = partition(tab, p, r)
    if q == k:
        return tab[q]
    elif k < q:
        return select(tab, p, q - 1, k)
    else:
        return select(tab, q + 1, r, k)


test = list(range(10))
shuffle(test)
print(select(test,0,9,7))