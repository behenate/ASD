"""Zadanie 6. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania
kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda
kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5)."""
from math import inf


def change(coins, value):
    n = value + 1
    F = [inf for _ in range(n)]
    F[0] = 0
    for i in range(1, n):
        for coin in coins:
            if i - coin >= 0:
                F[i] = min(F[i], F[i - coin] + 1)
    print(F)
    return F[value]


_coins = [5, 10, 15, 20]
_value = 45
print(change(_coins, _value))
