from math import inf
_G = [
    [0, 2, 0, 0, 0, 0, 0],
    [2, 0, 1, 3, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 3, 0, 0, 3, 0, 1],
    [0, 0, 1, 3, 0, 2, 0],
    [0, 0, 0, 0, 2, 0, 1],
    [0, 0, 0, 1, 0, 1, 0],
]

def floyd_warshall(G):
    n = len(G)
    S = [[G[i][j] if G[i][j] != 0 else inf for j in range(n)] for i in range(n)]
    P = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            P[i][j] = i
    min_cycle = inf
    for t in range(n):
        for i in range(n):
            for j in range(n):
                if S[i][t] + S[t][j] != inf and S[i][j] != inf and P[t][j] != j and P[t][j] != i and t!= j and t!=i and P[i][j] != P[j][t] and P[i][j] != P[i][t]:
                    print("Cycle: {} {} {}, len: {}, {} {} {}".format(i, j, t, S[i][j] + S[i][t] + S[t][j], S[i][j], S[i][t], S[t][j]))
                    min_cycle = min(min_cycle, S[i][j] + S[i][t] + S[t][j])
                tmp = S[i][j]
                S[i][j] = min(S[i][j], S[i][t] + S[t][j])
                if tmp != S[i][j]:
                    P[i][j] = P[t][j]
    for line in P:
        print(line)
    for line in S:
        print(line)
floyd_warshall(_G)
