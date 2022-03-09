"""
Zadanie 1. Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
pretty_sort(T)
która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
"""


def how_pretty(number):
    digit_tab = [0] * 10
    score = 10
    while number > 0:
        digit_tab[number % 10] += 1
        number //= 10

    for elem in digit_tab:
        if elem == 1:
            score += 10
        elif elem > 1:
            score -= 1
    return score


def count_sort(tab, num_tab):
    n = len(tab)
    b = [0]*n
    c = [0]*110

    for elem in tab:
        c[elem] = c[elem]+1
    for i in range(1, 110):
        c[i] = c[i] + c[i-1]

    for k in range(n-1, -1, -1):
        b[c[tab[k]]-1] = num_tab[k]
        c[tab[k]] = c[tab[k]] - 1
    return b


def pretty_sort(tab):
    score_tab = [0]*len(tab)

    for i in range(len(tab)):
        score_tab[i] = how_pretty(tab[i])
    return count_sort(score_tab, tab)


tab = [455, 1266, 114577, 2344, 67333]
print(pretty_sort(tab))
