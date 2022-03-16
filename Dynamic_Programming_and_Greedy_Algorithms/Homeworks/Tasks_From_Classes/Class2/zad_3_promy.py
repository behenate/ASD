"""
Zadanie 3. (ładowanie promu) Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce,
żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, który
wyznacza, które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut.
Auta muszą wjeżdżać w takiej kolejności, w jakiej są podane w tablicy A.
"""


def ferry(C, ll):
    n = len(C)
    F = [[[None for _ in range(n + 1)] for _ in range(ll+1)] for _ in range(ll+1)]
    for i in range(n, -1, -1):
        if ferry_recur(ll,ll,i,F,C):
            print(i)
            break


def ferry_recur(l, r, i, F, C):
    if i == 0:
        return True
    if l < 0 or r < 0:
        return 0
    if F[l][r][i] is not None:
        return F[l][r][i]
    F[l][r][i] = ferry_recur(l-C[i-1], r, i-1, F, C) or ferry_recur(l, r-C[i-1], i-1, F, C)
    return F[l][r][i]

C = [2, 3, 2, 1]
ferry(C, 2)
