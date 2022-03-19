from math import inf
stacks = [[2, 10], [8, 6], [3, 4]]
def pascal(S, n):
    m = len(S)
    F =[[0 for _ in range(m)]for _ in range(n+1)]
    sums = [len(stacks[i]) for i in range(m)]
    for i in range(1, m):
        sums[i] = sums[i-1] + sums[i]
    for i in range(1, n+1):
        if len(stacks[0]) >= i:
            F[i][0] = F[i-1][0] + stacks[0][i-1]
        else:
            F[i][0] = -inf

    for j in range(1,m):
        for i in range(1, n+1):
            if i > sums[j]:
                F[i][j] = -inf
                continue
            for k in range(len(stacks[j])+1):
                beauty = sum([stacks[j][u] for u in range(k)])
                F[i][j] = max(F[i-k][j-1] + beauty, F[i][j])
    for line in F:
        print(line)

pascal(stacks, 5)