from math import inf
"""Zadanie 1. (problem plecakowy) Proszę podać i zaimplementować algorytm znajdujący wartość optymalnego zbioru przedmiotów w dyskretnym problemie plecakowym. Algorytm powinien działać w czasie
wielomianowym względem liczby przedmiotów oraz sumy ich profitów."""
# Tablica n wierszy i suma cen kolumn
#

def knapsack(W, P, maxW):
    price_sum = 0
    for price in P:
        price_sum += price
    n = len(W)
    F = [[inf for _ in range(price_sum + 1)] for _ in range(n)]
    F[0][P[0]] = W[0]
    for i in range(n):
        F[i][0] = 0

    for w in range(1, n):
        for k in range(1, price_sum + 1):
            F[w][k] = F[w - 1][k]
            if F[w - 1][k - P[w]] + W[w] < F[w][k]:
                F[w][k] = F[w - 1][k - P[w]] + W[w]

    for line in F:
        print(line)
    target_index = -1
    for i in range(price_sum + 1):
        if F[n - 1][i] <= maxW and F[n - 1][i] != inf:
            target_index = i
    solution = findsolution(W, P, F, n - 1, target_index)
    print(target_index)
    return solution
    # return F[n - 1][maxW]


def findsolution(W, P, F, i, price):
    if i == 0:
        if P[i] <= price:
            return [0]
        return []
    # if price - P[i] == 0:
    #     return findsolution(W, P, F, i - 1, price - P[i]) + [i]

    if price - P[i] >= 0 and F[i][price] == F[i - 1][price - P[i]] + W[i]:
        return findsolution(W, P, F, i - 1, price - P[i]) + [i]
    return findsolution(W, P, F, i - 1, price)


ceny = [1, 2, 10]
wagi = [5, 3, 1]
print(knapsack(wagi, ceny, 9))
