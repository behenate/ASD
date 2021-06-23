from queue import PriorityQueue
"""
Wojciech Dróżdż:
Algorytm używa kolejki priorytetowej (opartej o kopiec typu min). Działa wg algorytmu zachłannego przedstawionego
na wykładzie. Do przechowania drzewa użyta jest struktura Node, która pozwala łatwo tworzyć drzewo, którego
liście wiedzą na jakiej pozycji były w wejściowej tablicy, po to, aby przy wypisaniu wypisać kody w takiej samej
kolejności, w jakiej były podane znaki na wejściu.
Po wypełnieniu drzewa używana jest rekurencyjna funkcja, która odtwarza ścieżkę do każdego z liści, oraz wpisuje tą 
ścieżkę do tablicy wynikowej.
Ostatecznie pętla po tablicy wynikowej wypisuje dane w podanej kolejności i przy okazji zlicza sumę.

W przeciętnym przypadku złożoność algorytmu to O(nlogn) - stworzenie kolejki zajmuje O(n) czasu, następnie są wyciągane
2 ostatnie elementy - 2 * O(logn), łączone w jeden nowy i wstawiane - O(logn). Operacja ta jest powtarzana n-1 razy, 
więc ostatecznie złożoność całości to O(nlogn).
Wynika z tego, że złożoność algorytmu to O(nlogn) 

Wypisywanie:
W pesymistycznym przypadku (ciągu fibonacciego) długości kodów huffmana to 1,2,3,4, ... , n ~= n**2

"""

class Node:
    def __init__(self, val, idx=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.idx = idx

    # Funkcje porównawcze dla priority queue. Zmienne mogą być identyczne jak u innych bo pycharm je sugeruje (⌐■_■)
    def __gt__(self, other):
        return self.val > other.val

    def __lt__(self, other):
        return self.val < other.val


def huffman(S, F):
    n = len(S)
    queue = PriorityQueue()
    # Utwórz kolejkę z liśćmi drzewa
    for i in range(n):
        queue.put(Node(val=F[i], idx=i))
    while queue.qsize() > 1:
        a = queue.get()
        b = queue.get()
        new = Node(val=a.val + b.val, left=b, right=a)
        queue.put(new)
    codes = [[] for _ in range(n)]
    # Wypełnij pod odpowiednimi indeksami kody odpowiadające liczbom
    fill_codes(queue.queue[0], "", codes)
    # Skrajny przypadek - próbujemy zakodować tylko jedną cyfrę:
    if n == 1:
        codes[0] = "0"
    cost = 0
    for i in range(n):
        print(S[i], " : ", codes[i])
        cost += F[i] * len(codes[i])
    print("dlugosc napisu: ", cost)
    pass


def fill_codes(node, code, codes):
    # Po lewej zawsze są mniejsze z dwóch, dlatego dodaj do wyniku 0
    if node.left is not None:
        fill_codes(node.left, code + "0", codes)
    # Po prawej zawsze są większe z dwóch, dlatego dodaj do wyniku 1
    if node.right is not None:
        fill_codes(node.right, code + "1", codes)
    # Jeżeli doszedł do liścia to wpisuje w odpowiedni indeks tablicy wynikowej kod huffmana
    if node.left is None and node.right is None:
        codes[node.idx] = code


S = ["a", "b", "c", "d", "e", "f"]
F = [10, 11, 7, 13, 1, 20]

huffman(S, F)
