"""Zadanie 1. (problem stacji benzynowych) Czołg jedzie z punktu A do punktu B. Spalanie czołgu to
dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A
do B to prosta, na której znajdują się stacje benzynowe (na pozycjach będących liczbami naturalnymi; A
jest na pozycji 0). Proszę podać algorytmy dla następujących przypadków:
(1) Wyznaczamy stacje na których tankujemy tak, żeby łączna liczba tankowań była minimalna.
(2) Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma dodatkowo cenę za litr paliwa). Na każdej stacji możemy tankować dowolną ilość paliwa.
(3) j.w., ale jeśli na stacji tankujemy, to musimy zatankować do pełna.
"""from math import inf


def always_refuel(p, s, l, target):
    n = len(s)
    F = [inf] * n
    F[0] = p[0] * s[0]
    lowest = inf
    for i in range(1, n):
        l_i = -1
        for k in range(i):
            dist = s[i] - s[k]
            if dist <= l:
                F[i] = min(F[k] + p[i] * dist, F[i])
        if target - s[i] < l:
            lowest = min(lowest, F[i])
    print(lowest)


p = [1, 2, 3, 4, 5, 6, 7]
s = [3, 6, 7, 9, 12, 13, 15]
always_refuel(p, s, 5, 15)
