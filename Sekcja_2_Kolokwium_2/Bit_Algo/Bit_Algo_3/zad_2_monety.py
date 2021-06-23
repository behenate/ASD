coins = [1, 5, 10, 25, 100]
n = len(coins)
cnt = [0 for _ in range(n)]
cost = 126
while cost != 0:
    for i in range(n-1, -1, -1):
        if coins[i] <= cost:
            cnt[i] += 1
            cost -= coins[i]
print(cnt)