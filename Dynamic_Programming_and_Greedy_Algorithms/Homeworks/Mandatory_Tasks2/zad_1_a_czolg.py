"""
Zadanie 1. (problem stacji benzynowych) Czołg jedzie z punktu A do punktu B. Spalanie czołgu to
dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A
do B to prosta, na której znajdują się stacje benzynowe (na pozycjach będących liczbami naturalnymi; A
jest na pozycji 0). Proszę podać algorytmy dla następujących przypadków:
(1) Wyznaczamy stacje na których tankujemy tak, żeby łączna liczba tankowań była minimalna.
(2) Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma dodatkowo cenę za litr paliwa). Na każdej stacji możemy tankować dowolną ilość paliwa.
(3) j.w., ale jeśli na stacji tankujemy, to musimy zatankować do pełna."""
def least_refueling_path(l, s):
    p_i = 0
    n = len(s)
    refuel_cnt = 0
    for i in range(-1, n - 1, 1):
        if s[i + 1] - p_i > l:
            print("refueling at: ", s[i])
            if i != -1:
                p_i = s[i]
            else:
                p_i = s[0]
            refuel_cnt += 1
    return refuel_cnt


S = [4, 6, 9, 14, 16]
print(least_refueling_path(5, S))
