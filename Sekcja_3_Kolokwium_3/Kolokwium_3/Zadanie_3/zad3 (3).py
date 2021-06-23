from zad3testy import runtests
from zad3EK import edmonds_karp
from math import inf
"""
Autor: Wojciech Dróżdż
Algorytm polega na stworzeniu turbo-źródła koloru zielonego i niebieskiego. Z nimi łączymy wszystkie wierzchołki
zielone i niebieskie. Używając Floyda-Warshalla znajduję odpowiednie odległości między 
każdym a każdym. Teraz przechodzę po wszystkich wierzchołkach i szukam takich połączeń, gdzie kolory wierzchołków
są różne i odległości między nimi odpowiednie, Jeżeli są to ustawiam krawędź na 1 jeżeli nie są to ustawiam na 0.
Teraz po wykonaniu algorytmu maksymalnego przepływu uzyskuję odpowiedź do zadania.

Złożoność obliczeniowa O(V^2 * E) ~= O(V^3) dla grafów rzadkich, O(V^4) dla gęstych   (algorytm edmondsa-karpia)
Złożoność pamięciowa O(V^2) (Tablica S w algorytmie floyda-warshalla)
gdzie V to ilość wierzchołków, E krawędzi
"""

def floyd_warshall(G):
    n = len(G)
    S = [[G[i][j] if G[i][j] != 0 else inf for j in range(n)] for i in range(n)]
    for t in range(n):
        for i in range(n):
            for j in range(n):
                S[i][j] = min(S[i][j], S[i][t] + S[t][j])
    for i in range(n):
        S[i][i] = 0
    return S

def BlueAndGreen(T, K, D):
    n = len(T)
    S = floyd_warshall(T)
    # Dodaje do grafu wejściowego turbo-źródło i turbo-ujście
    T.append([])
    T.append([])
    for i in range(n):
        if K[i] == "B":
            T[i].append(inf)
            T[i].append(0)
        if K[i] == "G":
            T[i].append(0)
            T[i].append(inf)
    for color in range(n):
        if K[color] == "B":
            T[n].append(inf)
            T[n+1].append(0)
        if K[color] == "G":
            T[n].append(0)
            T[n + 1].append(inf)
    # Skierowuję graf, żeby nie uzyskiwać zbyt dużego przepływu
    for i in range(n):
        for j in range(n):
            if j < i:
                T[i][j] = 0
                S[i][j] = 0

    for i in range(n):
        for j in range(n):
            if S[i][j] >= D and K[i] != K[j]:
                T[i][j] = 1
            else:
                T[i][j] = 0
    result = edmonds_karp(T, n, n+1)
    return result

runtests( BlueAndGreen )