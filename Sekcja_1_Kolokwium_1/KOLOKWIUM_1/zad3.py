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