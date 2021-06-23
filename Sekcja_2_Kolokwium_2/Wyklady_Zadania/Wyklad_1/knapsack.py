def knapsack(W, P, maxW):
    n = len(W)
    F = [[0 for _ in range(maxW + 1)] for _ in range(n)]
    for line in F:
        print(line)
    for i in range(W[0], maxW + 1):
        F[0][i] = P[0]

    for i in range(1, n):
        for w in range(maxW + 1):
            F[i][w] = F[i - 1][w]
            if W[i] <= w and F[i][w] < F[i - 1][w - W[i]] + P[i]:
                F[i][w] = F[i - 1][w - W[i]] + P[i]
    print(findsolution(W, P, F, len(W) - 1, maxW))
    return F[n - 1][maxW]



def findsolution(W, P, F, i, w):
    if i == 0:
        if W[i] <= w:
            return [0]
        return []
    if w - W[i] >= 0 and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return findsolution(W, P, F, i - 1, w - W[i]) + [i]
    return findsolution(W, P, F, i - 1, w)


wagi = [2, 2, 3, 15, 1, 4, 5, 6]
rzeczy = [40, 160, 70, 300, 70, 25, 25, 180]
print(knapsack(wagi, rzeczy, 15))
