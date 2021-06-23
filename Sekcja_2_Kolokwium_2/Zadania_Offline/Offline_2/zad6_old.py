from math import *
from matplotlib import pyplot

def bitonicTSP(C):
    C = sorted(C, key=lambda x: x[1])
    # print(C)
    n = len(C)
    D = [[0 for _ in range(n)] for _ in range(n)]
    F = [[inf for _ in range(n)] for _ in range(n)]
    # for elem in C:
    #     pyplot.plot(elem[1], elem[2], 'bo')
    # pyplot.show()
    for i in range(n):
        for j in range(i, n):
            D[i][j] = dist((C[i][1], C[i][2]), (C[j][1], C[j][2]))
    F[0][1] = D[0][1]
    G = [-1] * n
    GG = [-1] * n
    G[1] = 0
    #G[i] - index miasto z którego przeskoczyliśmy na miasto i
    GG[1] = 0
    # print(GG)
    starters = [-1, -1]
    fi = 0
    for k in range(n - 1):
        G = GG[:]
        res = bitonicTSP_recur(k, n - 1, F, D, G, GG) + D[k][n - 1]
        if res <= F[n - 1][n - 1]:
            F[n - 1][n - 1] = res
            for i in range(n):
                GG[i] = G[i]
            # print(res, k)
            starters[fi] = k
            fi = (fi + 1) % 2
    print_path(C, starters, G)
    # print(GG)


def print_path(C,starters,GG):
    # Pierwsza część ścieżki musi być odwrócona, ponieważ ścieżki są względem ostatniego miasta.
    # Najłatwiej wypisać ją rekurencyjnie
    rpfp(C, starters[0], GG)
    # Wypisz element końcowy
    # print(end="")
    print(C[-1][0], end=",")
    # Nierekurencyjnie wypisz pozostałą część ścieżki, jej kolejność jest poprawna.

    m = starters[1]
    while m != -1:
        if m != 0:
            print(C[m][0], end=",")
        else:
            print(C[m][0], end="")
        m = GG[m]
    print()

def rpfp(C, index, path):
    if index != 0:
        rpfp(C, path[index], path)
    print(C[index][0], end=",")


def bitonicTSP_recur(i, j, F, D, G, GG):
    if F[i][j] != inf:
        # G[j] = GG[j]
        return F[i][j]
    if i == j - 1:
        for k in range(j - 1):
            res = bitonicTSP_recur(k, i, F, D, G, GG) + D[k][j]
            if res < F[i][j]:
                F[i][j] = res
                G[j] = k
    else:
        F[i][j] = bitonicTSP_recur(i, j - 1, F, D, G, GG) + D[j - 1][j]
        G[j] = j - 1

    return F[i][j]


C0 = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1], ["Paprykarz", 6, 2], ["Palcza", 7, 3]]
C1 = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1], ["Papr", 1, 3], ["kox", 0.5, -2]]
C2 = [["Wrocław", 0, 1], ["Warszawa", 11, 5], ["Gdańsk", 4, 2], ["Kraków", 2, 1], ["Papr", 7, 3], ["kox", 0.5, 4]]
C3 = [["Wrocław", 0, 12], ["Warszawa", 1, 3], ["Gdańsk", 2, 8], ["Kraków", 12, -5], ["Papr", 4, -1], ["kox", 8, 9]]
C4 = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],
      ['I', 0.5, 2.5], ['J', 1.5, 3.5]]
C5 = [["A", 0, 2], ["B", 4, 3], ["C", 2, 4], ["D", 3, 1], ["E", 1, 3], ["F", 0.5, -2]]
C6 = [["Wrocław", 0, 2], ["Warszawa",4,3], ["Gdańsk", 2,4], ["Kraków",3,1]]
C7 = [["1", 0, 1], ["2", 1, -6], ["3", 3, -1], ["4", 6, -2], ["5", 10, 1], ["6", 14, 3], ["7", 9, 4], ["8", 7, 2], ["9", 4, 3], ["10", 2, 3]]
C8 = [['s', 9, 24], ['e', 11, 2], ['y', -5, 26], ['a', 28, -17], ['i', 23, 11], ['W', -24, -24], ['h', 29, 24],
     ['*', -25, 27], ['U', 22, -16], ['b', 5, 2], ['j', 15, -25], ['s', 24, -10], ['i', -9, 9], ['k', 18, 4],
     ['e', -19, 10], ['t', 16, -3], ['W', 30, 10], ['c', 26, 11], ['s', -20, -17], ['z', -17, 27]]

bitonicTSP(C0)
bitonicTSP(C1)
bitonicTSP(C2)
bitonicTSP(C3)
bitonicTSP(C4)
bitonicTSP(C5)
bitonicTSP(C6)
bitonicTSP(C7)
bitonicTSP(C8)

C0 = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1], ["Paprykarz", 6, 2], ["Palcza", 7, 3]]
C1 = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1], ["Papr", 1, 3], ["kox", 0.5, -2]]
C2 = [["Wrocław", 0, 1], ["Warszawa", 11, 5], ["Gdańsk", 4, 2], ["Kraków", 2, 1], ["Papr", 7, 3], ["kox", 0.5, 4]]
C3 = [["Wrocław", 0, 12], ["Warszawa", 1, 3], ["Gdańsk", 2, 8], ["Kraków", 12, -5], ["Papr", 4, -1], ["kox", 8, 9]]
C4 = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],
      ['I', 0.5, 2.5], ['J', 1.5, 3.5]]
C5 = [["A", 0, 2], ["B", 4, 3], ["C", 2, 4], ["D", 3, 1], ["E", 1, 3], ["F", 0.5, -2]]
C6 = [["Wrocław", 0, 2], ["Warszawa",4,3], ["Gdańsk", 2,4], ["Kraków",3,1]]
C7 = [["1", 0, 1], ["2", 1, -6], ["3", 3, -1], ["4", 6, -2], ["5", 10, 1], ["6", 14, 3], ["7", 9, 4], ["8", 7, 2], ["9", 4, 3], ["10", 2, 3]]
C8 = [['s', 9, 24], ['e', 11, 2], ['y', -5, 26], ['a', 28, -17], ['i', 23, 11], ['W', -24, -24], ['h', 29, 24],
     ['*', -25, 27], ['U', 22, -16], ['b', 5, 2], ['j', 15, -25], ['s', 24, -10], ['i', -9, 9], ['k', 18, 4],
     ['e', -19, 10], ['t', 16, -3], ['W', 30, 10], ['c', 26, 11], ['s', -20, -17], ['z', -17, 27]]
C9 = [["1",0,1], ["2", 1, -6]]
C10 = [["Wrocław", 0, 2], ["Warszawa",4,3],["Gdańsk", 2,4], ["Kraków",3,1]]

bitonicTSP(C0)
bitonicTSP(C1)
bitonicTSP(C2)
bitonicTSP(C3)
bitonicTSP(C4)
bitonicTSP(C5)
bitonicTSP(C6)
bitonicTSP(C7)
bitonicTSP(C8)
bitonicTSP(C9)
bitonicTSP(C10)