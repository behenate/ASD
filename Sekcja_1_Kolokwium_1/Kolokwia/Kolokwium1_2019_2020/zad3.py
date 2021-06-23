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
    while p < r:
        q = partition(tab, p, r)
        if q - p < r - q:
            quicksort(tab, p, q - 1)
            p = q + 1
        else:
            quicksort(tab, q + 1, r)
            r = q - 1


t = [198, 179, 183, 179, 192, 186, 190, 205, 167, 208, 197, 175, 166, 171, 204, 177, 167, 181, 178, 197, 161, 184,
     205, 188, 168, 175, 199, 172, 193, 202, 180, 174, 189, 179, 206, 210, 202, 185, 177]


def sum_of_two(tab, index):
    l_i = len(tab) - 1
    f_i = 0
    value = tab[index]
    if f_i == index:
        f_i += 1
    if l_i == index:
        l_i -= 1
    while f_i < l_i:
        if tab[f_i] + tab[l_i] < value:
            f_i += 1
            if f_i == index:
                f_i += 1
        elif tab[f_i] + tab[l_i] > value:
            l_i -= 1
            if l_i == index:
                l_i -= 1
        else:
            return True
    return False


def all_sum_another(tab):
    quicksort(t, 0, len(tab) - 1)
    for i in range(len(tab)):
        if not sum_of_two(tab, i):
            print("liczba {} nie jest!".format(tab[i]))
        else:
            print("liczba {} jest sumą!".format(tab[i]))


# Oczekiwana złożoność nlog(n) + n^2
print(sum_of_two([5, 10, 15], 1))
all_sum_another(tab=[1, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
print(t)
