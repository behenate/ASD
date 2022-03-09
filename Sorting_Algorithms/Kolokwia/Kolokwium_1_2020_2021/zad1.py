"""
Treść:
Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby
są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T, tak
aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci ponad tę, która potrzebna
jest na przechowywanie danych wejściowych (choć algorytm nie musi działać w miejscu). Proszę
podać złożoność czasową i pamięciową zaproponowanego algorytmu.
"""
"""
Autor: Wojciech Dróżdż
Algorytm polega na znalezieniu N median wartości w tablicy, wpisaniu ich na przekątną i
przepisaniu odpowiednio mniejszych wartości pod i większych nad tą przekątną.
Mamy tablicę NxN elementów. W szacowaniu złożoności liczba n oznacza liczbę wszystkich elementów w tej tablicy.
Tablicę rzutuję na jednowymiarową i zapisuję ją - złożoność pamięciowa i obliczeniowa : O(n).
Tablicę sortuję algorytmem quicksort. - złożoność czasowa O(nlog(n)).
Znajduje index pierwszej i ostatniej z median i przepipisuje wartosci w na przekatna O (N) czasu
Wiem żę wszystkie elementy przed pierwszym indexem median są mniejsze a wszystkie po większe od nich więc wpisuję je
na odpowiednie miejsca. - Zajmuje to O(n - N) czasu
złożoność czasowa : O(nlog(n))
złożoność pamięciowa: O(n)
Uwaga! Algorytm można rozwiązać szybciej, gdy wartości są rzeczywiście różne. Można użyć algorytmu select by znaleźć
N median - złożoność N*n i wiedząc że wszystkie wartości są różne na podstawie czy są większe czy mniejsze od
najmniejszego i największego ze znalezionych median decydować o ich miejscu. Zdecydopwałem się jednak na wolniejszą wersję,
która przechodzi podane testy.
"""

from zad1testy import runtests

def partition(tab, p, r):
    last = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= last:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r):
    if p < r:
        i = partition(tab, p, r)
        quicksort(tab, p, i - 1)
        quicksort(tab, i + 1, r)

def Median(T):
    n = len(T)
    num_elems = n**2
    in_data = [0]*num_elems
    c = 0
    for sub in T:
        for elem in sub:
            in_data[c] = elem
            c += 1

    quicksort(in_data, 0, num_elems-1)
    m_p = ((num_elems-n) // 2)
    m_q = m_p+n-1
    for i in range(n):
        T[i][i] = in_data[m_q - i]
    c = len(in_data)-1
    for i in range(n):
        for j in range(i + 1, n):
            T[i][j] = in_data[c]
            c -= 1

    c = 0
    for i in range(n-1,-1,-1):
        for j in range(i):
            T[i][j] = in_data[c]
            c += 1
    return T

runtests( Median )
