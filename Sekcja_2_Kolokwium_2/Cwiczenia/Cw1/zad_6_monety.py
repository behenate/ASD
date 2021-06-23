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
