"""
Wojciech Dróżdż
Aby znaleźć podciągi we wskazanej kolejności należy znaleźć najdłuższy malejący podciąg w tablicy odwróconej,
wtedy mając ostatni element podciągu malejącego odwróconego mamy pierwszy element podciągu rosnącego nieodwróconego, co
pozwala nam łatwo wybrać od którego elementu podciągu rozpocząć wypisywanie.

Algorytm nie odwraca tablicy. Można przy pomocy manipulowania wartościami indexów "zasymulować" tablicę odwróconą i tak
wykonać algorytm.

Funkcja wypisująca jest rekurencyjna i używa jednej tablicy która jest listą do wypisywania która jest  
wypisywana na końcu rekurencji. Potem wartości są nadpisywane bo nie są już potrzebne.

Z powodu charakterystyki funkcji print pythona dla dużej ilości elementów wypisanie ich zajmuje dość długo, natomiast
można zapisywać wyniki do tablicy i potem wypisać całą naraz co działa dużo dużo szybciej, 
ale wtedy wzrasta złożoność pamięciowa. Jest to tylko dygresja odnośnie praktycznej implementacji. W teorii
wypisywanie powinno zająć dokładnie tyle samo w obu przypadkach, a nawet nieco mniej w tym którego używam.

Funkcja znajdująca ścieżki po których należy rekurencyjnie przejść aby wypisać jest bardzo podobna do zwykłego LIS.
Tablica długości działa dokładnie tak samo, a tablica rozszerzeń jest teraz dwuwymiarowa i zamiast jednej ścieżki 
najdłuższej zapisuje wszystkie indeksy na które można pójść szukając najdłuższej ścieżki.

Ilość podciągów jest zliczana przy okazji rekurencji.

Funkcja printAllLIS ma złożoność O(n^2), funkcja print_solution ma złożoność taką jaka jest (ilość najdłuższych podciągów)*(długość tych podcigów)

"""


# Longest decreasing subsequence
def printAllLIS(arr):
    n = len(arr)
    lengths = [1] * n
    extends = [[] for _ in range(n)]
    max_length = 0
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            # Jeśli długość jest większa wyczyść extends na j i wstaw nowe, prawidłowe przedłużenie
            if arr[j] > arr[i] and lengths[n - j - 1] + 1 > lengths[n - i - 1]:
                lengths[n - i - 1] = lengths[n - j - 1] + 1
                # Jeżeli ta maksymalna lokalna długość jest większa od tej głównej to ją zastąp
                max_length = max(max_length, lengths[n - i - 1])
                # Wyczyść tablicę rozszerzeń pod aktualnym indexem i wstaw tam pierwsze potencjalne rozszerzenie
                extends[n - i - 1] = [n - j - 1]
            # Jeśli długość  jest równa aktualnej maksymalnej to jest kilka potencjalnie najdłuższych podciągów
            elif arr[j] > arr[i] and lengths[n - j - 1] + 1 == lengths[n - i - 1]:
                extends[n - i - 1].append(n - j - 1)

    total = 0
    # W celu uzyskania odpowiedniej kolejności należy tu iść od końca.
    for i in range(n - 1, -1, -1):
        if lengths[i] == max_length:
            total += print_solution(arr, extends, i, [0] * max_length)
    return total


def print_solution(arr, extends, current_index, append_tab, tab_index=0):
    n = len(arr) - 1

    # Warunek wyjścia z pętli - element nie posiada przedłużenia
    if len(extends[current_index]) == 0:
        append_tab[tab_index] = arr[n - current_index]
        for elem in append_tab:
            print(elem, end=" ")
        print("")
        return 1

    cnt = 0
    # Dla każdego rozgałęzienia wykonaj pod-rekurencję
    for i in range(len(extends[current_index])):
        append_tab[tab_index] = arr[n - current_index]
        cnt += print_solution(arr, extends, extends[current_index][i], append_tab, tab_index + 1)
    return cnt


# _arr = [2,1,4,3]
# printAllLIS(_arr)
