"""Dane jest drzewo BST zbudowane z węzłów
class BNode:
def __init__( self, value ):
self.left = None
self.right = None
self.parent = None
self.value = value
Klucze w tym drzewie znajdują się w polach value i są liczbami całkowitymi. Mogą zatem mieć
wartości zarówno dodatnie, jak i ujemne. Proszę napisać funkcję, która zwraca wartość będącą
minimalną możliwą sumą kluczy zbioru wierzchołków oddzielających wszystkie liście od korzenia
w taki sposób, że na każdej ścieżce od korzenia do liścia znajduje się dokładnie jeden wierzchołek z
tego zbioru. Zakładamy że korzeń danego drzewa nie jest bezpośrednio połączony z żadnym liściem
(ścieżka od korzenia do każdego liścia prowadzi przez co najmniej jeden dodatkowy węzeł). Jako
liść jest rozumiany węzeł W typu BNode such that W.left = W.right = None.
Rozwiązanie należy zaimplementować w postaci funkcji:
def cutthetree(T):
...
która przyjmuje korzeń danego drzewa BST i zwraca wartość rozwiązania. Nie wolno zmieniać
definicji class BNode."""
from zad2testy import runtests
from math import inf
"""
Autor:  Wojciech Dróżdż:
Algorytm polega na rozważeniu kilku podstawowych przypadków:
Jeżeli z aktualnego node'a jest ścieżka tylko w lewo to można w nią i na pewno był to dobry ruch
Jeżeli node rozgałęzia się to albo najlepszym rozwiązaniem jest wartość węzła lub suma optymalnych usunięć
w dzieciach.
Jeżeli z aktualnego węzła jest ścieżka tylko w prawo i jest on dodatni:
na pewno aktualny węzeł jest najlepszym możliwym rozwiązaniem
Jeżeli z aktualnego węzła jest ścieżka tylko w prawo i jest on mniejszy od 0:
Nie wiadomo, czy suma usunięć w dzieciach tego węzła nie będzie lepsza niż wartość samego węzła, dlatego
ten węzeł też rozważamy rekurencyjnie

Po wykonaniu powyższych kroków w algorytmie uzyskamy poprawny wynik

Skoro każdy z węzłów rozważymy maksymalnie raz, złożoność to O(n)

"""
class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value



def cutthetree(T, recur=0):
    n1 = T.left
    n2 = T.right
    best_left = inf
    best_right = inf
    if recur == 1:
        n2 = None
        best_right = 0
    if recur == 2:
        n1 = None
        best_left = 0
    while n1 and (n1.left is not None or n1.right is not None):
        if n1.left and n1.right:
            r1 = cutthetree(n1,1)
            r2 = cutthetree(n1,2)
            best_left = min(best_left, min(r1+ r2, n1.value))
            break
        if not n1.left and n1.right:
            if n1 > 0:
                best_left = min(best_left, n1.value)
                break
            best_left = min(best_left, cutthetree(n1, 2), n1.value)
            break
        if n1.left and not n1.right:
            best_left = min(best_left, n1.value)
            n1 = n1.left

    while n2 and (n2.left is not None or n2.right is not None):
        if n2.left and n2.right:
            r21 = cutthetree(n2,1)
            r22 = cutthetree(n2,2)
            best_right = min(best_right, min(r21 + r22, n2.value))
            break
        if not n2.left and n2.right:
            if n2.value > 0:
                best_right = min(best_right, n2.value)
                break
            best_right = min(best_right, cutthetree(n2, 2), n2.value)
            break
        if n2.left and not n2.right:
            best_right = min(best_right, n2.value)
            n2 = n2.left
    return best_right+best_left

A = [-1000, -1002, -1003, -1001, 10, -200, 100, -201, -199, 99, 101]
runtests(cutthetree)


