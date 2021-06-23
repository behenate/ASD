X = [0.25, 0.5, 0.75, 1, 1.6, 2.6, 2.7, 2.8, 2.95, 3.8]

index = 0
l_start = -1
l_end = -1
while l_end < X[-1]:
    n = X[index] + 1
    print(X[index], X[index] + 1)
    while index < len(X) and X[index] <= n:
        index += 1
    l_end = X[index - 1]
