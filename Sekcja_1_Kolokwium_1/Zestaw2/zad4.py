"""
Zadanie 4. (Pojemniki z wodą) Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami.
Pojemniki maja kształty prostokątów, rury nie maja objetosci (powierzchni). Każdy pojemnik opisany jest
przez współrzędne lewego górnego rogu i prawego dolnego rogu.
Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda rurami spłynęła do najniźszych
pojemników). Proszę zaproponować algorytm Obliczający ile pojemników zostało w pełni zalanych.
"""


def find_surface(c):
    return abs((c[0][0] - c[1][0]) * (c[0][1] - c[1][1]))


def partition(tab, p, r):
    last = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= last:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r):
    if p < r:
        i = partition(tab, p, r)
        quicksort(tab, p, i - 1)
        quicksort(tab, i + 1, r)


containers = [((0, 2), (2, 0)), ((3, 1), (5, 0)), ((6, 2), (10, 0)), ((11, 3), (15, 0))]
surfaces = [0] * len(containers)
for i in range(len(containers)):
    surfaces[i] = find_surface(containers[i])
quicksort(surfaces, 0, len(surfaces) - 1)
full_containers = 0
water = 20
for container in surfaces:
    water -= container
    if water < 0:
        break
    full_containers += 1
print(surfaces)
print(full_containers)
