"""
[2pkt.] Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu. Proszę zaimplementować funkcję: section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
"""

# ZAKŁADAM ŻE KAŻDA OSOBA MA CO NAJMNIEJ 100 CM WZROSTU I JEST NIE WYŻSZA NIŻ 250CM
def countsort(tab, k):
    n = len(tab)
    b = [0]*len(tab)
    c = [0]*k

    for elem in tab:
        c[elem-100] = c[elem-100] + 1

    for i in range(1, k):
        c[i] = c[i] + c[i-1]

    for k in range(n-1, -1, -1):
        b[c[tab[k]-100]-1] = tab[k]
        c[tab[k]-100] = c[tab[k]-100] - 1
    return b


t = [198, 179, 183, 179, 192, 186, 190, 205, 167, 208, 197, 175, 166, 171, 204, 177, 167, 181, 178, 197, 161, 184,
     205, 188, 168, 175, 199, 172, 193, 202, 180, 174, 189, 179, 206, 210, 202, 185, 177]
res = countsort(t, 150)
print(res)