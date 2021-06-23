from math import *
"""
    Wojciech Dróżdż, Algorytm komiwojażera bitonicznego jest bardzo podobny do tego z wykładu.
    W celu znalezienia optymalnej ścieżki należy najpierw zapisać do tablicy 2D na indexach i,j z jakiego miasta
    przeszliśmy na miasto j przy kombinacji ścieżek 0->i oraz 0->j.
    Aby odtworzyć ścieżkę należy rozpocząć od prawie lewego dolnego rogu tablicy i kontynuować w górę jednocześnie 
    rozpoznając miasto z której ścieżki aktualnie rozważamy. Mając te informacje wystarczy wypisać miasta po inexach 
    miast w odwróconej kolejności z pierwszej zapisanej ścieżki oraz w uzyskanej kolejności z drugiej.
    Szczegóły algorytmu są opisane w komentarzach jedno-linijkowych.
"""


def bitonicTSP(C):
    # Posortuj wejściową tablicę, wbudowanym algorytmem sortowania
    C = sorted(C, key=lambda x: x[1])
    n = len(C)
    D = [[0 for _ in range(n)] for _ in range(n)]
    F = [[inf for _ in range(n)] for _ in range(n)]
    # Wykorzystując funkcję dist z biblioteki math oblicz odległości między wszystkimi miastami ( jednokierunkowe)
    for i in range(n):
        for j in range(i, n):
            D[i][j] = dist((C[i][1], C[i][2]), (C[j][1], C[j][2]))
    # Wypełnij pierwszą odległość, ponieważ zawsze jest znana
    F[0][1] = D[0][1]
    # Tablica przechowująca dane potrzebne do odtworzenia wyniku
    G = [[-1 for _ in range(n)] for _ in range(n)]
    # Znajdź pole z którego dotarło się na ostatnie miasto, jednocześnie wypełnij tablicę ścieżek
    for k in range(n - 1):
        F[n-1][n-1] = min(F[n-1][n-1], bitonicTSP_recur(k, n - 1, F, D, G) + D[k][n - 1])
    # Wypisz dystans dla opisanej ścieżki
    print(F[n - 1][n - 1])
    # Dwa pierwsze miasta można wpisać już do ścieżek wynikowych ponieważ na ostatnie miasto zawsze przeskoczymy
    # Z najbliższego do niego w jednej ze ścieżek
    i = n-2
    j = n-1
    # Dwie ścieżki wynikowe
    paths = [[n-1], [n-2]]
    ii = 0 # Indeks wskazujący na którą ścieżkę chcemy dodać następne miasto
    while G[i][j] != -1:
        k = G[i][j]
        if k < i:  # Jeżeli k < i to następuje zamiana ścieżek
            paths[ii].append(k)
            j = i
            i = k
            # Zamień ścieżkę do której będzie wstawiany wynik w kolejnej iteracji
            ii += 1
            ii %= 2
        else:
            j = k
            paths[ii].append(k)
    # Jedna ze ścieżek nie będzie miała w sobie ostatniego (a właściwie pierwszego) miasta z powodu zakończenia while,
    # Znajdź ją i dodaj do niej miasto wyjściowe
    for path in paths:
        if path[-1] != 0:
            path.append(0)
    # Wypisz pierwsze miasta w kolejności odwróconej
    m = len(paths[0])
    for i in range(len(paths[0])):
        print(C[paths[0][m-i-1]][0], end=", ")
    # Miasta z drugiej ścieżki wypisz w kolejności w jakiej wydał je algorytm
    m = len(paths[1])
    for i in range(len(paths[1])):
        if i != m-1:  # If dla poprawnego wypisania przecinków
            print(C[paths[1][i]][0], end=", ")
        else:
            print(C[paths[1][i]][0], end="")
    print()


def bitonicTSP_recur(i, j, F, D, G):
    if F[i][j] != inf:
        return F[i][j]
    if i == j - 1:
        for k in range(j - 1):
            res = bitonicTSP_recur(k, i, F, D, G) + D[k][j]
            if res < F[i][j]:
                F[i][j] = res
                G[i][j] = k
    else:
        G[i][j] = j - 1
        F[i][j] = bitonicTSP_recur(i, j - 1, F, D, G) + D[j - 1][j]
    return F[i][j]
