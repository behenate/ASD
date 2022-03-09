# Takie samo jak zad_2, ale z nieco inną implementacją countsort
"""
[2pkt.] Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu. Proszę zaimplementować funkcję: section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
"""

def countsort(tab, k, p, q):
    n = len(tab)
    b = [0] * len(tab)
    c = [0] * k

    for elem in tab:
        c[149 - (elem - 150)] += 1

    for i in range(1, k):
        c[i] += c[i - 1]

    for i in range(n - 1, -1, -1):
        c[149 - (tab[i] - k)] -= 1
        b[c[149 - (tab[i] - k)]] = tab[i]
    return b[p:q]


t = [150, 169, 179, 189, 189, 210, 222, 205, 193, 188]
t = countsort(t, 150, 0, 10)
print(t)
