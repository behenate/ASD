from random import shuffle
# def partition(tab, p, r):
#     last = tab[r]
#     i = p - 1
#     for j in range(p, r):
#         if tab[j] <= last:
#             i = i + 1
#             tab[i], tab[j] = tab[j], tab[i]
#
#     tab[i + 1], tab[r] = tab[r], tab[i + 1]
#     return i + 1


def partition(tab, p, r):
    pivot = tab[r]
    i = p-1
    for j in range(p, r):
        if tab[j] < pivot:
            i += 1
            tab[j], tab[i] = tab[i], tab[j]
    tab[i+1], tab[r] = tab[r], tab[i+1]
    return i+1


def select(tab, p, r, index):
    if p == r:
        print("co1", p, tab[p])
        return tab[p]
    q = partition(tab, p, r)
    if q == index:
        print("co")
        return tab[q]
    elif index < q:
        return select(tab, p, q-1, index)
    else:
        return select(tab, q+1, r, index)

lst = list(range(12))
shuffle(lst)
print(lst)
print(select(lst,0,len(lst)-1, len(lst)//2))