"""Treść
Mamy daną N elementową tablicę T liczb rzeczywistych, w której liczby zostały wygenerowane z pewnego rozkładu losowego. Ten rozkład mamy zadany jako k przedziałów
[a1, b1],[a2, b2], . . . ,[ak, bk] takich, że i-ty przedział jest wybierany z prawdopodobieństwem ci
,
a liczba z przedziału jest wybierana zgodnie z rozkładem jednostajnym. Przedziały mogą na siebie nachodzić, liczby ai
, bi są liczbami naturalnymi ze zbioru {1, . . . , N}. Proszę zaimplementować
funkcję SortTab(T,P) sortująca podaną tablicę. Pierwszy argument to tablica do posortowania a
drugi to opis przedziałów w postaci:
P = [(a1, b1, c1), (a2, b2, c2), . . ., (ak, bk, ck)].
Na przykład dla wejścia:
P = [(1,5, 0.75) , (4,8, 0.25)]
T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
po wywołaniu SortTab(T,P) tablica T powinna być postaci:
T = [1.2, 1.5, 2.5, 3.5, 3.9, 4.5, 6.1, 7.8]
Algorytm powinien być możliwie jak najszybszy. Proszę podać złożoność czasową i pamięciową
zaproponowanego algorytmu.

"""

"""
Wojciech Dróżdż
Implementacja wykorzystuje algorytm Bucket sort. Znajdowane są największe i najmniejsze wartości przedziałów,
następnie tworzone są wiaderka i decydowane jest do którego z nich twafi wartość.
Algorytm działa w czasie O(n) i ma złożoność pamięciową O(n)

"""
from zad3testy import runtests


def insertion_sort(tab):
    for j in range(1, len(tab)):
        key = tab[j]
        i = j-1
        while i >= 0 and tab[i] > key:
            tab[i+1] = tab[i]
            i -= 1
        tab[i + 1] = key



def SortTab(T, P):
    min = 10000
    max = 0
    for elem in P:
        if elem[0] < min:
            min = elem[0]
        if elem[1] > max:
            max = elem[1]
    n = max-min
    b = [[] for _ in range(n)]

    for i in range(len(T)):
        index = T[i]-min
        if T[i] == max:
            b[-1].append(T[i])
        else:
            b[int((index/(max-min))*n)].append(T[i])
    for bucket in b:
        insertion_sort(bucket)
    k = 0
    for i in range(n):
        for elem in b[i]:
            T[k] = elem
            k += 1
runtests( SortTab )
