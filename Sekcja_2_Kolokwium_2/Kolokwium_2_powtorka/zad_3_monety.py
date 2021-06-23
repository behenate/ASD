from math import inf


def pick_coins(coins, n):
    def pick_recur(i):
        if F[i] != inf:
            return F[i]

        for coin in coins:
            if i - coin > 0:
                F[i] = min(F[i], pick_recur(i - coin)+1)
        return F[i]
    F = [inf for _ in range(n + 1)]
    for coin in coins:
        F[coin] = 1
    r = pick_recur(n)
    print(F)
    print(r)

_coins = [8, 5, 4]

pick_coins(_coins, 15)
